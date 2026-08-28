## Sinais do Maracanaú — recepção acessível aos calouros.

define alex = Character("Alex", color="#ff9fbd")
define ane = Character("Ane", color="#ffd166")
define lia = Character("Professora Lia", color="#7fe0aa")
define davi = Character("Davi", color="#8ed1fc")
define fabio = Character("Professor Fábio", color="#7fe0aa")
define edson = Character("Professor Edson", color="#8ed1fc")
define cicero = Character("Professor Cícero", color="#ffd166")
define otavio = Character("Professor Otávio", color="#b8a1ff")
define n = Character(None)

image bg entrada = Transform("campus/anime_frente_ifce.png", xysize=(1920, 1080), fit="cover")
image bg patio = Transform("campus/anime_corredor.png", xysize=(1920, 1080), fit="cover")
image bg laboratorio = Transform("campus/anime_sala_aula.png", xysize=(1920, 1080), fit="cover")
image bg biblioteca = Transform("campus/anime_biblioteca.png", xysize=(1920, 1080), fit="cover")
image bg biblioteca frente = Transform("campus/anime_frente_biblioteca.png", xysize=(1920, 1080), fit="cover")
image bg sala = Transform("campus/anime_sala_aula.png", xysize=(1920, 1080), fit="cover")
image bg cantina real = Transform("campus/anime_cantina.png", xysize=(1920, 1080), fit="cover")
image bg catraca = Transform("campus/anime_catraca_acesso.png", xysize=(1920, 1080), fit="cover")
image bg sagui = Transform("campus/anime_sagui_refeitorio.png", xysize=(1920, 1080), fit="cover")
image bg refeitorio = Transform("campus/anime_refeitorio.png", xysize=(1920, 1080), fit="cover")
image alex feliz = "personagens/alex_anime_v3_tatuagem.png"
image ane feliz = "Ane.png"
image lia feliz = "personagens/professora_lia.png"
image davi feliz = "personagens/davi.png"
image fabio aula = "personagens/professor_fabio.png"
image edson aula = "personagens/professor_edson.png"
image cicero aula = "personagens/professor_cicero.png"
image otavio aula = "personagens/professor_otavio.png"

default pontos_libras = 0
default lugares_visitados = []

transform entrar_esquerda:
    xalign -0.25 yalign 1.0 alpha 0.0
    easeout 0.55 xalign 0.12 alpha 1.0

transform entrar_centro:
    xalign 0.42 yalign 1.0 alpha 0.0 zoom 0.92
    easeout_back 0.55 alpha 1.0 zoom 1.0

transform entrar_direita:
    xalign 0.88 yalign 1.0 alpha 0.0
    easeout 0.55 xalign 0.68 alpha 1.0

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

transform destaque_professor:
    xalign 0.72 yalign 0.96 alpha 0.0 zoom 0.46
    easeout_back 0.55 alpha 1.0 zoom 0.50

