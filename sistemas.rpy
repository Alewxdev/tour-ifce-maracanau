## Sistemas de progressão, revisão e exploração.

default sinais_desbloqueados = []
default conquistas = []
default pistas_encontradas = []
default respostas_corretas = 0
default respostas_totais = 0
default repeticoes_libras = 0
default glossario_sinal = "LIBRAS"
default teste_final_acertos = 0
default tentativas_teste_final = 0

init -1 python:
    renpy.music.register_channel(
        "glossario", mixer="voice", loop=False,
        buffer_queue=False, movie=True,
    )

    sinais_caderno = {
        "ACESSIBILIDADE": "Planejar recursos para que todas as pessoas possam participar.",
        "AJUDAR": "Oferecer apoio respeitando a autonomia da pessoa.",
        "ALUNO": "Pessoa que estuda ou participa de uma atividade de aprendizagem.",
        "APRENDER": "Construir conhecimento por observação, prática e interação.",
        "BIBLIOTECA": "Espaço de leitura, pesquisa, estudo e apoio acadêmico.",
        "COMPUTADOR": "Equipamento usado em aulas, projetos e programação.",
        "COXINHA": "O salgado mais investigado do Campus Maracanaú.",
        "CUIDADO": "Atenção a uma situação, pessoa ou procedimento.",
        "ENTENDER": "Compreender uma ideia ou mensagem.",
        "LIBRAS": "Língua Brasileira de Sinais, com gramática e estrutura próprias.",
        "PROFESSOR": "Profissional que orienta processos de aprendizagem.",
        "VEZES": "Repetição ou quantidade de ocorrências; rever sinais ajuda na aprendizagem.",
    }

    locais_mapa = [
        ("Pátio", 0.22, 0.24),
        ("Biblioteca Rachel de Queiroz", 0.48, 0.20),
        ("Sala de estudos da biblioteca", 0.73, 0.25),
        ("Laboratórios de informática", 0.25, 0.49),
        ("Salas de aula", 0.51, 0.48),
        ("Piscina e complexo esportivo", 0.76, 0.50),
        ("Ginásio e quadra poliesportiva", 0.31, 0.72),
        ("Cantina", 0.65, 0.73),
    ]

    descricoes_conquistas = {
        "Mãos à vista": "Escolheu uma comunicação visual respeitosa.",
        "Caçador de bugs": "Corrigiu a condição de parada do programa.",
        "Detetive crocante": "Reuniu todas as pistas da coxinha.",
        "Guia do campus": "Visitou todos os ambientes do passeio.",
        "Coxinha bilíngue": "Encontrou a coxinha e revisou seu sinal.",
        "Memória visual": "Concluiu o desafio de associação de sinais.",
        "Repetir é aprender": "Usou a repetição de vídeos para praticar.",
        "Aprovado em Libras": "Reconheceu pelo menos três dos cinco sinais do teste final.",
        "Acessibilidade desde o começo": "Acertou as principais decisões inclusivas.",
        "Caos na arquibancada": "Encontrou a espectadora de tranças azuis escondida na quadra.",
    }

    def desbloquear_sinal(nome):
        if nome in sinais_caderno and nome not in sinais_desbloqueados:
            sinais_desbloqueados.append(nome)
            renpy.notify("Caderno de Libras: %s desbloqueado" % nome)

    def conceder_conquista(nome):
        if nome not in conquistas:
            conquistas.append(nome)
            renpy.notify("Conquista desbloqueada: %s" % nome)

    def registrar_pista(texto):
        if texto not in pistas_encontradas:
            pistas_encontradas.append(texto)
            renpy.notify("Nova pista: %s" % texto)

    def registrar_resposta(acertou):
        global respostas_corretas, respostas_totais
        respostas_totais += 1
        if acertou:
            respostas_corretas += 1

    def reproduzir_sinal_caderno(nome):
        dados = _indice_sinais.get(_normalizar_libras(nome).strip(), {})
        caminho = dados.get("arquivo")
        if caminho and renpy.loadable(caminho):
            renpy.music.play(caminho, channel="glossario", loop=False)

    def repetir_sinal_caderno(nome):
        global repeticoes_libras
        repeticoes_libras += 1
        reproduzir_sinal_caderno(nome)
        if repeticoes_libras >= 3:
            conceder_conquista("Repetir é aprender")

    def repetir_libras_pedagogico(texto):
        global repeticoes_libras
        repeticoes_libras += 1
        reproduzir_libras(texto)
        if repeticoes_libras >= 3:
            conceder_conquista("Repetir é aprender")

    def percentual_acertos():
        if not respostas_totais:
            return 0
        return int(round(100.0 * respostas_corretas / respostas_totais))

