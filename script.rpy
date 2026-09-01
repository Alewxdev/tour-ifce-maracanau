## Sinais do Maracanaú — recepção acessível aos calouros.

define alex = Character("Alex", color="#ff9fbd")
define ane = Character("Ane", color="#ffd166")
define lia = Character("Professora Lia", color="#7fe0aa")
define julia = Character("Júlia", color="#ff8fab")
define fabio = Character("Professor Fábio", color="#7fe0aa")
define edson = Character("Professor Edson", color="#8ed1fc")
define cicero = Character("Professor Cícero", color="#ffd166")
define otavio = Character("Professor Otávio", color="#b8a1ff")
define camila = Character("Professora Camila", color="#f2b84b")
define helena = Character("Professora Helena", color="#61d4c5")
define n = Character(None)

image bg entrada = Transform("campus/anime_frente_ifce.png", xysize=(1920, 1080), fit="cover")
image bg jardineira = Transform("campus/anime_jardineira.png", xysize=(1920, 1080), fit="cover")
image bg patio = Transform("campus/anime_corredor.png", xysize=(1920, 1080), fit="cover")
image bg laboratorio = Transform("campus/anime_laboratorio_informatica.png", xysize=(1920, 1080), fit="cover")
image bg biblioteca = Transform("campus/anime_biblioteca.png", xysize=(1920, 1080), fit="cover")
image bg biblioteca frente = Transform("campus/anime_frente_biblioteca.png", xysize=(1920, 1080), fit="cover")
image bg sala estudo = Transform("campus/anime_sala_estudo.png", xysize=(1920, 1080), fit="cover")
image bg sala = Transform("campus/anime_sala_aula.png", xysize=(1920, 1080), fit="cover")
image bg cantina real = Transform("campus/anime_cantina_easter_eggs.png", xysize=(1920, 1080), fit="cover")
image bg catraca = Transform("campus/anime_catraca_acesso.png", xysize=(1920, 1080), fit="cover")
image bg sagui = Transform("campus/anime_sagui_refeitorio.png", xysize=(1920, 1080), fit="cover")
image bg refeitorio = Transform("campus/anime_refeitorio.png", xysize=(1920, 1080), fit="cover")
image bg refeitorio interno = Transform("campus/anime_refeitorio_interno.png", xysize=(1920, 1080), fit="cover")
image bg piscina = Transform("campus/anime_piscina.png", xysize=(1920, 1080), fit="cover")
image bg ginasio = Transform("campus/anime_ginasio.png", xysize=(1920, 1080), fit="cover")
image bg pos creditos ane = Transform("campus/anime_pos_creditos_ane_jardineira.png", xysize=(1920, 1080), fit="cover")
image coxinha premio = "objetos/coxinha_magica.png"
image sagui suspeito = "objetos/sagui_suspeito.png"
image saguis coxinhas = "objetos/saguis_caixa_coxinhas.png"
image alex feliz = "personagens/alex_anime_v3_tatuagem.png"
image ane feliz = "Ane.png"
image lia feliz = "personagens/professora_lia.png"
image fabio aula = "personagens/professor_fabio.png"
image edson aula = "personagens/professor_edson.png"
image cicero aula = "personagens/professor_cicero.png"
image otavio aula = "personagens/professor_otavio.png"

# Cada folha possui três retratos: padrão/explicando, reação e feliz.
image alex retrato = Crop((0, 0, 512, 1024), "personagens/expressoes_alex_transparente.png")
image alex surpreso = Crop((512, 0, 512, 1024), "personagens/expressoes_alex_transparente.png")
image alex pensando = Crop((1024, 0, 512, 1024), "personagens/expressoes_alex_transparente.png")
# As folhas abaixo foram exportadas em resolucoes diferentes. Cada recorte usa
# exatamente um terco do arquivo e e normalizado para a mesma altura de palco.
image ane retrato = Transform(Crop((0, 0, 512, 1024), "personagens/expressoes_ane_transparente.png"), ysize=1024, fit="contain")
image ane surpresa = Transform(Crop((512, 0, 512, 1024), "personagens/expressoes_ane_transparente.png"), ysize=1024, fit="contain")
image ane rindo = Transform(Crop((1024, 0, 512, 1024), "personagens/expressoes_ane_transparente.png"), ysize=1024, fit="contain")
image julia retrato = "personagens/julia_retrato.png"
image julia preocupada = "personagens/julia_preocupada.png"
image julia rindo = "personagens/julia_rindo.png"
image lia explicando = Transform(Crop((0, 0, 591, 887), "personagens/expressoes_lia_transparente.png"), ysize=1024, fit="contain")
image lia seria = Transform(Crop((591, 0, 591, 887), "personagens/expressoes_lia_transparente.png"), ysize=1024, fit="contain")
image lia aprovando = Transform(Crop((1182, 0, 592, 887), "personagens/expressoes_lia_transparente.png"), ysize=1024, fit="contain")
image fabio explicando = Transform(Crop((0, 0, 512, 1024), "personagens/expressoes_fabio_transparente.png"), ysize=1024, fit="contain")
image fabio surpreso = Transform(Crop((512, 0, 512, 1024), "personagens/expressoes_fabio_transparente.png"), ysize=1024, fit="contain")
image fabio feliz = Transform(Crop((1024, 0, 512, 1024), "personagens/expressoes_fabio_transparente.png"), ysize=1024, fit="contain")
image edson explicando = Transform(Crop((0, 0, 512, 1024), "personagens/expressoes_edson_transparente.png"), ysize=940, fit="contain")
image edson pensando = Transform(Crop((512, 0, 512, 1024), "personagens/expressoes_edson_transparente.png"), ysize=940, fit="contain")
image edson feliz = Transform(Crop((1024, 0, 512, 1024), "personagens/expressoes_edson_transparente.png"), ysize=940, fit="contain")
image cicero explicando = Transform(Crop((0, 0, 591, 887), "personagens/expressoes_cicero_transparente.png"), ysize=1024, fit="contain")
image cicero desconfiado = Transform(Crop((591, 0, 591, 887), "personagens/expressoes_cicero_transparente.png"), ysize=1024, fit="contain")
image cicero feliz = Transform(Crop((1182, 0, 592, 887), "personagens/expressoes_cicero_transparente.png"), ysize=1024, fit="contain")
image otavio explicando = Transform(Crop((0, 0, 724, 724), "personagens/expressoes_otavio_transparente.png"), ysize=1024, fit="contain")
image otavio surpreso = Transform(Crop((724, 0, 724, 724), "personagens/expressoes_otavio_transparente.png"), ysize=1024, fit="contain")
image otavio feliz = Transform(Crop((1448, 0, 724, 724), "personagens/expressoes_otavio_transparente.png"), ysize=1024, fit="contain")
image camila explicando = Transform(Crop((0, 0, 512, 1024), "personagens/expressoes_camila_transparente.png"), ysize=1024, fit="contain")
image camila preocupada = Transform(Crop((512, 0, 512, 1024), "personagens/expressoes_camila_transparente.png"), ysize=1024, fit="contain")
image camila feliz = Transform(Crop((1024, 0, 512, 1024), "personagens/expressoes_camila_transparente.png"), ysize=1024, fit="contain")
image helena explicando = Transform(Crop((0, 0, 512, 1024), "personagens/expressoes_helena_transparente.png"), ysize=1024, fit="contain")
image helena surpresa = Transform(Crop((512, 0, 512, 1024), "personagens/expressoes_helena_transparente.png"), ysize=1024, fit="contain")
image helena feliz = Transform(Crop((1024, 0, 512, 1024), "personagens/expressoes_helena_transparente.png"), ysize=1024, fit="contain")