label start:
    $ pontos_libras = 0
    $ lugares_visitados = []
    scene bg entrada:
        size (1920, 1080)
        zoom 1.04
        linear 5.0 zoom 1.0
    with Fade(0.7, 0.2, 0.8, color="#0b2b21")

    centered "{size=64}{color=#7fe0aa}SINAIS DO MARACANAÚ{/color}{/size}\n{size=32}Uma recepção aos calouros do IFCE{/size}"
    n "No primeiro dia, Alex chegou ao IFCE Campus Maracanaú com uma missão: conhecer o campus e não perder a reunião dos calouros."
    n "Alex é surda, sua primeira língua é Libras e ela percebe o mundo principalmente com os olhos."

    show alex feliz at entrar_esquerda:
        zoom 0.48
    alex "Campus novo, pessoas novas e muitos corredores. Vamos começar."
    show ane feliz at entrar_direita:
        zoom 0.46
    ane "Oi! Eu sou Ane. Estou aprendendo Libras e posso acompanhar você no passeio."
    alex "Ótimo. Só uma regra: fale de frente para mim e não esconda as mãos."
    ane "Combinado. Se eu errar um sinal, você pode me ajudar."

    menu:
        "Como Ane deve chamar a atenção de Alex?"
        "Tocar levemente no ombro e entrar no campo de visão":
            $ pontos_libras += 1
            alex "Certo! Agora eu posso ver você antes da conversa começar."
        "Gritar do outro lado do pátio":
            ane "Isso não funciona. Melhor entrar no campo de visão de Alex."
            alex "Agora sim. Comunicação também começa com respeito."

    n "A primeira parada seria a recepção. Mas um cartaz chamou a atenção das duas."
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
            alex "Certo. O leitor confirma o acesso e a catraca é liberada."
        "Forçar a barra da catraca":
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
    show davi feliz at entrar_direita:
        zoom 0.47
    davi "Bem-vindas! Eu sou Davi, monitor da biblioteca e estudante de Ciência da Computação."
    ane "Davi, você viu uma coxinha muito importante passar por aqui?"
    davi "Vi uma caixa passeando para o lado da biblioteca. Parecia um projeto com fome."
    alex "Antes de seguir, ensine aos calouros um sinal útil."
    davi "Este é o sinal de BIBLIOTECA. Veja o vídeo e depois tente fazer."
    $ renpy.notify("Novo sinal aprendido: BIBLIOTECA")

    menu:
        "O vídeo passou rápido. O que fazer?"
        "Usar o botão para repetir o sinal":
            $ pontos_libras += 1
            davi "Perfeito. Aprender Libras precisa de atenção, prática e repetição."
        "Fingir que entendeu":
            alex "Pode pedir para repetir. Ninguém precisa disfarçar uma dúvida."

    davi "Vamos à Biblioteca Rachel de Queiroz. Lá temos livros, estudo e jogos."
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
    show davi feliz at entrar_esquerda:
        zoom 0.46
    show alex feliz at entrar_direita:
        zoom 0.43
    davi "Aqui também existe uma regra difícil: devolver o livro e não levar a coxinha para a estante."
    alex "Encontrei uma pista: uma nota dizendo LABORATÓRIO CINCO."
    davi "O mistério sabe escrever, mas ainda precisa melhorar a letra."
    n "Antes de sair, Davi apresenta mais dois sinais disponíveis no jogo."
    davi "Para estudar aqui, você pode LER e usar o COMPUTADOR."
    $ renpy.notify("Sinais aprendidos: LER e COMPUTADOR")
    jump laboratorio

label laboratorio:
    $ lugares_visitados.append("Laboratórios de informática")
    scene bg laboratorio:
        size (1920, 1080)
        alpha 0.0
        linear 0.6 alpha 1.0
    n "Os laboratórios de informática apoiam aulas práticas, programação e projetos de Ciência da Computação."
    show lia feliz at entrar_centro:
        zoom 0.54
    lia "Olá! Eu sou a professora Lia. Bem-vindos à Ciência da Computação do IFCE Maracanaú."
    hide lia feliz with dissolve
    show alex feliz at entrar_esquerda:
        zoom 0.43
    show ane feliz at entrar_direita:
        zoom 0.43
    ane "Professora, procuramos uma coxinha desaparecida. A investigação agora também é computacional."
    alex "Nossa hipótese aponta para este laboratório e para um computador com uma mensagem aberta."
    show lia feliz at entrar_centro:
        zoom 0.48
    lia "A caixa esteve aqui, mas seguiu para a sala. Antes disso, temos uma missão de Computação e Libras."

    n "Na tela havia um pequeno programa: ele deveria mostrar a próxima pista, mas repetia a palavra COXINHA para sempre."
    ane "Encontramos um bug com fome infinita. Isso é sofisticado ou preocupante?"
    davi "Na Computação, chamamos isso de laço infinito. Na cantina, chamamos de terça-feira."

    menu:
        "Como corrigir o programa?"
        "Revisar a condição de parada do laço":
            $ pontos_libras += 1
            alex "Certo. Um algoritmo precisa saber quando continuar e quando parar."
        "Desligar o computador e dizer que foi mistério":
            lia "Criativo, mas não resolve o programa. Vamos ler a mensagem e revisar o código."

    n "Alex corrigiu a condição. O programa mostrou: PROCURE NA SALA DE AULA."
    lia "Programar é organizar ideias, testar, errar, revisar e tentar outra vez."

    menu:
        "Qual atitude facilita uma conversa em Libras?"
        "Manter boa iluminação e as mãos visíveis":
            $ pontos_libras += 1
            lia "Exatamente. Expressões do rosto e movimentos das mãos fazem parte da língua."
        "Apagar a luz para ver apenas o computador":
            lia "Computador no escuro parece cinema, mas impede a comunicação visual."
            alex "Vamos manter a luz e as mãos visíveis."

    lia "Libras é uma língua completa, com estrutura própria. Não é português feito palavra por palavra."
    lia "Os vídeos deste jogo mostram sinais isolados para apoiar o aprendizado. Uma tradução deve ser revisada por pessoa fluente."
    lia "Software acessível começa no planejamento. Legenda, Libras e interface visual não devem ficar para depois."
    $ renpy.notify("Sinal aprendido: ACESSIBILIDADE")
    jump sala

