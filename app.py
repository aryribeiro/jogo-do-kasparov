import streamlit as st
import numpy as np
import random

# Configuração da página
st.set_page_config(page_title="Jogo do Kasparov", page_icon="🇷🇺", layout="centered")

st.markdown(
   """
   <style>
   .game-title {
       text-align: center;
   }
   </style>
   <div class="game-title">
       <h1>🇷🇺 Jogo do Kasparov</h1>
       <h4>VOCÊ, perdendo para a IA!</h4>
   </div>
   """,
   unsafe_allow_html=True
)

# CSS para estilizar o tabuleiro
st.markdown("""
<style>
 .game-container {
     display: flex;
     justify-content: center;
     align-items: center;
     flex-direction: column;
     margin: 1px 0;
 }
 
 .game-title {
     text-align: center;
     margin-bottom: 2px;
 }
 
 .game-subtitle {
     text-align: center;
     margin-bottom: 2px;
 }
 
 .winner {
     font-size: 24px;
     font-weight: bold;
     color: #4CAF50;
     text-align: center;
     margin: 2px 0;
 }
 
 .current-player {
     font-size: 18px;
     margin: 2px 0;
     text-align: center;
 }
 
 .difficulty-selector {
     margin: 0px 0;
     text-align: center;
 }
 
 .stButton > button {
     height: 150px !important;
     width: 100% !important;
     font-size: 100px !important;
     line-height: 1 !important;
     border: 2px solid #000 !important;
     margin: 0 !important;
     padding: 0 !important;
     background-color: white !important;
     color: inherit !important;
     border-radius: 0px !important;
     box-shadow: none !important;
     display: flex !important;
     align-items: center !important;
     justify-content: center !important;
 }
 
 .stButton > button:hover {
     background-color: #f0f0f0 !important;
     transform: none !important;
     box-shadow: none !important;
 }
 
 .stButton > button:disabled {
     background-color: #f8f9fa !important;
     cursor: not-allowed !important;
     transform: none !important;
 }
 
 .block-container {
     padding-top: 2rem;
 }
 
 .difficulty-info {
     background-color: #f8f9fa;
     padding: 15px;
     border-radius: 10px;
     margin: 10px 0;
     border-left: 4px solid #007bff;
 }
 
 .reset-button {
     margin-top: 10px;
 }
 
 .reset-button .stButton > button {
     height: 50px !important;
     font-size: 18px !important;
     background-color: #007bff !important;
     color: white !important;
     border: none !important;
     border-radius: 8px !important;
 }
 
 .reset-button .stButton > button:hover {
     background-color: #0056b3 !important;
 }
 
 div[data-testid="column"] {
     padding: 0 !important;
     gap: 0 !important;
 }
 
 .row-widget.stHorizontal {
     gap: 0 !important;
 }
</style>
""", unsafe_allow_html=True)

# Inicialização do estado do jogo
if 'board' not in st.session_state:
  st.session_state.board = np.full((3, 3), '', dtype=str)
  st.session_state.current_player = 'X'
  st.session_state.game_over = False
  st.session_state.winner = None
  st.session_state.difficulty = 'Difícil'  # Dificuldade padrão

def check_winner(board):
  # Verificar linhas
  for i in range(3):
      if board[i, 0] == board[i, 1] == board[i, 2] != '':
          return board[i, 0]
  
  # Verificar colunas
  for j in range(3):
      if board[0, j] == board[1, j] == board[2, j] != '':
          return board[0, j]
  
  # Verificar diagonais
  if board[0, 0] == board[1, 1] == board[2, 2] != '':
      return board[0, 0]
  if board[0, 2] == board[1, 1] == board[2, 0] != '':
      return board[0, 2]
  
  return None

def is_board_full(board):
  return not np.any(board == '')

def get_available_moves(board):
  moves = []
  for i in range(3):
      for j in range(3):
          if board[i, j] == '':
              moves.append((i, j))
  return moves

def minimax(board, depth, is_maximizing, alpha=-float('inf'), beta=float('inf')):
  winner = check_winner(board)
  
  if winner == 'O':
      return 1
  elif winner == 'X':
      return -1
  elif is_board_full(board):
      return 0
  
  if is_maximizing:
      max_eval = -float('inf')
      for i in range(3):
          for j in range(3):
              if board[i, j] == '':
                  board[i, j] = 'O'
                  eval_score = minimax(board, depth + 1, False, alpha, beta)
                  board[i, j] = ''
                  max_eval = max(max_eval, eval_score)
                  alpha = max(alpha, eval_score)
                  if beta <= alpha:
                      break
      return max_eval
  else:
      min_eval = float('inf')
      for i in range(3):
          for j in range(3):
              if board[i, j] == '':
                  board[i, j] = 'X'
                  eval_score = minimax(board, depth + 1, True, alpha, beta)
                  board[i, j] = ''
                  min_eval = min(min_eval, eval_score)
                  beta = min(beta, eval_score)
                  if beta <= alpha:
                      break
      return min_eval

def get_best_move(board):
  best_move = None
  best_value = -float('inf')
  
  for i in range(3):
      for j in range(3):
          if board[i, j] == '':
              board[i, j] = 'O'
              move_value = minimax(board, 0, False)
              board[i, j] = ''
              
              if move_value > best_value:
                  best_value = move_value
                  best_move = (i, j)
  
  return best_move

def computer_move(board, difficulty):
  available_moves = get_available_moves(board)
  if not available_moves:
      return None
  
  if difficulty == 'Fácil':
      return random.choice(available_moves)
  elif difficulty == 'Médio':
      if random.random() < 0.7:
          return get_best_move(board)
      else:
          return random.choice(available_moves)
  else:  # Difícil
      return get_best_move(board)