default pontos_libras = 0
default lugares_visitados = []

transform entrar_esquerda:
    xalign -0.25 yalign 1.0 alpha 0.0
    easeout 0.55 xalign 0.28 alpha 1.0

transform entrar_centro:
    xalign 0.5 yalign 1.0 alpha 0.0 zoom 0.92
    easeout_back 0.55 alpha 1.0 zoom 1.0

transform entrar_direita:
    xalign 0.88 yalign 1.0 alpha 0.0
    # Mantem a personagem fora do painel fixo de Libras no lado direito.
    easeout 0.55 xalign 0.64 alpha 1.0

transform flutuar:
    yoffset 0
    ease 1.4 yoffset -10
    ease 1.4 yoffset 0
    repeat

transform reagir_surpresa:
    yoffset 0
    easeout_back 0.20 yoffset -55
    easein 0.22 yoffset 0

transform reagir_riso:
    xoffset 0 rotate 0
    ease 0.10 xoffset -12 rotate -2
    ease 0.10 xoffset 12 rotate 2
    ease 0.10 xoffset -8 rotate -1
    ease 0.10 xoffset 0 rotate 0

transform reagir_pensando:
    yoffset 0
    ease 0.45 yoffset -14
    ease 0.45 yoffset 0
    repeat 2

# Enquadramento acelerado para a gag anime depois dos creditos.
transform corrida_pos_creditos:
    size (1920, 1080)
    zoom 1.08 xalign 0.58 yalign 0.5 xoffset 0
    parallel:
        ease 1.8 zoom 1.0 xalign 0.5
    parallel:
        linear 0.055 xoffset -7
        linear 0.055 xoffset 7
        repeat 16

# Movimentos mais vivos para cenas de passeio e apresentação do campus.
transform chegar_saltando_esquerda:
    xalign -0.22 yalign 1.0 alpha 0.0 yoffset 35 rotate -3
    parallel:
        easeout_back 0.75 xalign 0.27 alpha 1.0 rotate 0
    parallel:
        pause 0.20
        ease 0.16 yoffset -22
        easeout_bounce 0.32 yoffset 0

transform chegar_saltando_direita:
    xalign 1.18 yalign 1.0 alpha 0.0 yoffset 35 rotate 3
    parallel:
        easeout_back 0.82 xalign 0.64 alpha 1.0 rotate 0
    parallel:
        pause 0.27
        ease 0.16 yoffset -20
        easeout_bounce 0.32 yoffset 0

transform conversar_esquerda:
    xalign 0.27 yalign 1.0
    ease 0.42 yoffset -9 rotate -1
    ease 0.42 yoffset 0 rotate 0
    repeat

transform conversar_direita:
    xalign 0.64 yalign 1.0
    ease 0.42 yoffset -9 rotate 1
    ease 0.42 yoffset 0 rotate 0
    repeat

transform confirmar_animado_direita:
    xalign 0.64 yalign 1.0
    ease 0.16 yoffset 12
    easeout_back 0.24 yoffset -8
    easeout_bounce 0.34 yoffset 0

transform destaque_professor:
    xalign 0.5 yalign 1.0 alpha 0.0 zoom 0.72
    easeout_back 0.55 alpha 1.0 zoom 0.78

transform retrato_centro:
    xalign 0.5 yalign 1.0 alpha 0.0 zoom 0.72
    easeout 0.30 alpha 1.0 zoom 0.78

# Entra junto da mão de Ane e continua viva em cena, como um pequeno troféu.
transform coxinha_na_mao:
    xpos 0.405 ypos 0.64 anchor (0.5, 0.5)
    alpha 0.0 zoom 0.04 rotate -18
    parallel:
        easeout_back 0.85 alpha 1.0 zoom 0.16 rotate 5
    parallel:
        pause 0.85
        ease 0.75 yoffset -12
        ease 0.75 yoffset 0
        repeat

transform coxinha_comemora:
    xpos 0.5 ypos 0.48 anchor (0.5, 0.5)
    alpha 0.0 zoom 0.08 rotate -12
    easeout_back 0.75 alpha 1.0 zoom 0.27 rotate 8
    ease 0.18 yoffset -35 rotate -5
    easeout_bounce 0.40 yoffset 0 rotate 0
    ease 0.9 zoom 0.25
    ease 0.9 zoom 0.27
    repeat

transform sagui_espiando:
    xpos 0.075 ypos 0.56 anchor (0.5, 0.5)
    alpha 0.0 zoom 0.12 xoffset -90
    easeout_back 0.7 alpha 1.0 xoffset 0
    ease 1.1 rotate -2
    ease 1.1 rotate 2
    repeat

transform saguis_revelacao:
    xpos 0.50 ypos 0.58 anchor (0.5, 0.5)
    alpha 0.0 zoom 0.16 yoffset 120
    easeout_back 1.0 alpha 1.0 zoom 0.52 yoffset 0
    ease 1.2 yoffset -7
    ease 1.2 yoffset 0
    repeat

transform reacao_extrema_esquerda:
    xpos 0.08 ypos 1.0 anchor (0.5, 1.0)
    alpha 0.0 zoom 0.34
    easeout_back 0.55 alpha 1.0

transform reacao_esquerda:
    xpos 0.25 ypos 1.0 anchor (0.5, 1.0)
    alpha 0.0 zoom 0.34
    pause 0.12
    easeout_back 0.55 alpha 1.0

transform reacao_direita:
    xpos 0.79 ypos 1.0 anchor (0.5, 1.0)
    alpha 0.0 zoom 0.34
    pause 0.24
    easeout_back 0.55 alpha 1.0

label start:
    play music "audio/musica_tema_ambiente.mp3" fadein 1.5 volume 0.70
    $ pontos_libras = 0
    $ lugares_visitados = []
    $ sinais_desbloqueados = []
    $ conquistas = []
    $ pistas_encontradas = []
    $ respostas_corretas = 0
    $ respostas_totais = 0
    $ repeticoes_libras = 0
    $ glossario_sinal = "LIBRAS"
    $ teste_final_acertos = 0
    $ tentativas_teste_final = 0
    $ desbloquear_sinal("LIBRAS")
    $ desbloquear_sinal("ALUNO")

    window hide
    scene bg entrada:
        size (1920, 1080)
        zoom 1.08
        linear 1.4 zoom 1.0
    with Fade(0.6, 0.1, 0.5, color="#071c19")
    pause 0.7
    scene bg laboratorio:
        size (1920, 1080)
        alpha 0.25
        linear 0.7 alpha 1.0
    with dissolve
    pause 0.55
    scene bg ginasio:
        size (1920, 1080)
        xalign 0.5
    with dissolve
    pause 0.55
    scene bg entrada:
        size (1920, 1080)
        zoom 1.04
        linear 5.0 zoom 1.0
    with Fade(0.7, 0.2, 0.8, color="#0b2b21")

    centered "{size=64}{color=#7fe0aa}SINAIS DO MARACANAÚ{/color}{/size}\n{size=32}Uma recepção aos calouros do IFCE{/size}"
    n "No primeiro dia, Alex chegou ao IFCE Campus Maracanaú com uma missão: conhecer o campus e não perder a reunião dos calouros."
    n "Alex é surdo, sua primeira língua é Libras e ele percebe o mundo principalmente com os olhos."

    show alex feliz at entrar_esquerda:
        zoom 0.48
    alex "Campus novo, pessoas novas e muitos corredores. Vamos começar."
    show ane feliz at entrar_direita:
        zoom 0.46
    ane "Oi! Eu sou Ane. Estou aprendendo Libras e posso acompanhar você no passeio."
    alex "Ótimo. Só uma regra: fale de frente para mim e não esconda as mãos."
    ane "Combinado. Se eu errar um sinal, você pode me ajudar."
    $ desbloquear_sinal("AJUDAR")

    menu:
        "Como Ane deve chamar a atenção de Alex?"
        "Tocar levemente no ombro e entrar no campo de visão":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            $ conceder_conquista("Mãos à vista")
            alex "Certo! Agora eu posso ver você antes da conversa começar."
        "Gritar do outro lado do pátio":
            $ registrar_resposta(False)
            ane "Isso não funciona. Melhor entrar no campo de visão de Alex."
            alex "Agora sim. Comunicação também começa com respeito."

    hide ane
    hide alex
    with dissolve
    jump apresentacao_jardineira

