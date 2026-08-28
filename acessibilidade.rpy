## Painel educacional de Libras — funciona integralmente offline.
## O acervo contém sinais isolados, portanto o painel os apresenta como
## vocabulário de apoio, nunca como tradução automática palavra por palavra.

default libras_ativo = True

init -1 python:
    import json
    import re
    import unicodedata

    renpy.music.register_channel(
        "libras", mixer="voice", loop=False,
        buffer_queue=False, movie=True,
    )

    try:
        with renpy.file("videos/libras/sinais/manifesto.json") as arquivo:
            manifesto_sinais = json.load(arquivo).get("sinais", {})
    except Exception:
        manifesto_sinais = {}

    def _normalizar_libras(texto):
        texto = "".join(
            c for c in unicodedata.normalize("NFD", texto)
            if unicodedata.category(c) != "Mn"
        )
        return re.sub(r"[^A-Z0-9 ]", " ", texto.upper())

    _indice_sinais = {
        _normalizar_libras(nome).strip(): dados
        for nome, dados in manifesto_sinais.items()
    }

    # Glosas pedagógicas revisáveis. Todas usam somente vídeos presentes no
    # manifesto local. A ordem segue uma aproximação visual de sinais-chave.
    libras_glosas = {
        "Campus novo, pessoas novas e muitos corredores. Vamos começar.": "NOVO PESSOA NOVO VAMOS COMEÇAR",
        "Oi! Eu sou Ane. Estou aprendendo Libras e posso acompanhar você no passeio.": "APRENDER LIBRAS PODER ACOMPANHAR VOCÊ PASSEAR",
        "Ótimo. Só uma regra: fale de frente para mim e não esconda as mãos.": "ÓTIMO REGRA FALAR PARA MEU NÃO",
        "Combinado. Se eu errar um sinal, você pode me ajudar.": "ERRAR SINAL VOCÊ PODER AJUDAR",
        "Certo! Agora eu posso ver você antes da conversa começar.": "AGORA PODER VOCÊ ANTES COMEÇAR",
        "Isso não funciona. Melhor entrar no campo de visão de Alex.": "NÃO FUNCIONAR MELHOR ENTRAR ALEX",
        "Agora sim. Comunicação também começa com respeito.": "AGORA TAMBÉM COMEÇAR",
        "A reunião dos calouros sem coxinha? Isso já virou emergência acadêmica.": "REUNIÃO ALUNO COXINHA ACADÊMICA",
        "Vamos procurar. Assim conhecemos o campus e salvamos o intervalo.": "VAMOS PROCURAR ASSIM CONHECER SALVAR INTERVALO",
        "Bem-vindas! Eu sou Davi, monitor da biblioteca e estudante de Ciência da Computação.": "BEM Davi BIBLIOTECA ALUNO CIÊNCIA COMPUTADOR",
        "Davi, você viu uma coxinha muito importante passar por aqui?": "Davi VOCÊ COXINHA MUITO AQUI",
        "Vi uma caixa passeando para o lado da biblioteca. Parecia um projeto com fome.": "PASSEAR PARA LADO BIBLIOTECA PARECER PROJETO",
        "Antes de seguir, ensine aos calouros um sinal útil.": "ANTES ALUNO SINAL",
        "Este é o sinal de BIBLIOTECA. Veja o vídeo e depois tente fazer.": "SINAL BIBLIOTECA VÍDEO DEPOIS TENTAR FAZER",
        "Perfeito. Aprender Libras precisa de atenção, prática e repetição.": "APRENDER LIBRAS PRECISAR VEZES",
        "Pode pedir para repetir. Ninguém precisa disfarçar uma dúvida.": "PODER PEDIR VEZES NENHUM PRECISAR DISFARÇAR",
        "Vamos à Biblioteca Rachel de Queiroz. Lá temos livros, estudo e jogos.": "VAMOS BIBLIOTECA LER APRENDER",
        "Aqui também existe uma regra difícil: devolver o livro e não levar a coxinha para a estante.": "AQUI TAMBÉM REGRA LER NÃO LEVAR COXINHA",
        "Encontrei uma pista: uma nota dizendo LABORATÓRIO CINCO.": "ENCONTRAR NOTA CINCO",
        "O mistério sabe escrever, mas ainda precisa melhorar a letra.": "HISTÓRIA ESCREVER MAS AINDA PRECISAR MELHOR",
        "Para estudar aqui, você pode LER e usar o COMPUTADOR.": "PARA AQUI VOCÊ PODER LER COMPUTADOR",
        "Olá! Eu sou a professora Lia. Bem-vindos à Ciência da Computação do IFCE Maracanaú.": "PROFESSOR Lia BEM CIÊNCIA COMPUTADOR",
        "Professora, procuramos uma coxinha desaparecida. A investigação agora também é computacional.": "PROFESSOR PROCURAR COXINHA AGORA TAMBÉM COMPUTADOR",
        "Nossa hipótese aponta para este laboratório e para um computador com uma mensagem aberta.": "PENSAR PARA COMPUTADOR MENSAGEM",
        "A caixa esteve aqui, mas seguiu para a sala. Antes disso, temos uma missão de Computação e Libras.": "ESTAR AQUI MAS PARA ANTES COMPUTADOR LIBRAS",
        "Encontramos um bug com fome infinita. Isso é sofisticado ou preocupante?": "ENCONTRAR ERRAR COMPUTADOR",
        "Na Computação, chamamos isso de laço infinito. Na cantina, chamamos de terça-feira.": "COMPUTADOR PROGRAMA SEMPRE",
        "Certo. Um algoritmo precisa saber quando continuar e quando parar.": "PROGRAMA PRECISAR PARA PARADA",
        "Criativo, mas não resolve o programa. Vamos ler a mensagem e revisar o código.": "IDEIA MAS NÃO PROGRAMA VAMOS LER MENSAGEM REVISAR",
        "Programar é organizar ideias, testar, errar, revisar e tentar outra vez.": "PROGRAMA ORGANIZAR IDEIA TENTAR ERRAR REVISAR VEZES",
        "Exatamente. Expressões do rosto e movimentos das mãos fazem parte da língua.": "VERDADE PARTE LIBRAS",
        "Computador no escuro parece cinema, mas impede a comunicação visual.": "COMPUTADOR PARECER MAS NÃO",
        "Vamos manter a luz e as mãos visíveis.": "VAMOS CLARO",
        "Libras é uma língua completa, com estrutura própria. Não é português feito palavra por palavra.": "LIBRAS ESTRUTURA NÃO FAZER PALAVRA PARA PALAVRA",
        "Os vídeos deste jogo mostram sinais isolados para apoiar o aprendizado. Uma tradução deve ser revisada por pessoa fluente.": "VÍDEO MOSTRAR SINAL PARA AJUDAR APRENDER TRADUÇÃO REVISAR PESSOA FLUENTE",
        "Software acessível começa no planejamento. Legenda, Libras e interface visual não devem ficar para depois.": "PROGRAMA ACESSIBILIDADE COMEÇAR IDEIA LEGENDA LIBRAS NÃO PARA DEPOIS",
        "A caixa está aqui! O mistério acabou antes da prova.": "ESTAR AQUI HISTÓRIA ANTES PROVA",
        "Mas ela está vazia. Temos agora o mistério da coxinha invisível.": "MAS ESTAR NADA AGORA HISTÓRIA COXINHA",
        "Vejam a mensagem: A COXINHA ESTÁ NA REUNIÃO. A caixa era somente a pista.": "MENSAGEM COXINHA ESTAR REUNIÃO",
        "Parabéns. O passeio era a primeira atividade de recepção dos calouros.": "BOM PASSEAR PRIMEIRO ALUNO",
        "Vocês conheceram o pátio, a biblioteca, os laboratórios e as salas. Também resolveram o primeiro bug do curso.": "VOCÊS CONHECER BIBLIOTECA TAMBÉM PRIMEIRO ERRAR",
        "Então ninguém roubou a coxinha?": "ENTÃO NENHUM COXINHA",
        "Ainda não. Mas a reunião vai começar, então precisamos ir rápido.": "AINDA NÃO MAS REUNIÃO COMEÇAR ENTÃO PRECISAR",
        "BIBLIOTECA. Um lugar para ler, estudar e encontrar ajuda.": "BIBLIOTECA PARA LER APRENDER ENCONTRAR AJUDAR",
        "COMPUTADOR. Nosso colega de projetos e fornecedor oficial de mensagens de erro.": "COMPUTADOR PROJETO MENSAGEM ERRAR",
        "ACESSIBILIDADE. Ela deve estar presente desde o começo de cada projeto.": "ACESSIBILIDADE ESTAR COMEÇAR CADA PROJETO",
        "Hoje eu conheci o campus. Amanhã começamos nosso primeiro projeto de Computação acessível.": "DIA CONHECER AMANHÃ COMEÇAR PRIMEIRO PROJETO COMPUTADOR ACESSIBILIDADE",
    }

    def _tokens_glosa(texto):
        glosa = libras_glosas.get(texto)
        if glosa:
            candidatos = _normalizar_libras(glosa).split()
        else:
            # Cobertura offline para narração: mostra apenas palavras que
            # possuem sinal cadastrado; nunca inventa um vídeo inexistente.
            candidatos = _normalizar_libras(texto).split()
        vistos = set()
        resultado = []
        for token in candidatos:
            if token in _indice_sinais and token not in vistos:
                resultado.append(token)
                vistos.add(token)
        return resultado or ["LIBRAS"]

    def glosa_exibida_libras(texto):
        return " • ".join(_tokens_glosa(texto))

    def videos_sinais_libras(texto):
        caminhos = []
        for token in _tokens_glosa(texto):
            dados = _indice_sinais.get(token, {})
            caminho = dados.get("arquivo")
            if caminho and renpy.loadable(caminho):
                caminhos.append(caminho)
        return caminhos

    def reproduzir_libras(texto):
        caminhos = videos_sinais_libras(texto)
        if caminhos:
            renpy.music.play(caminhos, channel="libras", loop=False)

    def parar_libras():
        renpy.music.stop(channel="libras")