label sala:
    $ lugares_visitados.append("Salas de aula")
    scene bg sala:
        size (1920, 1080)
    with Fade(0.45, 0.15, 0.55, color="#ffffff")
    n "As salas de aula são espaços de teoria, debate e trabalho em equipe. A última pista estava sobre a mesa."
    show davi feliz at entrar_esquerda:
        zoom 0.43
    show ane feliz at entrar_direita:
        zoom 0.42
    davi "A caixa está aqui! O mistério acabou antes da prova."
    ane "Mas ela está vazia. Temos agora o mistério da coxinha invisível."
    show alex feliz at entrar_centro:
        zoom 0.42
    alex "Vejam a mensagem: A COXINHA ESTÁ NA REUNIÃO. A caixa era somente a pista."
    hide alex feliz with dissolve
    show lia feliz at entrar_centro:
        zoom 0.48
    lia "Parabéns. O passeio era a primeira atividade de recepção dos calouros."
    lia "Vocês conheceram o pátio, a biblioteca, os laboratórios e as salas. Também resolveram o primeiro bug do curso."
    ane "Então ninguém roubou a coxinha?"
    davi "Ainda não. Mas a reunião vai começar, então precisamos ir rápido."

    menu:
        "Antes da reunião, qual sinal você quer repetir?"
        "BIBLIOTECA":
            $ pontos_libras += 1
            davi "BIBLIOTECA. Um lugar para ler, estudar e encontrar ajuda."
        "COMPUTADOR":
            $ pontos_libras += 1
            ane "COMPUTADOR. Nosso colega de projetos e fornecedor oficial de mensagens de erro."
        "ACESSIBILIDADE":
            $ pontos_libras += 1
            lia "ACESSIBILIDADE. Ela deve estar presente desde o começo de cada projeto."
    jump final

label final:
    scene bg sagui:
        size (1920, 1080)
        xalign 0.5
        yalign 0.5
    with dissolve
    n "No caminho do refeitório, um sagui observava o movimento entre as árvores do campus."
    ane "Ele está fiscalizando quem ainda tem saldo para o almoço."
    alex "Ou investigando o desaparecimento da coxinha. Temos um novo suspeito, mas nenhuma prova."

    scene bg refeitorio:
        size (1920, 1080)
    with Fade(0.7, 0.2, 1.0, color="#0b2b21")
    n "No refeitório, o cartão recarregado permite comprar a refeição. Na reunião, também havia coxinha para todos e informações sobre o curso."
    show alex feliz at entrar_centro, flutuar:
        zoom 0.48
    alex "Hoje eu conheci o campus. Amanhã começam as primeiras aulas da nossa semana."
    if pontos_libras >= 3:
        centered "{size=54}{color=#7fe0aa}EXCELENTE RECEPÇÃO!{/color}{/size}\nVocê praticou comunicação visual em [pontos_libras] momentos."
    else:
        centered "{size=54}{color=#ffd166}MISSÃO CONCLUÍDA!{/color}{/size}\nUse o botão de repetir e continue praticando Libras."
    centered "{size=34}Lugares visitados{/size}\n[join_lista(lugares_visitados)]\n\n{color=#7fe0aa}Fim da segunda-feira{/color}"
    jump dia_2_programacao