label apresentacao_jardineira:
    scene bg jardineira:
        size (1920, 1080)
        xalign 0.5
        yalign 0.5
        zoom 1.06
        ease 3.2 zoom 1.0
    with Fade(0.65, 0.15, 0.75, color="#d9f2df")

    n "Ainda em frente ao campus, Alex e Ane encontraram a jardineira do IFCE estacionada perto da entrada."
    show alex feliz at chegar_saltando_esquerda:
        zoom 0.43
    show ane feliz at chegar_saltando_direita:
        zoom 0.42
    pause 0.35

    show ane feliz at conversar_direita:
        zoom 0.42
    ane "Esta é a jardineira. Ela busca estudantes no metrô e os traz até o IFCE Campus Maracanaú."
    show alex feliz at conversar_esquerda:
        zoom 0.43
    alex "E no sentido de volta ela leva estudantes do campus até o metrô. Isso ajuda bastante no deslocamento."
    show ane feliz at confirmar_animado_direita:
        zoom 0.42
    ane "Os horários podem mudar. Antes de usar o transporte, confiram os horários disponíveis nos avisos oficiais do campus."
    alex "Também é importante chegar com antecedência, organizar a fila e avisar a equipe quando alguém precisar de apoio de acessibilidade."
    n "Com a orientação anotada, os dois seguiram da frente do campus para a recepção."

    hide ane
    hide alex
    with dissolve
    scene bg entrada:
        size (1920, 1080)
        zoom 1.03
        ease 1.8 zoom 1.0
    with pushleft

    n "A primeira parada seria a recepção. Mas um cartaz chamou a atenção dos dois."
    centered "{size=48}{color=#ffd166}MISTÉRIO DO DIA{/color}{/size}\nA coxinha de boas-vindas desapareceu!"
    ane "A reunião dos calouros sem coxinha? Isso já virou emergência acadêmica."
    alex "Vamos procurar. Assim conhecemos o campus e salvamos o intervalo."
    jump catraca_acesso

label catraca_acesso:
    scene bg catraca:
        size (1920, 1080)
        xalign 0.5
        yalign 0.5
        zoom 1.05
        ease 2.5 zoom 1.0
    with pushleft

    n "Depois da recepção, Alex e Ane chegaram à catraca de entrada do campus."
    show alex feliz at entrar_esquerda:
        zoom 0.42
    show ane feliz at entrar_direita:
        zoom 0.42
    ane "Esta é a catraca. Para entrar, aproximamos o cartão de acesso do leitor e esperamos a liberação."
    alex "Então o cartão confirma que somos estudantes e permite nossa entrada no campus."
    ane "Isso. Ele também pode receber recarga para comprar o almoço no refeitório. É bom conferir o saldo antes da fila."

    menu:
        "Como usar o cartão na catraca?"
        "Aproximar o cartão do leitor e aguardar a confirmação":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            alex "Certo. O leitor confirma o acesso e a catraca é liberada."
        "Forçar a barra da catraca":
            $ registrar_resposta(False)
            ane "Melhor não. Se o cartão falhar, devemos procurar a recepção para receber ajuda."

    ane "Cartão guardado. Agora podemos continuar o passeio."
    jump patio

label patio:
    $ lugares_visitados.append("Pátio")
    scene bg patio:
        size (1920, 1080)
        xalign 0.5 zoom 1.06
        ease 3.0 zoom 1.0
    with pushleft
    n "O pátio liga diferentes áreas do campus e é ponto de encontro, descanso e atividades acadêmicas."
    show ane feliz at entrar_esquerda:
        zoom 0.43
    show julia retrato at entrar_direita:
        zoom 0.44
    julia "Bem-vindos! Eu sou Júlia, monitora da biblioteca e estudante de Ciência da Computação."
    ane "Júlia, você viu uma coxinha muito importante passar por aqui?"
    show julia rindo at entrar_direita:
        zoom 0.44
    julia "Vi uma caixa passeando para o lado da biblioteca. Parecia um projeto com fome."
    alex "Antes de seguir, ensine aos calouros um sinal útil."
    julia "Este é o sinal de BIBLIOTECA. Veja o vídeo e depois tente fazer."
    $ desbloquear_sinal("BIBLIOTECA")
    $ renpy.notify("Novo sinal aprendido: BIBLIOTECA")

    menu:
        "O vídeo passou rápido. O que fazer?"
        "Usar o botão para repetir o sinal":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            $ desbloquear_sinal("VEZES")
            julia "Perfeito. Aprender Libras precisa de atenção, prática e repetição."
        "Fingir que entendeu":
            $ registrar_resposta(False)
            alex "Pode pedir para repetir. Ninguém precisa disfarçar uma dúvida."

    n "Júlia propôs um teste rápido: reconhecer o sinal sem usar a legenda como cola acadêmica."
    $ resposta_quiz = renpy.call_screen("quiz_libras", "BIBLIOTECA", "Qual lugar foi apresentado no vídeo?", ["Biblioteca", "Cantina", "Piscina"])
    if resposta_quiz == "Biblioteca":
        $ pontos_libras += 1
        $ registrar_resposta(True)
        julia "Acertou! O olhar atento passou no teste sem precisar de recuperação."
    else:
        $ registrar_resposta(False)
        julia "Era BIBLIOTECA. Revise o vídeo no Caderno de Libras; repetir faz parte do aprendizado."

    julia "Vamos à Biblioteca Rachel de Queiroz. Lá temos livros, estudo e jogos."
    jump biblioteca

label biblioteca:
    $ lugares_visitados.append("Biblioteca Rachel de Queiroz")
    scene bg biblioteca frente:
        size (1920, 1080)
    with dissolve
    n "Na Biblioteca Rachel de Queiroz, os calouros encontram acervo, espaços de estudo e apoio para pesquisar."
    scene bg biblioteca:
        size (1920, 1080)
    with pushleft
    show julia retrato at entrar_esquerda:
        zoom 0.44
    show alex feliz at entrar_direita:
        zoom 0.43
    julia "Aqui também existe uma regra difícil: devolver o livro e não levar a coxinha para a estante."
    show julia preocupada at entrar_esquerda:
        zoom 0.44
    ane "Tem um guardanapo dobrado no marcador deste livro. Ou é pista, ou alguém levou o conceito de leitura com lanche longe demais."
    show sagui suspeito at sagui_espiando
    n "Por uma fração de segundo, uma cauda listrada apareceu junto à janela. Quando Júlia olhou, restava apenas um silêncio extremamente suspeito."
    hide sagui suspeito with dissolve
    alex "Encontrei uma pista: uma nota dizendo LABORATÓRIO CINCO."
    $ registrar_pista("Bilhete: LABORATÓRIO CINCO")
    julia "O mistério sabe escrever, mas ainda precisa melhorar a letra."
    n "Antes de sair, Júlia apresenta mais dois sinais disponíveis no jogo."
    julia "Para estudar aqui, você pode LER e usar o COMPUTADOR."
    $ desbloquear_sinal("COMPUTADOR")
    $ renpy.notify("Sinais aprendidos: LER e COMPUTADOR")
    jump sala_estudo