image glossario_player = Movie(
    channel="glossario", size=(640, 360), loop=False, keep_last_frame=True,
)

screen easter_egg_quadra():
    zorder 250
    modal True

    frame:
        xalign 0.5
        ypos 26
        padding (24, 14)
        background Solid("#071c19dc")
        text "Há duas visitantes conhecidas na arquibancada. Encontre a de tranças azuis ou continue." size 25 color "#e9fff8"

    # Jinx ocupa esta região na arte de 1920x1080. A área maior também
    # facilita o toque em telas pequenas e o foco por teclado.
    button:
        xpos 1160
        ypos 535
        xsize 150
        ysize 235
        background Solid("#00000000")
        hover_background Solid("#31dfff38")
        tooltip "Uma espectadora de longas tranças azuis..."
        action Return("jinx")

    textbutton "Continuar a visita":
        xalign 0.5
        yalign 0.94
        padding (28, 14)
        text_size 26
        background Solid("#147a60ee")
        hover_background Solid("#1ca982")
        action Return("continuar")

screen caderno_libras():
    zorder 300
    modal True
    on "hide" action Function(renpy.music.stop, channel="glossario")
    add Solid("#071c19f5")
    frame:
        xalign 0.5 yalign 0.5
        xsize 1720 ysize 930
        padding (35, 28)
        background Solid("#102e28f5")
        hbox:
            spacing 34
            vbox:
                xsize 500 spacing 10
                text "CADERNO DE LIBRAS" size 45 color "#7fe0aa" bold True
                text "[len(sinais_desbloqueados)] de [len(sinais_caderno)] sinais" size 24 color "#ffd166"
                viewport:
                    ysize 710 mousewheel True draggable True scrollbars "vertical"
                    vbox:
                        spacing 8
                        for nome in sorted(sinais_caderno.keys()):
                            if nome in sinais_desbloqueados:
                                textbutton nome:
                                    xsize 430
                                    action [SetVariable("glossario_sinal", nome), Function(reproduzir_sinal_caderno, nome)]
                            else:
                                textbutton "??? — continue jogando":
                                    xsize 430 sensitive False
            vbox:
                xsize 1080 spacing 18
                text glossario_sinal size 48 color "#ffd166" bold True xalign 0.5
                frame:
                    xalign 0.5 xsize 660 ysize 380 padding (10, 10)
                    background Solid("#173f36")
                    add "glossario_player" xalign 0.5 yalign 0.5
                text sinais_caderno.get(glossario_sinal, "Escolha um sinal desbloqueado."):
                    size 28 xalign 0.5 text_align 0.5 xmaximum 980
                text "Observe mãos, movimento, localização, orientação e expressões não manuais.":
                    size 23 color "#cce9df" xalign 0.5 text_align 0.5
                hbox:
                    xalign 0.5 spacing 20
                    textbutton "Reproduzir":
                        action Function(reproduzir_sinal_caderno, glossario_sinal)
                    textbutton "Repetir e praticar":
                        action Function(repetir_sinal_caderno, glossario_sinal)
                text "Sinais isolados para apoio educativo; não são tradução automática de frases.":
                    size 20 color "#ffd166" xalign 0.5
        textbutton "Fechar":
            xalign 0.98 yalign 0.98 action Hide("caderno_libras")

screen mapa_campus():
    zorder 300
    modal True
    add Transform("campus/anime_frente_ifce.png", xysize=(1920, 1080), fit="cover")
    add Solid("#061a17b8")
    text "MAPA DA RECEPÇÃO" xalign 0.5 ypos 45 size 52 color "#7fe0aa" bold True
    text "Áreas visitadas aparecem em verde" xalign 0.5 ypos 110 size 25
    for nome, px, py in locais_mapa:
        button:
            xpos px ypos py anchor (0.5, 0.5)
            xsize 350 yminimum 90 padding (14, 10)
            background Solid("#148a69ed" if nome in lugares_visitados else "#263b38e8")
            hover_background Solid("#1bb98bea" if nome in lugares_visitados else "#344e49e8")
            action Notify(("Local visitado: " if nome in lugares_visitados else "Ainda bloqueado: ") + nome)
            vbox:
                xalign 0.5
                text ("✓ " + nome if nome in lugares_visitados else "🔒 " + nome):
                    size 22 text_align 0.5 xalign 0.5
                if nome in lugares_visitados:
                    text "Visitado" size 18 color "#ffd166" xalign 0.5
    textbutton "Fechar" xalign 0.96 yalign 0.94 action Hide("mapa_campus")