image libras_player = Movie(
    channel="libras", size=(400, 225), loop=False, keep_last_frame=True,
)

screen painel_libras(what):
    zorder 100
    if not renpy.variant("small"):
        textbutton ("Libras: ON" if libras_ativo else "Libras: OFF"):
            xalign 0.985 yalign 0.015
            action [ToggleVariable("libras_ativo"), Function(parar_libras)]

        if libras_ativo:
            on "show" action Function(reproduzir_libras, what)
            frame:
                xalign 0.985 yalign 0.075
                xsize 440 ysize 590
                padding (18, 14)
                background Solid("#10251fee")
                vbox:
                    spacing 9
                    text "APRENDA LIBRAS":
                        color "#7fe0aa" size 25 bold True xalign 0.5
                    text "SINAIS-CHAVE DESTA FALA":
                        color "#7fe0aa" size 17 bold True
                    text glosa_exibida_libras(what):
                        substitute False color "#ffffff" size 20
                        xmaximum 400
                    frame:
                        xsize 400 ysize 225 xalign 0.5
                        padding (0, 0) background Solid("#183b31")
                        add "libras_player"
                    hbox:
                        spacing 12 xalign 0.5
                        textbutton "Repetir sinais":
                            action Function(reproduzir_libras, what)
                        textbutton "Parar":
                            action Function(parar_libras)
                    text "Vídeos WebM locais — funciona sem internet.":
                        size 16 color "#d8efe3" xalign 0.5
                    text "Sinais isolados do Signbank/UFSC. Apoio educativo; não substitui tradução revisada ou intérprete.":
                        size 15 color "#ffd166" xalign 0.5
                        text_align 0.5 xmaximum 400
    else:
        textbutton ("Libras ON" if libras_ativo else "Libras OFF"):
            xalign 0.98 yalign 0.02
            action [ToggleVariable("libras_ativo"), Function(parar_libras)]