label sala_estudo:
    $ lugares_visitados.append("Sala de estudos da biblioteca")
    scene bg sala estudo:
        size (1920, 1080)
        zoom 1.03
        ease 2.0 zoom 1.0
    with pushleft
    n "No segundo andar da biblioteca, Alex, Ane e Júlia conheceram a sala de estudos, um espaço reservado para leitura, pesquisa e trabalhos em grupo."
    show julia retrato at entrar_esquerda:
        zoom 0.42
    show ane feliz at entrar_direita:
        zoom 0.40
    julia "Aqui no segundo andar, podemos estudar com mais tranquilidade. Para conversar, é importante respeitar quem precisa de silêncio e manter Alex no campo de visão."
    ane "Então nada de chamar alguém de costas ou esconder as mãos atrás de uma pilha de livros."
    show alex feliz at entrar_centro:
        zoom 0.40
    alex "Exato. Podemos organizar as cadeiras para que todas as pessoas se vejam durante um trabalho em grupo."
    n "Depois de conhecer o espaço, o grupo desceu da biblioteca e seguiu a pista até o laboratório."
    jump laboratorio

label laboratorio:
    $ lugares_visitados.append("Laboratórios de informática")
    scene bg laboratorio:
        size (1920, 1080)
        alpha 0.0
        linear 0.6 alpha 1.0
    n "Os laboratórios de informática apoiam aulas práticas, programação e projetos de Ciência da Computação."
    show lia explicando at retrato_centro
    lia "Olá! Eu sou a professora Lia. Bem-vindos à Ciência da Computação do IFCE Maracanaú."
    $ desbloquear_sinal("PROFESSOR")
    hide lia with dissolve
    show alex feliz at entrar_esquerda:
        zoom 0.43
    show ane feliz at entrar_direita:
        zoom 0.43
    ane "Professora, procuramos uma coxinha desaparecida. A investigação agora também é computacional."
    alex "Nossa hipótese aponta para este laboratório e para um computador com uma mensagem aberta."
    show lia explicando at retrato_centro
    lia "A caixa esteve aqui, mas seguiu para a sala. Antes disso, temos uma missão de Computação e Libras."

    n "Na tela havia um pequeno programa: ele deveria mostrar a próxima pista, mas repetia a palavra COXINHA para sempre."
    alex "E existe uma migalha entre as teclas C e X. O culpado escreve COXINHA com dedicação prática."
    show sagui suspeito at sagui_espiando
    ane "Mais alguém viu um estagiário muito peludo auditando o laboratório?"
    hide sagui suspeito with dissolve
    ane "Encontramos um bug com fome infinita. Isso é sofisticado ou preocupante?"
    julia "Na Computação, chamamos isso de laço infinito. Na cantina, chamamos de terça-feira."

    menu:
        "Como corrigir o programa?"
        "Revisar a condição de parada do laço":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            $ conceder_conquista("Caçador de bugs")
            alex "Certo. Um algoritmo precisa saber quando continuar e quando parar."
        "Desligar o computador e dizer que foi mistério":
            $ registrar_resposta(False)
            show lia seria at retrato_centro
            lia "Criativo, mas não resolve o programa. Vamos ler a mensagem e revisar o código."

    n "Alex corrigiu a condição. O programa mostrou: PROCURE NA SALA DE AULA."
    $ registrar_pista("Programa: PROCURE NA SALA DE AULA")
    lia "Programar é organizar ideias, testar, errar, revisar e tentar outra vez."

    menu:
        "Qual atitude facilita uma conversa em Libras?"
        "Manter boa iluminação e as mãos visíveis":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            lia "Exatamente. Expressões do rosto e movimentos das mãos fazem parte da língua."
        "Apagar a luz para ver apenas o computador":
            $ registrar_resposta(False)
            lia "Computador no escuro parece cinema, mas impede a comunicação visual."
            alex "Vamos manter a luz e as mãos visíveis."

    lia "Libras é uma língua completa, com estrutura própria. Não é português feito palavra por palavra."
    lia "Os vídeos deste jogo mostram sinais isolados para apoiar o aprendizado. Uma tradução deve ser revisada por pessoa fluente."
    lia "Software acessível começa no planejamento. Legenda, Libras e interface visual não devem ficar para depois."
    show lia aprovando at retrato_centro
    $ renpy.notify("Sinal aprendido: ACESSIBILIDADE")
    $ desbloquear_sinal("ACESSIBILIDADE")
    $ desbloquear_sinal("APRENDER")
    jump sala

label sala:
    $ lugares_visitados.append("Salas de aula")
    scene bg sala:
        size (1920, 1080)
    with Fade(0.45, 0.15, 0.55, color="#ffffff")
    n "As salas de aula são espaços de teoria, debate e trabalho em equipe. A última pista estava sobre a mesa."
    show julia rindo at entrar_esquerda:
        zoom 0.44
    show ane feliz at entrar_direita:
        zoom 0.42
    julia "A caixa está aqui! O mistério acabou antes da prova."
    ane "Mas ela está vazia. Temos agora o mistério da coxinha invisível."
    $ registrar_pista("Caixa vazia com a mensagem: A COXINHA ESTÁ NA REUNIÃO")
    show alex feliz at entrar_centro:
        zoom 0.42
    alex "Vejam a mensagem: A COXINHA ESTÁ NA REUNIÃO. A caixa era somente a pista."
    hide alex feliz with dissolve
    show lia feliz at entrar_centro:
        zoom 0.48
    lia "Parabéns. O passeio era a primeira atividade de recepção dos calouros."
    lia "Vocês conheceram o pátio, a biblioteca, os laboratórios e as salas. Também resolveram o primeiro bug do curso."
    ane "Então ninguém roubou a coxinha?"
    julia "Ainda não. Mas a reunião vai começar, então precisamos ir rápido."

    menu:
        "Antes da reunião, qual sinal você quer repetir?"
        "BIBLIOTECA":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            julia "BIBLIOTECA. Um lugar para ler, estudar e encontrar ajuda."
        "COMPUTADOR":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            ane "COMPUTADOR. Nosso colega de projetos e fornecedor oficial de mensagens de erro."
        "ACESSIBILIDADE":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            lia "ACESSIBILIDADE. Ela deve estar presente desde o começo de cada projeto."

    n "Antes do próximo corredor, Lia abriu o Desafio de Memória Visual: três associações entre sinais e situações do campus."
    $ memoria_acertos = 0
    menu:
        "Qual sinal combina com pesquisar livros e estudar?"
        "BIBLIOTECA":
            $ memoria_acertos += 1
            $ registrar_resposta(True)
        "COXINHA":
            $ registrar_resposta(False)
            ane "Só se o livro for um raro Tratado Geral dos Salgados."
    menu:
        "Qual sinal combina com programar no laboratório?"
        "COMPUTADOR":
            $ memoria_acertos += 1
            $ registrar_resposta(True)
        "PISCINA":
            $ registrar_resposta(False)
            julia "Computador e água formam um projeto com banca de avaliação e bombeiros."
    menu:
        "Qual conceito deve existir desde o planejamento de um projeto?"
        "ACESSIBILIDADE":
            $ memoria_acertos += 1
            $ registrar_resposta(True)
        "MISTÉRIO":
            $ registrar_resposta(False)
            lia "Mistério pode ficar para o roteiro. Acessibilidade começa no planejamento."
    if memoria_acertos == 3:
        $ pontos_libras += 2
        $ conceder_conquista("Memória visual")
        lia "Três acertos! A memória visual de vocês está mais organizada que a fila da cantina."
    else:
        lia "Bom começo. Os vídeos ficaram no Caderno de Libras para revisão sem pressa."
    jump piscina

