import pandas as pd
from stockfish import Stockfish

df = pd.read_csv('data/chess-eval.csv')
data = df.loc[df['evaluation'].isnull() & df['mate'].isnull() & ((df['white_result'] == 'resigned') | (df['black_result'] == 'resigned'))]

for index, row in data.iterrows():
    try:
      stockfish = Stockfish()
      stockfish.set_fen_position(row['fen'])
      evaluation = stockfish.get_evaluation()
      print(index, evaluation)

      if evaluation['type'] == 'mate':
          # mate in x moves
          df.at[index, 'mate'] = evaluation['value']
      else:
          # centipawns
          # 100 centipawns = 1 pawn
          df.at[index, 'evaluation'] = evaluation['value'] / 100
    except:
      print('error')

df.to_csv('data/chess-eval.csv', index=False)