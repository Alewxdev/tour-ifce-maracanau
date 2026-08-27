## Camada de acessibilidade em Libras.
##
## Os vídeos devem conter a tradução da FRASE completa, revisada por uma
## pessoa fluente em Libras. Não divida o português palavra por palavra.

default libras_ativo = True

init -1 python:
    import threading
    import json
    import os
    import re
    import ssl
    import time
    import unicodedata
    import urllib.parse
    import urllib.request

    # O Ren'Py usa o sistema de áudio também para decodificar vídeos, mas o
    # canal precisa ser registrado explicitamente como canal de filme.
    renpy.music.register_channel(
        "libras",
        mixer="voice",
        loop=False,
        buffer_queue=False,
        movie=True,
    )

    VLIBRAS_TRADUTOR = "https://traducao2.vlibras.gov.br/translate"
    # Traduções que o serviço oficial já retornou. Este cache garante que
    # essas falas funcionem também durante apresentações sem internet.
    libras_glosas = {
        "Achei! Escrevi 'media' de duas formas diferentes.": "ACHAR&PENSAR [EXCLAMAÇÃO] ESCREVER&PAPEL MEDIR 2 FORMA DIFERENTE [PONTO]",
        "Ane terminou o primeiro programa dela.": "ANE TERMINAR PRIMEIRO&ORDINAL PROGRAMA&PROJETO DELE [PONTO]",
        "Aqui fica a biblioteca. É silenciosa, tem ar-condicionado e salva muita gente na semana de provas.": "AQUI BIBLIOTECA [PONTO] SILENCIOSO CONDICIONADO SALVAR&RESGATAR VÁRIOS GENTE SEMANA PROVA&EVIDÊNCIA [PONTO]",
        "Boa escolha. O passeio fica para o intervalo.": "BOA ESCOLHA [PONTO] PASSEAR INTERVALO [PONTO]",
        "Cuidado. Daqui a pouco ele começa a cobrar monitoria em coxinhas.": "CUIDADO [PONTO] AQUI POUCO ELE COMEÇAR COBRAR MONITORIA COXINHA [PONTO]",
        "Deu erro. A segunda regra já está sendo testada.": "ERRAR [PONTO] REGRA JÁ TESTAR [PONTO]",
        "Então a pessoa pode acompanhar a legenda e também assistir à tradução de cada fala?": "PESSOA PODER&POSSIBILIDADE ACOMPANHAR LEGENDA TAMBÉM ASSISTIR&TV TRADUÇÃO&AÇÃO CADA FALAR [INTERROGAÇÃO]",
        "Então temos um motivo de verdade para comemorar.": "TER MOTIVO VERDADE COMEMORAR [PONTO]",
        "Exatamente. A tecnologia ajuda a exibir os sinais, mas as traduções precisam ser revisadas por alguém fluente.": "EXATAMENTE [PONTO] TECNOLOGIA 1S_AJUDAR_2S EXIBIR SINAL&VESTÍGIO TRADUÇÃO&AÇÃO PRECISAR REVISAR ALGUÉM FLUENTE [PONTO]",
        "Falando sério, estamos montando uma equipe para a mostra de projetos do campus.": "FALAR SÉRIO MONTAR&ORGANIZAR EQUIPE 1S_MOSTRAR_2S PROJETO&DOCUMENTO CAMPUS [PONTO]",
        "Funcionou!": "FUNCIONAR [EXCLAMAÇÃO]",
        "Ler a mensagem de erro antes de entrar em pânico.": "LER MENSAGEM ERRO ANTES&ANTERIOR ENTRAR&DENTRO PÂNICO [PONTO]",
        "Melhor irmos direto ao laboratório. Não quero perder a primeira aula.": "MELHOR DIRETO LABORATÓRIO [PONTO] NÃO_QUERER PERDER PRIMEIRO&ORDINAL AULA [PONTO]",
        "O exercício pede um programa que organize as notas dos alunos. Parece simples... eu acho.": "EXERCÍCIO&ATIVIDADE 1S_PEDIR_2S PROGRAMA&PROJETO ORGANIZAR NOTA&AVALIAR ALUNO [PONTO] PARECER&APARÊNCIA SIMPLES&FÁCIL [PONTO] ACHAR&PENSAR [PONTO]",
        "Parabéns, você conheceu o bug mais comum da humanidade: digitar com pressa.": "PARABÉNS VOCÊ CONHECER BUG COMUM HUMANIDADE DIGITAR PRESSA [PONTO]",
        "Parece que vocês precisam mesmo de ajuda.": "PARECER&APARÊNCIA VOCÊS PRECISAR 1S_AJUDAR_2S [PONTO]",
        "Primeira reunião amanhã. Eu levo os salgados científicos.": "PRIMEIRO&ORDINAL REUNIÃO AMANHÃ [PONTO] EU LEVAR SALGADO CIENTÍFICO [PONTO]",
        "Um jogo educativo sobre a vida universitária, com acessibilidade em Libras.": "JOGO EDUCATIVO SOBRE&ASSUNTO VIDA UNIVERSITÁRIO ACESSIBILIDADE LIBRAS [PONTO]",
        "Uma aula, um programa funcionando e uma equipe nova... Nada mal para o primeiro dia.": "AULA PROGRAMA&PROJETO FUNCIONAR EQUIPE NOVO&RECENTE [PONTO] NADA MAL PRIMEIRO&ORDINAL DIA [PONTO]",
        "Você parece estar procurando alguma coisa. Posso ajudar?": "VOCÊ PARECER PROCURAR ALGUMA COISA [PONTO] PODER&POSSIBILIDADE 1S_AJUDAR_2S [INTERROGAÇÃO]",
        "É assim que todo projeto começa. Bem-vinda à equipe!": "TODO PROJETO&DOCUMENTO COMEÇAR [PONTO] BEM_VINDO EQUIPE [EXCLAMAÇÃO]",
        "Ótimo conselho para o meu primeiro dia.": "ÓTIMO CONSELHO&GRUPO MEU PRIMEIRO&ORDINAL DIA [PONTO]",
    }
    libras_pendentes = set()
    libras_erros = {}

    # Associe cada fala ao vídeo revisado correspondente.
    # Exemplo:
    # libras_videos["Você parece estar procurando alguma coisa. Posso ajudar?"] = \
    #     "videos/libras/alex_posso_ajudar.webm"
    libras_videos = {}

    try:
        with renpy.file("videos/libras/sinais/manifesto.json") as arquivo_manifesto:
            manifesto_sinais = json.load(arquivo_manifesto).get("sinais", {})
    except Exception:
        manifesto_sinais = {}

    def _sem_acento_libras(texto):
        return "".join(
            c for c in unicodedata.normalize("NFD", texto)
            if unicodedata.category(c) != "Mn"
        ).upper()

    def _token_sinal_libras(token):
        token = re.sub(r"\[[^]]+\]", "", token).strip()
        token = token.split("&", 1)[0]
        token = re.sub(r"^[123][SP]_", "", token)
        token = re.sub(r"_[123][SP]$", "", token)
        return token.replace("_", " ").strip(" .,!?;:")

    def videos_sinais_libras(what):
        """Monta a sequência dos sinais isolados disponíveis para a glosa."""
        glosa = libras_glosas.get(what, "")
        caminhos = []
        for bruto in glosa.split():
            token = _token_sinal_libras(bruto)
            alvo = _sem_acento_libras(token)
            item = next(
                (
                    dados for nome, dados in manifesto_sinais.items()
                    if _sem_acento_libras(nome) == alvo
                ),
                None,
            )
            caminho = item.get("arquivo") if item else None
            if caminho and renpy.loadable(caminho):
                caminhos.append(caminho)
        return caminhos

    def video_libras(what):
        """Retorna apenas vídeos cadastrados e presentes no jogo."""
        caminho = libras_videos.get(what)
        if caminho and renpy.loadable(caminho):
            return caminho
        return None

    def reproduzir_libras(what):
        """Reproduz ou repete a tradução da fala atual."""
        caminho = video_libras(what)
        if caminho:
            renpy.music.play(caminho, channel="libras", loop=False)
            return

        sinais = videos_sinais_libras(what)
        if sinais:
            renpy.music.play(sinais, channel="libras", loop=False)

    def parar_libras():
        renpy.music.stop(channel="libras")

    def _finalizar_traducao_libras(texto, glosa=None, erro=None):
        libras_pendentes.discard(texto)
        if glosa:
            libras_glosas[texto] = glosa
            libras_erros.pop(texto, None)
            if renpy.store.libras_ativo:
                reproduzir_libras(texto)
        elif erro:
            libras_erros[texto] = erro
        renpy.restart_interaction()

    def _consultar_vlibras(texto):
        """Consulta a API sem bloquear a interface do Ren'Py."""
        try:
            certificado = os.path.join(config.gamedir, "certs", "cacert.pem")
            contexto_ssl = ssl.create_default_context(cafile=certificado)
            dados = urllib.parse.urlencode({"text": texto}).encode("utf-8")
            requisicao = urllib.request.Request(
                VLIBRAS_TRADUTOR,
                data=dados,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "IFCE-Jogo-Libras/1.0",
                },
                method="POST",
            )
            glosa = None
            ultimo_erro = None
            for tentativa in range(3):
                try:
                    with urllib.request.urlopen(
                        requisicao, timeout=12, context=contexto_ssl
                    ) as resposta:
                        glosa = resposta.read().decode("utf-8").strip()
                    if glosa:
                        break
                except Exception as erro:
                    ultimo_erro = erro
                    if tentativa < 2:
                        time.sleep(1.0 + tentativa)

            if not glosa:
                raise ultimo_erro or RuntimeError("Resposta vazia do VLibras")

            renpy.invoke_in_main_thread(
                _finalizar_traducao_libras, texto, glosa, None
            )
        except Exception:
            renpy.invoke_in_main_thread(
                _finalizar_traducao_libras,
                texto,
                None,
                "Modo offline ativo: glosa não recebida. A fala completa está exibida acima.",
            )

    def solicitar_traducao_libras(texto):
        """Obtém uma glosa uma única vez e mantém o resultado em memória."""
        if not texto or texto in libras_glosas or texto in libras_pendentes:
            return

        libras_erros.pop(texto, None)
        libras_pendentes.add(texto)
        tarefa = threading.Thread(target=_consultar_vlibras, args=(texto,))
        tarefa.daemon = True
        tarefa.start()

    def estado_traducao_libras(texto):
        if texto in libras_glosas:
            return libras_glosas[texto]
        if texto in libras_erros:
            return libras_erros[texto]
        return "Traduzindo pela API pública do VLibras..."