label piscina:
    $ lugares_visitados.append("Piscina e complexo esportivo")
    scene bg piscina:
        size (1920, 1080)
        zoom 1.03
        ease 2.0 zoom 1.0
    with Fade(0.55, 0.15, 0.65, color="#63d7ee")

    n "A caminho da reunião, Júlia indicou um atalho pelo complexo esportivo. Foi assim que o grupo encontrou a piscina do campus."
    n "O espaço recebe atividades de Educação Física e aulas de natação, sempre com planejamento, orientação profissional e regras de segurança."

    show julia rindo at entrar_esquerda:
        zoom 0.42
    show ane feliz at entrar_direita:
        zoom 0.40
    julia "Aqui acontecem as aulas de natação. Hoje é só visita: uniforme, mochila e caderno não contam como equipamento aquático."
    ane "Ainda bem. Se eu entrar assim, a disciplina vira Natação Aplicada à Lavagem de Mochila."
    julia "Com prática obrigatória de resgate do caderno."

    hide julia with dissolve
    hide ane with dissolve
    show alex feliz at entrar_centro:
        zoom 0.43
    alex "Na piscina, atenção visual também é segurança. As instruções devem ser apresentadas antes da entrada na água e confirmadas por toda a turma."
    n "Em uma aula acessível, o professor combina sinais visuais, mantém contato de frente com os estudantes e explica previamente os avisos e procedimentos de emergência."

    menu:
        "Qual é a atitude correta antes de uma aula de natação?"
        "Aguardar a orientação, observar a sinalização e não correr no deck":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            $ desbloquear_sinal("CUIDADO")
            alex "Perfeito. Primeiro vêm a orientação e a segurança; depois, a atividade na água."
            $ renpy.notify("Boa prática aprendida: segurança na piscina")
        "Correr até a borda e mergulhar antes da explicação":
            $ registrar_resposta(False)
            alex "O piso pode estar molhado e nem todo ponto permite mergulho. É preciso aguardar o professor e conhecer as regras do espaço."

    hide alex with dissolve
    show julia retrato at entrar_esquerda:
        zoom 0.42
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "E a coxinha? Será que ela tentou atravessar a piscina?"
    julia "Sem touca e sem autorização? Seria a pista mais indisciplinada do campus."
    ane "Então continuamos secos e seguimos para a reunião. Meu caderno agradece."
    n "O grupo retomou o caminho sabendo onde acontecem as atividades aquáticas e como participar delas com responsabilidade."
    jump ginasio

label ginasio:
    $ lugares_visitados.append("Ginásio e quadra poliesportiva")
    scene bg ginasio:
        size (1920, 1080)
        zoom 1.04
        ease 2.4 zoom 1.0
    with pushleft

    n "Ao lado do complexo aquático, a quadra e as arquibancadas recebem aulas, jogos, eventos e aquela torcida que descobre um talento súbito para ser narrador esportivo."

    window hide
    $ segredo_quadra = renpy.call_screen("easter_egg_quadra")
    window auto
    if segredo_quadra == "jinx":
        with hpunch
        centered "{size=62}{color=#31dfff}EASTER EGG ENCONTRADO!{/color}{/size}\n{size=31}{color=#ff68c5}As tranças azuis causaram uma pequena interferência no placar...{/color}{/size}"
        $ conceder_conquista("Caos na arquibancada")
        show ane surpresa at entrar_esquerda
        ane "Alex... aquela garota de tranças azuis acabou de olhar para o placar e ele começou a piscar."
        show alex surpreso at entrar_direita
        alex "E a lutadora de azul ao lado dela nem parece surpresa. Melhor classificarmos isso como intercâmbio cultural não autorizado."
        ane "Conquista secreta registrada. E, por segurança, ninguém entrega uma chave de fenda para a arquibancada."
        hide ane
        hide alex
        with dissolve

    show ane rindo at entrar_esquerda
    show alex retrato at entrar_direita
    ane "Aqui a comunicação precisa alcançar quem está longe. O professor pode combinar bandeiras, luzes e gestos visuais antes da atividade."
    alex "E deve garantir que a pessoa surda viu o aviso. Apitar com mais vontade não transforma som em legenda."
    ane "Anotado: menos pulmão de juiz, mais planejamento acessível."

    menu:
        "Durante um jogo, como tornar uma instrução urgente acessível?"
        "Combinar antes um sinal visual e confirmar que todos entenderam":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            $ desbloquear_sinal("ENTENDER")
            alex "Perfeito. O combinado visual precisa ser conhecido antes do jogo e visível no momento certo."
            $ renpy.notify("Boa prática aprendida: avisos visuais")
        "Gritar a mesma instrução cada vez mais alto":
            $ registrar_resposta(False)
            ane "O volume só sobe o drama. Para incluir, precisamos de um aviso visual previamente combinado."

    alex "Hora da revisão visual: ao observar um sinal, note configuração das mãos, movimento, localização, orientação e expressão facial."
    show sagui suspeito at sagui_espiando
    ane "Até o sagui está prestando atenção. Ou está esperando a parte sobre localização da coxinha."
    hide sagui suspeito with dissolve
    n "Esses cinco parâmetros ajudam a distinguir sinais em Libras. Aprender não é copiar apenas um movimento: é observar o sinal completo e praticar com respeito."
    ane "Cinco parâmetros? Minha coxinha tem só um: desaparecimento. Melhor seguirmos para a cantina."
    jump cantina

label cantina:
    $ lugares_visitados.append("Cantina")
    if len(lugares_visitados) >= len(locais_mapa):
        $ conceder_conquista("Guia do campus")
    scene bg cantina real:
        size (1920, 1080)
        zoom 1.03
        ease 2.0 zoom 1.0
    with Fade(0.55, 0.15, 0.65, color="#ffd166")
    n "Antes da reunião, o grupo atravessou a cantina, um dos pontos mais movimentados do campus nos intervalos."
    show alex feliz at entrar_esquerda:
        zoom 0.41
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "Agora entendi por que a cantina é o vértice mais visitado do nosso mapa."
    alex "Com tanta gente conversando, o contato visual ajuda muito. Também podemos escolher uma mesa bem iluminada para usar Libras."
    ane "E finalmente confirmar se a coxinha chegou à reunião antes de nós."
    n "Entre mesas cheias e o movimento dos estudantes, os dois seguiram para conhecer a parte interna do refeitório."
    jump refeitorio_interno

