#!/usr/bin/env ruby
require "zlib"

abort "uso: ruby chroma_png.rb entrada.png saida.png" unless ARGV.length == 2
data = File.binread(ARGV[0])
abort "PNG invalido" unless data.start_with?("\x89PNG\r\n\x1a\n".b)

chunks = {}
pos = 8
while pos < data.bytesize
  length = data[pos, 4].unpack1("N")
  type = data[pos + 4, 4]
  body = data[pos + 8, length]
  (chunks[type] ||= []) << body
  pos += 12 + length
end

width, height, depth, color, compression, filter, interlace = chunks.fetch("IHDR").first.unpack("NNCCCCC")
abort "formato PNG nao suportado" unless depth == 8 && [2, 6].include?(color) && interlace == 0
channels = color == 2 ? 3 : 4
stride = width * channels
raw = Zlib::Inflate.inflate(chunks.fetch("IDAT").join)
rows = []
previous = Array.new(stride, 0)
offset = 0

height.times do
  filter_type = raw.getbyte(offset)
  source = raw.byteslice(offset + 1, stride).bytes
  current = Array.new(stride, 0)
  stride.times do |x|
    left = x >= channels ? current[x - channels] : 0
    up = previous[x]
    upper_left = x >= channels ? previous[x - channels] : 0
    value = case filter_type
            when 0 then source[x]
            when 1 then source[x] + left
            when 2 then source[x] + up
            when 3 then source[x] + ((left + up) / 2)
            when 4
              p = left + up - upper_left
              pa, pb, pc = (p - left).abs, (p - up).abs, (p - upper_left).abs
              source[x] + (pa <= pb && pa <= pc ? left : (pb <= pc ? up : upper_left))
            else abort "filtro PNG desconhecido"
            end
    current[x] = value & 255
  end
  rows << current
  previous = current
  offset += stride + 1
end

output = +"".b
transparent_pixels = 0
rows.each do |row|
  output << "\x00"
  width.times do |x|
    i = x * channels
    r, g, b = row[i, 3]
    original_alpha = channels == 4 ? row[i + 3] : 255
    dominance = g - [r, b].max
    alpha = if g > 150 && dominance > 35
              ((140 - dominance) * 255 / 105.0).round.clamp(0, 255)
            else
              255
            end
    alpha = alpha * original_alpha / 255
    transparent_pixels += 1 if alpha < 16

    # Remove o reflexo verde apenas nos pixels semitransparentes da silhueta.
    if alpha.between?(1, 254)
      coverage = alpha / 255.0
      g = [[((g - (1.0 - coverage) * 255) / coverage).round, 0].max, 255].min
    elsif alpha == 0
      r = g = b = 0
    end
    output << [r, g, b, alpha].pack("C4")
  end
end

def chunk(type, body)
  [body.bytesize].pack("N") + type + body + [Zlib.crc32(type + body)].pack("N")
end

png = "\x89PNG\r\n\x1a\n".b
png << chunk("IHDR", [width, height, 8, 6, 0, 0, 0].pack("NNCCCCC"))
png << chunk("IDAT", Zlib::Deflate.deflate(output, Zlib::BEST_SPEED))
png << chunk("IEND", "".b)
File.binwrite(ARGV[1], png)
warn "#{width}x#{height}: #{transparent_pixels} pixels transparentes"