label dia_2_programacao:
    scene bg laboratorio:
        size (1920, 1080)
        zoom 1.04
        ease 2.0 zoom 1.0
    with Fade(0.7, 0.2, 0.7, color="#10251f")
    centered "{size=60}{color=#7fe0aa}TERÇA-FEIRA{/color}{/size}\n{size=34}Fundamentos de Programação{/size}"

    show alex feliz at entrar_esquerda:
        zoom 0.41
    show ane feliz at entrar_direita, reagir_surpresa:
        zoom 0.40
    ane "A lousa já tem fluxogramas. A aula nem começou e as setas parecem saber aonde vão."
    alex "Tomara que elas expliquem o caminho para nós também."

    hide ane feliz with dissolve
    show fabio aula at destaque_professor
    fabio "Bom dia! Eu sou o professor Fábio e esta é a disciplina de Fundamentos de Programação."
    fabio "Um algoritmo é uma sequência organizada de passos para resolver um problema. Antes da linguagem de programação, precisamos aprender a pensar na solução."
    fabio "Vamos trabalhar com variáveis, entrada e saída, decisões, repetições, funções e testes. Esses conceitos aparecem em quase todas as áreas do curso."
    fabio "Eles serão usados em sistemas, aplicativos, jogos, inteligência artificial, bancos de dados e nos projetos das próximas disciplinas."

    menu:
        "O programa precisa escolher entre aprovado e reprovado. Qual conceito usar?"
        "Uma condição, como se/senão":
            $ pontos_libras += 1
            fabio "Exatamente. A condição permite que o programa tome caminhos diferentes conforme os dados."
        "Um laço infinito":
            fabio "O laço repete instruções. Para escolher entre dois caminhos, começamos com uma condição."

    hide fabio aula with dissolve
    show ane feliz at entrar_direita, reagir_riso:
        zoom 0.40
    ane "Então o caso da coxinha sumida era um algoritmo: procurar, perguntar e repetir até o intervalo."
    alex "Com uma condição de parada muito importante: encontrar a coxinha."
    centered "{size=38}{color=#7fe0aa}Conceitos do dia{/color}{/size}\nAlgoritmos • variáveis • condições • repetições • funções"
    jump dia_3_calculo

label dia_3_calculo:
    scene bg sala:
        size (1920, 1080)
        xalign 0.5
    with pushleft
    centered "{size=60}{color=#8ed1fc}QUARTA-FEIRA{/color}{/size}\n{size=34}Cálculo I{/size}"

    show edson aula at destaque_professor
    edson "Olá! Eu sou o professor Edson. Em Cálculo I estudaremos funções, limites, derivadas e, mais adiante, integrais."
    edson "Uma função descreve como uma quantidade depende de outra. O limite ajuda a entender o comportamento quando nos aproximamos de um ponto."
    edson "A derivada mede taxa de mudança: velocidade, crescimento ou inclinação. Na Computação, isso aparece em gráficos, simulações, otimização e aprendizado de máquina."
    edson "O objetivo não é decorar símbolos. É aprender a modelar problemas e interpretar o resultado."

    hide edson aula with dissolve
    show alex feliz at entrar_esquerda, reagir_pensando:
        zoom 0.41
    show ane feliz at entrar_direita:
        zoom 0.40
    ane "Se a quantidade de exercícios cresce e meu tempo livre diminui, isso já conta como função?"
    alex "Conta como uma função assustadoramente realista."
    show ane feliz at entrar_direita, reagir_surpresa:
        zoom 0.40

    menu:
        "Qual ideia representa melhor uma derivada?"
        "A taxa de mudança de uma quantidade":
            $ pontos_libras += 1
            edson "Muito bem. Ela mostra como algo varia naquele instante."
        "Uma lista de passos de um algoritmo":
            edson "Isso pertence à programação. Em Cálculo, a derivada está ligada à variação."

    centered "{size=38}{color=#8ed1fc}Conceitos do dia{/color}{/size}\nFunções • limites • derivadas • modelagem"
    jump dia_4_discreta

