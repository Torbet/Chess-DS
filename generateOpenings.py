import pandas as pd
import io
import chess.pgn

df = pd.read_csv('data/chess.csv')

for index, row in df.iterrows():
    try:
       pgn = row['pgn']
       game = chess.pgn.read_game(io.StringIO(pgn))

       if 'ECOUrl' not in game.headers:
          df.at[index, 'opening'] = 'Unknown'
          print(index, 'Unknown')
          continue

       openingURL = game.headers['ECOUrl']
       opening = openingURL.split('/openings/')[-1]
       df.at[index, 'opening'] = opening
       print(index, opening)

    except:
      print("Error at index: ", index, row)
      continue

df.to_csv('data/chess-openings.csv', index=False)