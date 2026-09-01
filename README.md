# Sinais do Maracanaú

![Tela inicial de Sinais do Maracanaú](images/menu/elenco_campus.png)

**Sinais do Maracanaú** é uma visual novel educativa ambientada no IFCE Campus Maracanaú. O jogador acompanha estudantes em uma visita guiada pelo campus, conhece serviços e espaços importantes e aprende sinais introdutórios de Libras por meio de diálogos, vídeos e desafios interativos.

> Versão 3.0 · Desenvolvido com Ren'Py · Conteúdo em português · Recursos de Libras disponíveis offline

## Sobre o projeto

O jogo transforma a recepção de novos alunos em uma experiência narrativa e acessível. Ao longo da jornada, o jogador toma decisões, visita diferentes locais do campus, registra sinais no caderno e recebe um relatório de desempenho ao concluir a experiência.

A história combina cenários inspirados em espaços reais do IFCE com ilustrações em estilo anime. Entre as cenas estão a chegada da jardineira, a entrada pela catraca, corredores, laboratórios, quadra, biblioteca e as áreas interna e externa do refeitório.

## Principais recursos

- Narrativa interativa com escolhas e consequências.
- Cenários do IFCE Campus Maracanaú recriados em estilo anime.
- Painel de Libras integrado aos diálogos.
- Vídeos locais em WebM, disponíveis sem conexão com a internet.
- Caderno para revisar os sinais encontrados durante a história.
- Mapa de progresso com oito locais do campus.
- Desafios visuais e perguntas de vocabulário.
- Sistema de conquistas e easter eggs interativos.
- Relatório final com decisões corretas, locais visitados, sinais e conquistas.
- Recursos de acessibilidade, incluindo texto legível, controles de repetição e apoio visual.

## Destaques da experiência

### Uma recepção guiada

Alex e outros personagens apresentam o campus, explicam rotinas importantes e ajudam os calouros a se orientar. A jardineira é apresentada logo no início, com informações sobre o transporte entre o metrô e o campus e a recomendação de consultar os horários nos avisos oficiais.

### Aprendizado de Libras

Cada conversa pode destacar sinais relevantes. O jogador assiste às demonstrações, repete os vídeos e reúne o conteúdo no caderno para consulta posterior.

### Exploração e desafios

As cenas incluem perguntas de interpretação, vocabulário e programação, além de atividades visuais que reforçam o conteúdo apresentado durante a visita.

## Como executar

### Pelo Ren'Py Launcher

1. Instale o [Ren'Py](https://www.renpy.org/) 8.5.3 ou uma versão compatível.
2. Clone este repositório:

   ```bash
   git clone https://github.com/Alewxdev/tour-ifce-maracanau.git
   ```

3. Abra o Ren'Py Launcher.
4. Escolha **Adicionar projeto existente** e selecione a pasta clonada.
5. Clique em **Iniciar projeto**.

### Pela linha de comando

No macOS ou Linux, com o SDK do Ren'Py instalado:

```bash
/caminho/para/renpy.sh .
```

Para executar a verificação estática do projeto:

```bash
/caminho/para/renpy.sh . lint
```

## Estrutura do projeto

```text
.
├── audio/                 # Músicas e efeitos sonoros
├── images/
│   ├── campus/            # Cenários do campus
│   ├── menu/              # Arte e elementos do menu
│   └── personagens/       # Sprites dos personagens
├── videos/                # Conteúdo local de Libras
├── script.rpy             # Roteiro principal
├── sistemas.rpy           # Mapa, caderno, desafios e conquistas
├── screens.rpy            # Interfaces do jogo
└── options.rpy            # Metadados e configurações do projeto
```

## Nota pedagógica e de acessibilidade

O conteúdo de Libras deste projeto tem finalidade introdutória e educativa. Ele não substitui tradução profissional nem a atuação de intérpretes. Antes de uso institucional, recomenda-se a validação pedagógica final por uma pessoa surda fluente em Libras e pela comunidade envolvida.

Os vídeos de sinais utilizam materiais do Signbank/UFSC conforme os créditos exibidos no próprio jogo, sob licença **CC BY-NC-SA 4.0**. Os demais códigos, imagens e recursos permanecem sujeitos às licenças e autorizações de seus respectivos autores.

## Tecnologias

- Ren'Py 8.5.3
- Python (integrado ao Ren'Py)
- Imagens PNG/JPEG
- Vídeos WebM

## Campus retratado

Instituto Federal de Educação, Ciência e Tecnologia do Ceará — **IFCE Campus Maracanaú**.
