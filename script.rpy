define e = Character("Alex", color="#6ec6ff")
define j = Character("Ane", color="#ff91c8")
define m = Character("Madruga", color="#ffd166")
define n = Character(None)

image bg room = "bgroom.png"
image bg patio = "bg_patio.png"
image bg laboratorio = "bg_laboratorio.png"
image bg cantina = "bg_cantina.png"
image Alex happy = "Alex1.png"
image Ane happy = "Ane.png"
image Madruga happy = "Madruga.png"

label start:
    scene bg room:
        size (1920, 1080)
    with fade

    n "Era o primeiro dia de aula no IFCE Campus Maracanaú."
    n "Ane observava os corredores, tentando esconder o nervosismo enquanto procurava sua sala."

    show Ane happy:
        zoom 0.5
        xalign 0.2
        yalign 1.0
    with dissolve

    j "Laboratório cinco... bloco dois... Por que todo corredor parece igual?"
    j "Se eu me atrasar logo no primeiro dia, vou entrar para a história do campus."

    show Alex happy:
        zoom 0.5
        xalign 0.72
        yalign 1.0
    with moveinright

    e "Você parece estar procurando alguma coisa. Posso ajudar?"
    j "Oi! Estou procurando o laboratório cinco. Sou caloura de Ciência da Computação."
    e "Então você está com sorte. Eu sou Alex, do quinto semestre, e também estou indo para aquele lado."
    j "Prazer, Alex! Eu sou a Ane. Já estava pensando em pedir um mapa e uma bússola."
    e "Depois de algumas semanas você se acostuma. Ou aprende a disfarçar quando está perdido."
    j "Ótimo conselho para o meu primeiro dia."

    menu:
        "Aceitar o passeio pelo campus":
            j "Se você tiver tempo, pode me mostrar os lugares mais importantes?"
            e "Claro! Uma visita guiada por um veterano quase pontual."
            jump passeio

        "Ir direto para o laboratório":
            j "Melhor irmos direto ao laboratório. Não quero perder a primeira aula."
            e "Boa escolha. O passeio fica para o intervalo."
            jump laboratorio

label passeio:
    scene bg patio:
        size (1920, 1080)
    with fade

    n "Os dois atravessaram o pátio central. O campus já estava cheio de conversas e passos apressados."

    show Alex happy:
        zoom 0.5
        xalign 0.68
        yalign 1.0
    show Ane happy:
        zoom 0.5
        xalign 0.22
        yalign 1.0

    e "Aqui fica a biblioteca. É silenciosa, tem ar-condicionado e salva muita gente na semana de provas."
    j "Em outras palavras, será minha segunda casa."
    e "Mais adiante ficam os laboratórios. Nunca esqueça de salvar seus projetos em mais de um lugar."
    j "Isso parece uma história traumática."
    e "Quatro horas de código perdidas. Prefiro não falar sobre isso."

    show Madruga happy:
        zoom 0.5
        xalign 0.45
        yalign 1.0
    with moveinleft

    m "Alex! Já está recrutando gente para fazer os trabalhos do semestre?"
    e "Ane, este é o Madruga. Ignore metade do que ele disser."
    m "Só metade? Estou melhorando."
    j "Prazer, Madruga."
    m "O prazer é meu. Vocês vão à cantina? A famosa parada no Pardal faz parte da visita oficial."
    e "Primeiro o laboratório, depois o lanche."
    m "A responsabilidade venceu outra vez. Que fase triste."
    jump laboratorio

label laboratorio:
    scene bg laboratorio:
        size (1920, 1080)
    with fade

    n "No laboratório, as máquinas já estavam ligadas e um exercício aguardava a turma no quadro."

    show Ane happy:
        zoom 0.5
        xalign 0.2
        yalign 1.0
    show Alex happy:
        zoom 0.5
        xalign 0.7
        yalign 1.0

    j "O exercício pede um programa que organize as notas dos alunos. Parece simples... eu acho."
    e "A primeira regra da programação é nunca confiar quando alguma coisa parece simples."
    j "E qual é a segunda?"
    e "Ler a mensagem de erro antes de entrar em pânico."
    n "Ane digitou algumas linhas, executou o programa e encarou a tela."
    j "Deu erro. A segunda regra já está sendo testada."
    e "Vamos por partes. Confira os nomes das variáveis e a indentação."
    j "Achei! Escrevi 'media' de duas formas diferentes."
    e "Parabéns, você conheceu o bug mais comum da humanidade: digitar com pressa."

    menu:
        "Pedir para Alex explicar o código":
            j "Você pode me explicar por que usamos uma lista aqui? Quero entender de verdade."
            e "Claro. A lista guarda várias notas numa única estrutura. Assim calculamos tudo sem repetir código."
            j "Agora fez sentido. É como organizar várias gavetas dentro do mesmo armário."
            e "Exatamente. E um bom programador sempre etiqueta as gavetas."
            $ estudou = True

        "Tentar resolver sem ajuda":
            j "Vou tentar mais uma vez sozinha. Se eu travar, peço socorro."
            e "Combinado. Estou logo aqui."
            n "Depois de alguns testes, Ane encontrou a solução e sorriu ao ver o resultado correto."
            j "Funcionou!"
            e "Guarde essa sensação. Ela é o combustível de todo programador."
            $ estudou = False

    jump intervalo

