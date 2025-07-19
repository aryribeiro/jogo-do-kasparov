# 🇷🇺 Jogo do Kasparov

Um jogo da velha (Tic-Tac-Toe) interativo desenvolvido em Python com Streamlit, onde você enfrenta uma IA com diferentes níveis de dificuldade.

## 🎮 Sobre o Jogo

Homenagem ao lendário enxadrista Garry Kasparov, que em 1997 perdeu para o supercomputador Deep Blue da IBM. Este jogo simula essa experiência histórica onde humanos enfrentam a inteligência artificial.

## ✨ Funcionalidades

- **3 Níveis de Dificuldade:**
  - 🟢 **Fácil**: IA joga aleatoriamente
  - 🟡 **Médio**: IA joga bem 70% das vezes
  - 🔴 **Difícil**: IA joga perfeitamente usando algoritmo Minimax (impossível vencer)

- **Interface Intuitiva**: Design limpo e responsivo com símbolos grandes e visíveis
- **Jogabilidade Fluida**: Jogadas automáticas da IA após cada movimento do jogador
- **Feedback Visual**: Indicadores claros de turno, vitória, empate e dificuldade

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd jogo-kasparov
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
streamlit run app.py
```

4. Abra seu navegador e acesse:
```
http://localhost:8501
```

## 🎯 Como Jogar

1. **Escolha a dificuldade** no seletor no topo da página
2. **Clique em uma célula vazia** para fazer sua jogada (você é sempre o X)
3. **Aguarde a IA** fazer sua jogada automaticamente (ela é sempre o O)
4. **Vença fazendo uma linha** horizontal, vertical ou diagonal com 3 X's
5. **Use o botão "Novo Jogo"** para reiniciar a partida

## 🧠 Algoritmo da IA

A IA utiliza o algoritmo **Minimax com poda Alpha-Beta** no modo difícil, garantindo jogadas matematicamente perfeitas. Este algoritmo:

- Avalia todas as possíveis jogadas futuras
- Escolhe sempre o movimento que maximiza suas chances de vitória
- Utiliza poda Alpha-Beta para otimizar a performance

## 📁 Estrutura do Projeto

```
jogo-kasparov/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **Streamlit**: Framework para aplicações web
- **NumPy**: Manipulação de arrays para o tabuleiro
- **HTML/CSS**: Estilização customizada da interface

## 👨‍💻 Autor

**Ary Ribeiro**
- Email: aryribeiro@gmail.com

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 🎉 Dica

Tente vencer a IA no modo difícil - é matematicamente impossível, mas você pode conseguir um empate se jogar perfeitamente! 😄