screen painel_conquistas():
    zorder 300
    modal True
    add Solid("#071c19f7")
    frame:
        xalign 0.5 yalign 0.5 xsize 1450 ysize 900 padding (45, 35)
        background Solid("#102e28")
        vbox:
            spacing 18
            text "CONQUISTAS" size 50 color "#ffd166" bold True xalign 0.5
            text "[len(conquistas)] de [len(descricoes_conquistas)] desbloqueadas" size 25 xalign 0.5
            for nome, descricao in descricoes_conquistas.items():
                frame:
                    xfill True yminimum 82 padding (18, 12)
                    background Solid("#147a60" if nome in conquistas else "#253c37")
                    hbox:
                        spacing 20
                        text ("★" if nome in conquistas else "☆") size 40 color "#ffd166"
                        vbox:
                            text nome size 28 bold True
                            text (descricao if nome in conquistas else "Continue explorando para descobrir.") size 20 color "#d6e9e3"
        textbutton "Fechar" xalign 0.98 yalign 0.98 action Hide("painel_conquistas")

screen quiz_libras(sinal, pergunta, opcoes):
    zorder 300
    modal True
    on "hide" action Function(renpy.music.stop, channel="glossario")
    on "show" action Function(reproduzir_sinal_caderno, sinal)
    add Solid("#061b19f5")
    frame:
        xalign 0.5 yalign 0.5 xsize 1300 ysize 900 padding (35, 30)
        background Solid("#10342c")
        vbox:
            spacing 18 xalign 0.5
            text "DESAFIO VISUAL" size 46 color "#7fe0aa" bold True xalign 0.5
            text pergunta size 28 xalign 0.5 text_align 0.5
            frame:
                xsize 660 ysize 380 xalign 0.5 padding (10, 10)
                background Solid("#173f36")
                add "glossario_player" xalign 0.5 yalign 0.5
            textbutton "Repetir vídeo" xalign 0.5 action Function(repetir_sinal_caderno, sinal)
            for opcao in opcoes:
                textbutton opcao:
                    xsize 850 xalign 0.5
                    action Return(opcao)

screen relatorio_final():
    zorder 250
    modal True
    add Solid("#071c19f7")
    frame:
        xalign 0.5 yalign 0.5 xsize 1500 ysize 900 padding (45, 34)
        background Solid("#10342c")
        vbox:
            spacing 20
            text "RELATÓRIO DA RECEPÇÃO" size 50 color "#7fe0aa" bold True xalign 0.5
            text "Decisões corretas: [respostas_corretas] de [respostas_totais] — [percentual_acertos()]%" size 28
            bar value StaticValue(respostas_corretas, max(1, respostas_totais)) xmaximum 1300
            text "Locais visitados: [len(lugares_visitados)] de [len(locais_mapa)]" size 28
            text "Sinais no caderno: [len(sinais_desbloqueados)] de [len(sinais_caderno)]" size 28
            text "Pistas reunidas: [len(pistas_encontradas)]" size 28
            text "Conquistas: [len(conquistas)] de [len(descricoes_conquistas)]" size 28
            if tentativas_teste_final > 0:
                text "Teste final: [teste_final_acertos] de 5 — [tentativas_teste_final] tentativa(s)" size 28 color "#ffd166"
            frame:
                xfill True padding (22, 16) background Solid("#173f36")
                text ("Excelente leitura visual! Continue praticando com a comunidade surda." if percentual_acertos() >= 75 else "Boa jornada! Use o Caderno de Libras para rever os vídeos e tente novamente."):
                    size 26 text_align 0.5 xalign 0.5
            text "Conteúdo introdutório pendente de validação pedagógica final por pessoa surda fluente em Libras.":
                size 21 color "#ffd166" xalign 0.5 text_align 0.5
            hbox:
                xalign 0.5 spacing 25
                textbutton "Revisar Libras" action Show("caderno_libras")
                textbutton "Ver mapa" action Show("mapa_campus")
                textbutton "Conquistas" action Show("painel_conquistas")
                textbutton "Recomeçar" action Jump("start")
                textbutton "Continuar" action Return()
