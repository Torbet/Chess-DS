import pandas as pd
import chess
from stockfish import Stockfish

def getPieceImbalance(fen):
    board = chess.Board(fen)
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
        3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
        3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
        5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
        9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens))
    )

df = pd.read_csv('data/chess.csv')
engine = Stockfish()
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
engine.set_fen_position(fen)
# depth = 20
engine.set_depth(12)
print(engine.get_evaluation())

"""
for i, row in df.iterrows():
  ev = getPieceImbalance(row['fen'])
  print(i, ev)
  df.at[i, 'evaluation'] = ev

df.to_csv('data/chess-imbalance.csv', index=False)
"""