label dia_4_discreta:
    scene bg sala:
        size (1920, 1080)
        xalign 0.5
        matrixcolor TintMatrix("#fff3d6")
    with Fade(0.5, 0.1, 0.6, color="#5a3218")
    centered "{size=60}{color=#ffd166}QUINTA-FEIRA{/color}{/size}\n{size=34}Matemática Discreta{/size}"

    show cicero aula at destaque_professor
    cicero "Eu sou o professor Cícero. Matemática Discreta estuda estruturas formadas por elementos separados, muito próximas do funcionamento da Computação."
    cicero "Começaremos com lógica, proposições, conjuntos, relações, funções, técnicas de contagem e grafos."
    cicero "A lógica ajuda a escrever condições corretas. Grafos representam redes, rotas, amizades, dependências e conexões entre computadores."
    cicero "Vocês usarão esse raciocínio em algoritmos, bancos de dados, redes, segurança e análise de problemas."

    hide cicero aula with dissolve
    show ane feliz at entrar_direita, reagir_surpresa:
        zoom 0.40
    ane "Então um mapa do campus pode virar um grafo?"
    show alex feliz at entrar_esquerda:
        zoom 0.41
    alex "Sim. Os lugares são vértices e os caminhos viram arestas. A cantina provavelmente é o vértice mais visitado."

    menu:
        "Em um mapa representado por grafo, o que são os caminhos entre lugares?"
        "Arestas":
            $ pontos_libras += 1
            cicero "Correto. Os lugares podem ser vértices e as ligações entre eles são arestas."
        "Variáveis de texto":
            cicero "Variáveis guardam dados. No grafo, usamos arestas para representar as conexões."

    centered "{size=38}{color=#ffd166}Conceitos do dia{/color}{/size}\nLógica • conjuntos • contagem • grafos"
    jump dia_5_circuitos

label dia_5_circuitos:
    scene bg laboratorio:
        size (1920, 1080)
        matrixcolor TintMatrix("#d8f3ef")
    with pushleft
    centered "{size=60}{color=#b8a1ff}SEXTA-FEIRA{/color}{/size}\n{size=34}Circuitos Digitais — Eletrônica Digital{/size}"

    show otavio aula at destaque_professor
    otavio "Bem-vindos! Eu sou o professor Otávio. Em Circuitos Digitais veremos como informações são representadas eletronicamente."
    otavio "Começamos com os valores binários zero e um, tabelas-verdade e portas lógicas como AND, OR e NOT."
    otavio "Depois combinamos esses blocos para criar somadores, memórias e circuitos capazes de tomar decisões simples."
    otavio "Essa disciplina liga software e hardware. Ela ajuda a entender processadores, sistemas embarcados, robótica e a arquitetura dos computadores."

    hide otavio aula with dissolve
    show alex feliz at entrar_esquerda, reagir_surpresa:
        zoom 0.41
    alex "Então, por baixo dos programas, existem milhões de decisões feitas com zero e um."
    show ane feliz at entrar_direita, reagir_riso:
        zoom 0.40
    ane "E eu levei quatro dias para decidir entre suco e refrigerante. O processador está na frente."

    menu:
        "Qual porta inverte um valor lógico?"
        "NOT":
            $ pontos_libras += 1
            otavio "Exato. Se a entrada é um, a saída vira zero; se é zero, vira um."
        "AND":
            otavio "A AND combina entradas. Quem realiza a inversão é a porta NOT."

    centered "{size=38}{color=#b8a1ff}Conceitos do dia{/color}{/size}\nBinário • portas lógicas • circuitos • hardware"
    jump encerramento_semana

label encerramento_semana:
    scene bg refeitorio:
        size (1920, 1080)
    with Fade(0.7, 0.2, 0.8, color="#10251f")
    show alex feliz at entrar_esquerda:
        zoom 0.41
    show ane feliz at entrar_direita, flutuar:
        zoom 0.40
    ane "Sobrevivemos à primeira semana: algoritmo, derivada, grafo e porta lógica."
    alex "E aprendemos como cada disciplina se conecta. Programação dá instruções, a matemática modela e prova, e os circuitos executam."
    ane "A coxinha também sobreviveu, mas por pouco."

    if pontos_libras >= 7:
        centered "{size=58}{color=#7fe0aa}SEMANA EXCELENTE!{/color}{/size}\nVocê acertou [pontos_libras] decisões e começou a conectar as disciplinas."
    else:
        centered "{size=58}{color=#ffd166}PRIMEIRA SEMANA CONCLUÍDA!{/color}{/size}\nVocê tomou [pontos_libras] boas decisões. Revise as aulas e tente novamente."
    centered "{size=34}A jornada de Alex e Ane continua...{/size}"
    return

init python:
    def join_lista(itens):
        return " • ".join(itens)