label refeitorio_interno:
    scene bg refeitorio interno:
        size (1920, 1080)
        zoom 1.03
        ease 2.0 zoom 1.0
    with Fade(0.6, 0.15, 0.7, color="#dce7d2")

    n "No interior do refeitório, uma fila avançava junto ao balcão enquanto os estudantes conversavam nas mesas."
    show alex feliz at entrar_esquerda:
        zoom 0.41
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "Aqui tem espaço para almoçar com a turma e recuperar a energia entre uma aula e outra."
    alex "E também para praticar convivência: organizar a fila, deixar a passagem livre e recolher a bandeja depois da refeição."
    ane "Olha aquele aluno de chapéu de palha sentado de costas. Pelo tamanho do prato, ele levou a parte da energia muito a sério."
    n "Antes de saírem, Ane apontou para o salão e propôs uma rápida revisão de vocabulário."

    menu:
        "Qual palavra dá nome ao local onde os estudantes fazem suas refeições?"
        "Refeitório":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            alex "Correto! Este espaço é o refeitório."
            $ renpy.notify("Resposta correta: REFEITÓRIO")
        "Biblioteca":
            $ registrar_resposta(False)
            alex "Biblioteca é o espaço de livros e estudos. Aqui, a palavra correta é REFEITÓRIO."
        "Laboratório":
            $ registrar_resposta(False)
            alex "Laboratório é o espaço de aulas práticas. Aqui, a palavra correta é REFEITÓRIO."

    ane "Vocabulário revisado e almoço localizado. Agora podemos continuar a missão."
    hide ane
    hide alex
    with dissolve
    jump final

label final:
    scene bg sagui:
        size (1920, 1080)
        xalign 0.5
        yalign 0.5
    with dissolve
    n "No caminho do refeitório, um sagui observava o movimento entre as árvores do campus com a serenidade de quem sabe mais do que conta."
    ane "Ele está fiscalizando quem ainda tem saldo para o almoço."
    show alex pensando at entrar_centro
    alex "Espera. Guardanapo na biblioteca, migalha no teclado, caudas listradas em três lugares... Não era UM suspeito."
    hide alex pensando with dissolve
    ane "Alex, por que o mato está fazendo barulho de caixa de papelão?"

    window hide
    show alex surpreso at reacao_extrema_esquerda
    show ane surpresa at reacao_esquerda
    show julia preocupada at reacao_direita
    show saguis coxinhas at saguis_revelacao
    with hpunch
    pause 0.8
    centered "{size=62}{color=#ffd166}PLOT TWIST CROCANTE!{/color}{/size}\n{size=34}A quadrilha dos saguis estava com a caixa inteira!{/size}"
    window auto

    alex "EU SABIA! Quer dizer... eu suspeitava academicamente. Eram vários saguis trabalhando em equipe."
    ane "Cinco saguis, uma caixa e zero autorização da cantina. Isso já é um projeto interdisciplinar."
    julia "O da esquerda está escondendo a prova atrás das costas. Finalmente um mistério com flagrante e farofa."
    $ registrar_pista("Flagrante: cinco saguis com a caixa inteira de coxinhas")

    n "Os saguis não queriam destruir a recepção. Viram uma caixa sem identificação perto de uma janela aberta e decidiram organizar o próprio intervalo."
    alex "Também aprendemos outra coisa: informação importante precisa estar visível e clara. Uma etiqueta fechada dentro da caixa não informa ninguém — especialmente saguis oportunistas."
    ane "Nova regra do campus: identificar o lanche e jamais subestimar uma equipe com cinco caudas."

    hide saguis coxinhas
    hide julia
    hide ane
    hide alex
    with dissolve

    scene bg refeitorio:
        size (1920, 1080)
    with Fade(0.7, 0.2, 1.0, color="#0b2b21")
    n "A caixa foi recuperada e levada ao refeitório. O cartão recarregado permite comprar a refeição, e a reunião apresentou informações sobre o curso."
    show alex feliz at entrar_esquerda:
        zoom 0.43
    show ane feliz at entrar_direita:
        zoom 0.42
    ane "Caso encerrado. Os suspeitos devolveram a caixa em troca de uma retirada estratégica até as árvores."
    $ desbloquear_sinal("COXINHA")
    $ conceder_conquista("Coxinha bilíngue")
    if len(pistas_encontradas) >= 4:
        $ conceder_conquista("Detetive crocante")
    show coxinha premio at coxinha_na_mao
    alex "Mistério resolvido. Eu encontrei a caixa seguindo pistas visuais; agora vamos revisar o sinal de COXINHA antes que a prova desapareça de novo."
    ane "Primeiro o sinal, depois a divisão. Acessibilidade e coxinha ficam melhores quando ninguém é deixado de fora."
    $ renpy.notify("Sinal final aprendido: COXINHA")
    if percentual_acertos() >= 75:
        alex "Nossas escolhas facilitaram a comunicação durante todo o caminho. Investigação aprovada com acessibilidade e uma força-tarefa de cinco saguis."
    else:
        alex "Nem toda escolha funcionou de primeira, mas corrigimos o caminho. Aprender também é perceber o problema, pedir ajuda e tentar novamente."

    hide ane
    hide alex
    hide coxinha premio
    with dissolve
    show coxinha premio at coxinha_comemora
    centered "{size=58}{color=#ffd166}COXINHA ENCONTRADA!{/color}{/size}\n{size=30}Missão crocante concluída{/size}"
    hide coxinha premio with dissolve

    show alex feliz at entrar_centro:
        zoom 0.48
    alex "Hoje eu conheci o campus, pratiquei Libras e salvei o intervalo. Amanhã começam as primeiras aulas da nossa semana."
    if pontos_libras >= 3:
        centered "{size=54}{color=#7fe0aa}EXCELENTE RECEPÇÃO!{/color}{/size}\nVocê praticou comunicação visual em [pontos_libras] momentos."
    else:
        centered "{size=54}{color=#ffd166}MISSÃO CONCLUÍDA!{/color}{/size}\nUse o botão de repetir e continue praticando Libras."
    centered "{size=34}Lugares visitados{/size}\n[join_lista(lugares_visitados)]\n\n{color=#7fe0aa}Fim da segunda-feira{/color}"
    if percentual_acertos() >= 75:
        $ conceder_conquista("Acessibilidade desde o começo")
    call screen relatorio_final
    jump dia_2_programacao