label intervalo:
    scene bg cantina:
        size (1920, 1080)
    with fade

    n "No intervalo, os três se encontraram perto da cantina."

    show Ane happy:
        zoom 0.5
        xalign 0.15
        yalign 1.0
    show Madruga happy:
        zoom 0.5
        xalign 0.48
        yalign 1.0
    show Alex happy:
        zoom 0.5
        xalign 0.78
        yalign 1.0

    m "Finalmente! Minha presença aqui é puramente acadêmica: pesquiso o melhor salgado do campus."
    j "E a pesquisa está avançada?"
    m "Anos de dedicação e nenhum resultado conclusivo. Preciso continuar testando."
    e "Ane terminou o primeiro programa dela."
    m "Então temos um motivo de verdade para comemorar."

    if estudou:
        j "Alex me ajudou a entender como as listas funcionam."
        m "Cuidado. Daqui a pouco ele começa a cobrar monitoria em coxinhas."
    else:
        j "Eu insisti um pouco e consegui encontrar o erro sozinha."
        m "Essa é a atitude. Só não vale discutir com o computador; ele quase nunca pede desculpas."

    e "Falando sério, estamos montando uma equipe para a mostra de projetos do campus."
    j "Que tipo de projeto?"
    e "Um jogo educativo sobre a vida universitária, com acessibilidade em Libras."
    j "Então a pessoa pode acompanhar a legenda e também assistir à tradução de cada fala?"
    e "Essa é a ideia. O vídeo aparece ao lado do diálogo e pode ser repetido quantas vezes for preciso."
    m "Além de incluir, o jogo ajuda quem está começando a conhecer Libras."
    j "Mas precisamos tomar cuidado para não traduzir palavra por palavra. Libras tem estrutura própria."
    e "Exatamente. A tecnologia ajuda a exibir os sinais, mas as traduções precisam ser revisadas por alguém fluente."
    j "Podemos acrescentar um glossário com sinais importantes do cotidiano no campus."
    m "Biblioteca, laboratório, professor, prova... e cantina, que é essencial para a pesquisa."
    e "Ainda precisamos de alguém com ideias novas."
    m "E de alguém que impeça o Alex de colocar cinquenta telas de tutorial."
    e "E de alguém que impeça o Madruga de transformar tudo em piada."
    j "Parece que vocês precisam mesmo de ajuda."

    menu:
        "Entrar para a equipe":
            j "Eu topo! Ainda tenho muito que aprender, mas quero participar."
            e "É assim que todo projeto começa. Bem-vinda à equipe!"
            m "Primeira reunião amanhã. Eu levo os salgados científicos."
            jump final_equipe

        "Pensar antes de decidir":
            j "A ideia é boa, mas quero conhecer melhor minha rotina antes de prometer."
            e "Justo. Projeto bom também precisa de planejamento."
            m "Quando decidir, procure a gente. A vaga e as piadas continuam disponíveis."
            jump final_aberto

label final_equipe:
    scene bg room:
        size (1920, 1080)
    with fade
    n "Ao fim do primeiro dia, Ane já não via o campus como um labirinto."
    n "Agora cada corredor parecia levar a uma nova possibilidade."
    show Ane happy:
        zoom 0.55
        xalign 0.5
        yalign 1.0
    with dissolve
    j "Uma aula, um programa funcionando e uma equipe nova... Nada mal para o primeiro dia."
    n "Continua..."
    return

label final_aberto:
    scene bg room:
        size (1920, 1080)
    with fade
    n "Ane se despediu dos novos colegas e seguiu para a próxima aula."
    n "Ela ainda não sabia quais desafios encontraria, mas já sabia que não precisaria enfrentá-los sozinha."
    show Ane happy:
        zoom 0.55
        xalign 0.5
        yalign 1.0
    with dissolve
    j "Acho que vou gostar daqui."
    n "Continua..."
    return