image libras_player = Movie(
    channel="libras",
    size=(400, 225),
    loop=False,
    keep_last_frame=True,
)

screen painel_libras(what):
    zorder 100

    if not renpy.variant("small"):
        textbutton ("Libras: ON" if libras_ativo else "Libras: OFF"):
            xalign 0.985
            yalign 0.015
            action [ToggleVariable("libras_ativo"), Function(parar_libras)]

        if libras_ativo:
            on "show" action [
                Function(solicitar_traducao_libras, what),
                Function(reproduzir_libras, what),
            ]

            frame:
                xalign 0.985
                yalign 0.075
                xsize 440
                ysize 620
                padding (18, 14)
                background Solid("#10251fee")

                vbox:
                    spacing 9

                    text "TRADUÇÃO EM LIBRAS":
                        color "#7fe0aa"
                        size 25
                        bold True
                        xalign 0.5

                    text "FALA ATUAL":
                        color "#7fe0aa"
                        size 17
                        bold True

                    text what:
                        color "#ffffff"
                        size 18
                        xmaximum 400

                    text "GLOSA GERADA PELO VLIBRAS":
                        color "#7fe0aa"
                        size 17
                        bold True

                    text estado_traducao_libras(what):
                        substitute False
                        color ("#ffd166" if what in libras_erros else "#ffffff")
                        size 19
                        xmaximum 400

                    if what in libras_erros:
                        textbutton "Tentar tradução novamente":
                            xalign 0.5
                            action Function(solicitar_traducao_libras, what)

                    if video_libras(what) or videos_sinais_libras(what):
                        frame:
                            xsize 400
                            ysize 225
                            xalign 0.5
                            padding (0, 0)
                            background Solid("#183b31")

                            add "libras_player"

                        hbox:
                            spacing 12
                            xalign 0.5
                            textbutton "Reproduzir / repetir sinais":
                                action Function(reproduzir_libras, what)
                            textbutton "Parar":
                                action Function(parar_libras)
                    else:
                        frame:
                            xfill True
                            ysize 150
                            background Solid("#183b31")

                            vbox:
                                xalign 0.5
                                yalign 0.5
                                spacing 10

                                text "LIBRAS":
                                    size 40
                                    bold True
                                    color "#ffffff"
                                    xalign 0.5
                                text "Não há sinal isolado\npara esta fala no acervo":
                                    size 21
                                    color "#d8efe3"
                                    text_align 0.5
                                    xalign 0.5

                    text "Sinais isolados do Signbank/UFSC — não substituem intérprete.":
                        size 15
                        color "#d8efe3"
                        xalign 0.5

    else:
        textbutton ("Libras ON" if libras_ativo else "Libras OFF"):
            xalign 0.98
            yalign 0.02
            action [ToggleVariable("libras_ativo"), Function(parar_libras)]