label dia_2_programacao:
    scene bg laboratorio:
        size (1920, 1080)
        zoom 1.04
        ease 2.0 zoom 1.0
    with Fade(0.7, 0.2, 0.7, color="#10251f")
    centered "{size=60}{color=#7fe0aa}TERÇA-FEIRA{/color}{/size}\n{size=34}Fundamentos de Programação{/size}"

    show ane surpresa at retrato_centro
    ane "A lousa já tem fluxogramas. A aula nem começou e as setas parecem saber aonde vão."
    hide ane surpresa with dissolve
    show alex retrato at retrato_centro
    alex "Tomara que elas expliquem o caminho para nós também."
    hide alex retrato with dissolve

    show camila explicando at destaque_professor
    camila "Antes da primeira aula, quero dar as boas-vindas. Eu sou a professora Camila e acompanho os projetos dos estudantes."
    show camila preocupada at retrato_centro
    camila "Não esperem saber tudo na primeira semana. Procurem monitoria, formem grupos e registrem as dúvidas."
    show camila feliz at retrato_centro
    camila "Computação é construída em equipe. Ideias diferentes tornam os projetos mais fortes e acessíveis."
    hide camila feliz with dissolve

    show fabio explicando at destaque_professor
    fabio "Bom dia! Eu sou o professor Fábio e esta é a disciplina de Fundamentos de Programação."
    fabio "Um algoritmo é uma sequência organizada de passos para resolver um problema. Antes da linguagem de programação, precisamos aprender a pensar na solução."
    fabio "Vamos trabalhar com variáveis, entrada e saída, decisões, repetições, funções e testes. Esses conceitos aparecem em quase todas as áreas do curso."
    fabio "Eles serão usados em sistemas, aplicativos, jogos, inteligência artificial, bancos de dados e nos projetos das próximas disciplinas."

    menu:
        "O programa precisa escolher entre aprovado e reprovado. Qual conceito usar?"
        "Uma condição, como se/senão":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            show fabio feliz at retrato_centro
            fabio "Exatamente. A condição permite que o programa tome caminhos diferentes conforme os dados."
        "Um laço infinito":
            $ registrar_resposta(False)
            show fabio surpreso at retrato_centro
            fabio "O laço repete instruções. Para escolher entre dois caminhos, começamos com uma condição."

    hide fabio with dissolve
    show ane rindo at retrato_centro
    ane "Então o caso da coxinha sumida era um algoritmo: procurar, perguntar e repetir até o intervalo."
    hide ane rindo with dissolve
    show alex retrato at retrato_centro
    alex "Com uma condição de parada muito importante: encontrar a coxinha."
    hide alex retrato with dissolve
    centered "{size=38}{color=#7fe0aa}Conceitos do dia{/color}{/size}\nAlgoritmos • variáveis • condições • repetições • funções"
    jump dia_3_calculo

label dia_3_calculo:
    scene bg sala:
        size (1920, 1080)
        xalign 0.5
    with pushleft
    centered "{size=60}{color=#8ed1fc}QUARTA-FEIRA{/color}{/size}\n{size=34}Cálculo I{/size}"

    show edson explicando at destaque_professor
    edson "Olá! Eu sou o professor Edson. Em Cálculo I estudaremos funções, limites, derivadas e, mais adiante, integrais."
    edson "Uma função descreve como uma quantidade depende de outra. O limite ajuda a entender o comportamento quando nos aproximamos de um ponto."
    edson "A derivada mede taxa de mudança: velocidade, crescimento ou inclinação. Na Computação, isso aparece em gráficos, simulações, otimização e aprendizado de máquina."
    edson "O objetivo não é decorar símbolos. É aprender a modelar problemas e interpretar o resultado."

    hide edson with dissolve
    show ane retrato at retrato_centro
    ane "Se a quantidade de exercícios cresce e meu tempo livre diminui, isso já conta como função?"
    hide ane retrato with dissolve
    show alex pensando at retrato_centro
    alex "Conta como uma função assustadoramente realista."
    hide alex pensando with dissolve

    menu:
        "Qual ideia representa melhor uma derivada?"
        "A taxa de mudança de uma quantidade":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            show edson feliz at retrato_centro
            edson "Muito bem. Ela mostra como algo varia naquele instante."
        "Uma lista de passos de um algoritmo":
            $ registrar_resposta(False)
            show edson pensando at retrato_centro
            edson "Isso pertence à programação. Em Cálculo, a derivada está ligada à variação."

    hide edson with dissolve
    show helena explicando at destaque_professor
    helena "Sou a professora Helena. Nas pesquisas do curso, um resultado precisa vir acompanhado de fonte, método e evidência."
    show helena surpresa at retrato_centro
    helena "Copiar uma informação sem verificar a origem pode transformar um erro pequeno em uma conclusão inteira."
    show helena feliz at retrato_centro
    helena "Na biblioteca, vocês aprenderão a buscar artigos, citar autores e apresentar projetos com clareza."
    hide helena with dissolve

    centered "{size=38}{color=#8ed1fc}Conceitos do dia{/color}{/size}\nFunções • limites • derivadas • modelagem"
    jump dia_4_discreta

label dia_4_discreta:
    scene bg sala:
        size (1920, 1080)
        xalign 0.5
        matrixcolor TintMatrix("#fff3d6")
    with Fade(0.5, 0.1, 0.6, color="#5a3218")
    centered "{size=60}{color=#ffd166}QUINTA-FEIRA{/color}{/size}\n{size=34}Matemática Discreta{/size}"

    show cicero explicando at destaque_professor
    cicero "Eu sou o professor Cícero. Matemática Discreta estuda estruturas formadas por elementos separados, muito próximas do funcionamento da Computação."
    cicero "Começaremos com lógica, proposições, conjuntos, relações, funções, técnicas de contagem e grafos."
    cicero "A lógica ajuda a escrever condições corretas. Grafos representam redes, rotas, amizades, dependências e conexões entre computadores."
    cicero "Vocês usarão esse raciocínio em algoritmos, bancos de dados, redes, segurança e análise de problemas."

    hide cicero with dissolve
    show ane surpresa at retrato_centro
    ane "Então um mapa do campus pode virar um grafo?"
    hide ane surpresa with dissolve
    show alex retrato at retrato_centro
    alex "Sim. Os lugares são vértices e os caminhos viram arestas. A cantina provavelmente é o vértice mais visitado."
    hide alex retrato with dissolve

    menu:
        "Em um mapa representado por grafo, o que são os caminhos entre lugares?"
        "Arestas":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            show cicero feliz at retrato_centro
            cicero "Correto. Os lugares podem ser vértices e as ligações entre eles são arestas."
        "Variáveis de texto":
            $ registrar_resposta(False)
            show cicero desconfiado at retrato_centro
            cicero "Variáveis guardam dados. No grafo, usamos arestas para representar as conexões."

    centered "{size=38}{color=#ffd166}Conceitos do dia{/color}{/size}\nLógica • conjuntos • contagem • grafos"
    jump dia_5_circuitos

label dia_5_circuitos:
    scene bg laboratorio:
        size (1920, 1080)
        matrixcolor TintMatrix("#d8f3ef")
    with pushleft
    centered "{size=60}{color=#b8a1ff}SEXTA-FEIRA{/color}{/size}\n{size=34}Circuitos Digitais — Eletrônica Digital{/size}"

    show otavio explicando at destaque_professor
    otavio "Bem-vindos! Eu sou o professor Otávio. Em Circuitos Digitais veremos como informações são representadas eletronicamente."
    otavio "Começamos com os valores binários zero e um, tabelas-verdade e portas lógicas como AND, OR e NOT."
    otavio "Depois combinamos esses blocos para criar somadores, memórias e circuitos capazes de tomar decisões simples."
    otavio "Essa disciplina liga software e hardware. Ela ajuda a entender processadores, sistemas embarcados, robótica e a arquitetura dos computadores."

    hide otavio with dissolve
    show alex surpreso at retrato_centro
    alex "Então, por baixo dos programas, existem milhões de decisões feitas com zero e um."
    hide alex surpreso with dissolve
    show ane rindo at retrato_centro
    ane "E eu levei quatro dias para decidir entre suco e refrigerante. O processador está na frente."
    hide ane rindo with dissolve

    menu:
        "Qual porta inverte um valor lógico?"
        "NOT":
            $ pontos_libras += 1
            $ registrar_resposta(True)
            show otavio feliz at retrato_centro
            otavio "Exato. Se a entrada é um, a saída vira zero; se é zero, vira um."
        "AND":
            $ registrar_resposta(False)
            show otavio surpreso at retrato_centro
            otavio "A AND combina entradas. Quem realiza a inversão é a porta NOT."

    centered "{size=38}{color=#b8a1ff}Conceitos do dia{/color}{/size}\nBinário • portas lógicas • circuitos • hardware"
    jump encerramento_semana