def make_move(row, col):
  if not st.session_state.game_over and st.session_state.board[row, col] == '':
      st.session_state.board[row, col] = st.session_state.current_player
      
      winner = check_winner(st.session_state.board)
      if winner:
          st.session_state.winner = winner
          st.session_state.game_over = True
      elif is_board_full(st.session_state.board):
          st.session_state.game_over = True
      else:
          st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'
          
          # Vez do computador
          if st.session_state.current_player == 'O' and not st.session_state.game_over:
              comp_move = computer_move(st.session_state.board, st.session_state.difficulty)
              if comp_move:
                  st.session_state.board[comp_move[0], comp_move[1]] = 'O'
                  winner = check_winner(st.session_state.board)
                  if winner:
                      st.session_state.winner = winner
                      st.session_state.game_over = True
                  elif is_board_full(st.session_state.board):
                      st.session_state.game_over = True
                  else:
                      st.session_state.current_player = 'X'

def reset_game():
  st.session_state.board = np.full((3, 3), '', dtype=str)
  st.session_state.current_player = 'X'
  st.session_state.game_over = False
  st.session_state.winner = None

# Seleção de dificuldade
st.markdown('<div class="difficulty-selector">', unsafe_allow_html=True)
difficulty = st.selectbox(
  "Escolha a dificuldade:",
  ["Fácil", "Médio", "Difícil"],
  index=2,
  key="difficulty_selector"
)

if difficulty != st.session_state.difficulty:
  st.session_state.difficulty = difficulty
  reset_game()

# Informações sobre dificuldade
difficulty_info = {
  "Fácil": "🟢 IA joga aleatoriamente",
  "Médio": "🟡 IA joga bem 70% das vezes",
  "Difícil": "🔴 IA joga perfeitamente (impossível vencer)"
}

st.markdown(f'<div class="difficulty-info">{difficulty_info[difficulty]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Informações do jogo
if st.session_state.game_over:
  if st.session_state.winner:
      if st.session_state.winner == 'X':
          st.markdown('<div class="winner">🙋🏼‍♂ Você Venceu!</div>', unsafe_allow_html=True)
      else:
          st.markdown('<div class="winner">🤖 IA Venceu!!!</div>', unsafe_allow_html=True)
  else:
      st.markdown('<div class="winner">🤝 Empate!</div>', unsafe_allow_html=True)
else:
  if st.session_state.current_player == 'X':
      st.markdown('<div class="current-player">Você é o X! 👇🏻 Comece o jogo e aguarde a IA...</div>', unsafe_allow_html=True)
  else:
      st.markdown('<div class="current-player">Vez do computador</div>', unsafe_allow_html=True)

# Tabuleiro do jogo
st.markdown('<div class="game-container">', unsafe_allow_html=True)

# Criar o tabuleiro 3x3 com células visíveis
for i in range(3):
  cols = st.columns(3, gap="small")
  for j in range(3):
      with cols[j]:
          cell_value = st.session_state.board[i, j]
          if cell_value == 'X':
              button_html = '''<div style="height: 150px; width: 100%; border: 2px solid #000; 
                              background: white; display: flex; align-items: center; 
                              justify-content: center; font-size: 90px; cursor: not-allowed;">❌</div>'''
              st.markdown(button_html, unsafe_allow_html=True)
          elif cell_value == 'O':
              button_html = '''<div style="height: 150px; width: 100%; border: 2px solid #000; 
                              background: white; display: flex; align-items: center; 
                              justify-content: center; font-size: 90px; cursor: not-allowed;">⭕</div>'''
              st.markdown(button_html, unsafe_allow_html=True)
          else:
              if st.button("", key=f"cell_{i}_{j}", 
                          disabled=st.session_state.game_over,
                          use_container_width=True):
                  make_move(i, j)
                  st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Botão para reiniciar
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
  st.markdown('<div class="reset-button">', unsafe_allow_html=True)
  if st.button("🔄 Novo Jogo", use_container_width=True):
      reset_game()
      st.rerun()
  st.markdown('</div>', unsafe_allow_html=True)

# Instruções
st.markdown(
    """
    ---
    <style>
    .game-footer {
        text-align: center;
    }
    </style>
    <div class="game-footer">
        <h4>🇷🇺 Jogo do Kasparov: 😅 homenagem ao russo, que perdeu p/ a IA</h4>
    Clique em uma célula vazia para fazer sua jogada. A IA jogará automaticamente como <strong>O</strong>. 
    Vence quem conseguir 3 símbolos em linha (horizontal, vertical ou diagonal) 
    - por <strong>Ary Ribeiro</strong>: aryribeiro@gmail.com
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
    .main {
        background-color: #ffffff;
        color: #333333;
    }
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }

    /* Esconde a barra padrão do Streamlit */
    header {display: none !important;}
    footer {display: none !important;}
    #MainMenu {display: none !important;}

    /* Reduz, mas não zera, o espaço vertical */
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    div[data-testid="stVerticalBlock"] {
        gap: 0.3rem !important; /* Espaçamento vertical mínimo */
        padding-top: 0.3rem !important;
        padding-bottom: 0.3rem !important;
    }

    /* Mantém margens mínimas para evitar "embolamento" */
    .element-container {
        margin-top: 0rem !important;
        margin-bottom: 0rem !important;
    }

    /* Espaçamento horizontal entre elementos lado a lado */
    div[data-testid="column"] {
        padding-left: 0rem;
        padding-right: 0rem;
    }
</style>
""", unsafe_allow_html=True)