label encerramento_semana:
    scene bg refeitorio:
        size (1920, 1080)
    with Fade(0.7, 0.2, 0.8, color="#10251f")
    show alex feliz at entrar_esquerda:
        zoom 0.41
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "Sobrevivemos à primeira semana: algoritmo, derivada, grafo e porta lógica."
    alex "E aprendemos como cada disciplina se conecta. Programação dá instruções, a matemática modela e prova, e os circuitos executam."
    ane "A coxinha também sobreviveu, mas por pouco."
    alex "Antes de terminar, falta a missão final: reconhecer cinco sinais que apareceram durante nossa jornada."
    ane "Uma prova com vídeo, botão de repetir e nenhuma questão sobre a ficha criminal dos saguis. Podemos começar."
    jump teste_final_libras

label teste_final_libras:
    $ teste_final_acertos = 0
    $ tentativas_teste_final += 1
    window hide
    centered "{size=58}{color=#7fe0aa}TESTE FINAL DE LIBRAS{/color}{/size}\n{size=30}Observe cada vídeo e marque a palavra correta.\nVocê precisa acertar pelo menos 3 de 5.{/size}\n\n{size=21}{color=#ffd166}Os vídeos apresentam sinais isolados para reconhecimento visual.{/color}{/size}"

    $ resposta_teste = renpy.call_screen("quiz_libras", "LIBRAS", "Questão 1 de 5 — Qual palavra corresponde ao sinal?", ["Libras", "Computador", "Coxinha"])
    if resposta_teste == "Libras":
        $ teste_final_acertos += 1

    $ resposta_teste = renpy.call_screen("quiz_libras", "BIBLIOTECA", "Questão 2 de 5 — Qual palavra corresponde ao sinal?", ["Professor", "Biblioteca", "Ajudar"])
    if resposta_teste == "Biblioteca":
        $ teste_final_acertos += 1

    $ resposta_teste = renpy.call_screen("quiz_libras", "COMPUTADOR", "Questão 3 de 5 — Qual palavra corresponde ao sinal?", ["Computador", "Acessibilidade", "Aluno"])
    if resposta_teste == "Computador":
        $ teste_final_acertos += 1

    $ resposta_teste = renpy.call_screen("quiz_libras", "COXINHA", "Questão 4 de 5 — Qual palavra corresponde ao sinal?", ["Cuidado", "Aprender", "Coxinha"])
    if resposta_teste == "Coxinha":
        $ teste_final_acertos += 1

    $ resposta_teste = renpy.call_screen("quiz_libras", "ACESSIBILIDADE", "Questão 5 de 5 — Qual palavra corresponde ao sinal?", ["Entender", "Acessibilidade", "Vezes"])
    if resposta_teste == "Acessibilidade":
        $ teste_final_acertos += 1

    if teste_final_acertos >= 3:
        centered "{size=64}{color=#7fe0aa}APROVADO!{/color}{/size}\n{size=36}Você reconheceu [teste_final_acertos] de 5 sinais.{/size}\n{size=24}Tentativa: [tentativas_teste_final]{/size}"
        $ conceder_conquista("Aprovado em Libras")
        jump acolhimento_final
    else:
        centered "{size=58}{color=#ffd166}VAMOS PRATICAR MAIS UM POUCO{/color}{/size}\n{size=34}Você reconheceu [teste_final_acertos] de 5 sinais.\nSão necessários pelo menos 3 acertos.{/size}"
        scene bg refeitorio:
            size (1920, 1080)
        show ane rindo at entrar_esquerda
        show alex retrato at entrar_direita
        ane "Quase! Até algoritmo entra em repetição quando ainda não chegou à condição de parada."
        alex "Reveja com calma, observe o sinal completo e use o botão de repetir. Errar aqui não encerra a aprendizagem; só indica o próximo passo."
        menu:
            "Preparado para tentar novamente?"
            "Repetir o teste final":
                jump teste_final_libras

label acolhimento_final:
    scene bg entrada:
        size (1920, 1080)
        zoom 1.03
        ease 2.0 zoom 1.0
    with Fade(0.7, 0.2, 0.8, color="#10251f")

    show alex retrato at entrar_esquerda
    alex "Reconhecer cinco sinais é apenas o começo. Libras é uma língua completa, viva e ligada à cultura e à comunidade surda."
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "Aprender exige atenção visual, prática, convivência e coragem para pedir que alguém repita quando for necessário."
    hide alex with dissolve
    show lia aprovando at retrato_centro
    lia "A Ciência da Computação precisa de pessoas diferentes pensando juntas. Acessibilidade não é um detalhe colocado no final: faz parte de um bom projeto desde a primeira ideia."
    lia "Aos calouros de Ciência da Computação do IFCE Campus Maracanaú: sejam bem-vindos. Procurem ajuda, participem, compartilhem conhecimento e construam uma turma em que todas as pessoas possam se comunicar e aprender."
    hide lia with dissolve
    show alex feliz at entrar_esquerda:
        zoom 0.42
    show ane rindo at entrar_direita
    alex "Nos vemos pelos corredores. Se aparecer outro mistério, primeiro buscamos evidências."
    ane "E depois fechamos as janelas. Os saguis já demonstraram domínio avançado de logística."

    if pontos_libras >= 7:
        centered "{size=58}{color=#7fe0aa}SEMANA EXCELENTE!{/color}{/size}\nVocê acertou [pontos_libras] decisões e começou a conectar as disciplinas."
    else:
        centered "{size=58}{color=#ffd166}PRIMEIRA SEMANA CONCLUÍDA!{/color}{/size}\nVocê tomou [pontos_libras] boas decisões. Revise as aulas e tente novamente."
    centered "{size=34}{color=#7fe0aa}CERTIFICADO SIMBÓLICO{/color}{/size}\nRecepção acessível e teste final concluídos!\nResultado: [teste_final_acertos] de 5 sinais reconhecidos.\n\n{size=22}Este certificado celebra a participação no jogo e não substitui formação em Libras.{/size}"
    call screen relatorio_final
    centered "{size=34}A jornada de Alex e Ane continua...{/size}"
    call cena_pos_creditos
    return

label cena_pos_creditos:
    $ _libras_antes_pos_creditos = libras_ativo
    $ libras_ativo = False
    $ parar_libras()
    scene black
    with Fade(0.8, 0.4, 0.8)
    centered "{size=28}{color=#a9b8ad}CENA PÓS-CRÉDITOS{/color}{/size}"
    pause 0.5

    centered "{size=92}{color=#ffd166}11:59{/color}{/size}\n{size=27}Jardineira do meio-dia{/size}"

    scene bg pos creditos ane at corrida_pos_creditos
    with vpunch
    n "Ane descobriu tarde demais que concluir a primeira semana não suspende as leis do transporte estudantil."
    ane "Mmf! MMMMMF!"
    n "Mesmo com a torrada na boca, o recado era bem claro: \"SEGURA A JARDINEIRA!\""

    with hpunch
    centered "{size=64}{color=#ffd166}12:00{/color}{/size}\n{size=31}Continua... se ela conseguir alcançar.{/size}"
    pause 0.8
    scene black with Fade(0.25, 0.15, 0.6)
    $ libras_ativo = _libras_antes_pos_creditos
    return

init python:
    def join_lista(itens):
        return " • ".join(itens)
