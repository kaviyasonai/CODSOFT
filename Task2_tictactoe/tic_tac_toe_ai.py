"""
Tic-Tac-Toe AI — Minimax with Alpha-Beta Pruning
=================================================
Human  : X
AI     : O

The AI is unbeatable — best possible outcome for the human is a draw.
"""

import math
import os
import time


# Constants

HUMAN = "X"
AI    = "O"
EMPTY = " "

WIN_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],   # cols
    [0, 4, 8], [2, 4, 6],               # diagonals
]



# Board helpers

def make_board() -> list[str]:
    return [EMPTY] * 9


def display_board(board: list[str], highlight: list[int] = None) -> None:
    """Pretty-print the board with optional cell highlighting."""
    highlight = highlight or []
    symbols = {HUMAN: "X", AI: "O", EMPTY: " "}

    def cell(i: int) -> str:
        v = board[i]
        marker = symbols[v] if v != EMPTY else str(i + 1)
        if i in highlight:
            return f"[{marker}]"
        return f" {marker} "

    sep = "+-----+-----+-----+"
    print(f"\n{sep}")
    for row in range(3):
        base = row * 3
        print(f"| {cell(base)} | {cell(base+1)} | {cell(base+2)} |")
        print(sep)
    print()


def available_moves(board: list[str]) -> list[int]:
    return [i for i, v in enumerate(board) if v == EMPTY]


def check_winner(board: list[str]) -> str | None:
    """Return HUMAN, AI, 'draw', or None if game is still going."""
    for line in WIN_LINES:
        a, b, c = line
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if not available_moves(board):
        return "draw"
    return None


# Minimax with Alpha-Beta Pruning

_node_count = 0   # global counter reset before each AI move


def minimax(
    board: list[str],
    depth: int,
    is_maximising: bool,
    alpha: float,
    beta: float,
    use_alpha_beta: bool,
) -> int:
    global _node_count
    _node_count += 1

    result = check_winner(board)
    if result == AI:
        return 10 - depth          # prefer faster wins
    if result == HUMAN:
        return depth - 10          # prefer slower losses
    if result == "draw":
        return 0

    if is_maximising:              # AI's turn — maximise score
        best = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta, use_alpha_beta)
            board[move] = EMPTY
            best = max(best, score)
            if use_alpha_beta:
                alpha = max(alpha, best)
                if beta <= alpha:
                    break          # β cut-off
        return best

    else:                          # Human's turn — minimise score
        best = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta, use_alpha_beta)
            board[move] = EMPTY
            best = min(best, score)
            if use_alpha_beta:
                beta = min(beta, best)
                if beta <= alpha:
                    break          # α cut-off
        return best


def best_move(board: list[str], use_alpha_beta: bool = True) -> tuple[int, int]:
    """Return (best_index, nodes_searched)."""
    global _node_count
    _node_count = 0

    best_score = -math.inf
    best_idx   = -1

    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf, use_alpha_beta)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            best_idx   = move

    return best_idx, _node_count


# Winning line finder (for highlighting)

def winning_line(board: list[str]) -> list[int]:
    for line in WIN_LINES:
        a, b, c = line
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return line
    return []

# Game loop

def get_human_move(board: list[str]) -> int:
    moves = available_moves(board)
    while True:
        try:
            raw = input("Your move (1-9): ").strip()
            idx = int(raw) - 1
            if idx in moves:
                return idx
            print(f"  ✗  Cell {raw} is taken or invalid. Available: {[m+1 for m in moves]}")
        except ValueError:
            print("  ✗  Please enter a number between 1 and 9.")


def clear() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def print_header(scores: dict, use_alpha_beta: bool) -> None:
    ab_tag = "Alpha-Beta ON" if use_alpha_beta else "Alpha-Beta OFF"
    print("=" * 42)
    print("         TIC-TAC-TOE  —  Minimax AI")
    print(f"         Algorithm: {ab_tag}")
    print("=" * 42)
    print(f"  You (X): {scores['human']}   "
          f"Draws: {scores['draw']}   "
          f"AI (O): {scores['ai']}")
    print("  Numbered squares show available moves.")
    print()


def play_game(use_alpha_beta: bool = True, human_goes_first: bool = True) -> None:
    scores = {"human": 0, "draw": 0, "ai": 0}

    while True:
        board   = make_board()
        is_human_turn = human_goes_first
        nodes_last = 0

        while True:
            clear()
            print_header(scores, use_alpha_beta)
            display_board(board)

            result = check_winner(board)
            if result:
                line = winning_line(board)
                display_board(board, highlight=line)
                if result == HUMAN:
                    print(" You win! (Did you find a bug?)")
                    scores["human"] += 1
                elif result == AI:
                    print(" AI wins! Minimax is unbeatable.")
                    scores["ai"] += 1
                else:
                    print(" It's a draw — great play!")
                    scores["draw"] += 1
                break 

            if is_human_turn:
                print("  Your turn (X).")
                move = get_human_move(board)
                board[move] = HUMAN
            else:
                print("  AI is thinking…", end="", flush=True)
                t0 = time.perf_counter()
                move, nodes_last = best_move(board, use_alpha_beta)
                elapsed = time.perf_counter() - t0
                board[move] = AI
                print(f"\r  AI played cell {move+1}  "
                      f"({nodes_last:,} nodes, {elapsed*1000:.1f} ms)   ")

            is_human_turn = not is_human_turn

        # ── after game ──
        print()
        again = input("  Play again? [Y/n]: ").strip().lower()
        if again in ("n", "no"):
            print("\n  Thanks for playing!\n")
            break
        # swap who goes first each game
        human_goes_first = not human_goes_first


# Main menu

def main() -> None:
    clear()
    print("=" * 42)
    print("     TIC-TAC-TOE — Minimax AI  (Python)")
    print("=" * 42)
    print()

    # Alpha-Beta choice
    print("  Algorithm:")
    print("    1. Minimax + Alpha-Beta pruning  (default, fast)")
    print("    2. Minimax only  (slower, same result)")
    ab_choice = input("  Choose [1/2, default=1]: ").strip()
    use_alpha_beta = ab_choice != "2"

    # Who goes first
    print()
    print("  Who goes first?")
    print("    1. Human (X)  [default]")
    print("    2. AI    (O)")
    first_choice = input("  Choose [1/2, default=1]: ").strip()
    human_first  = first_choice != "2"

    print()
    play_game(use_alpha_beta=use_alpha_beta, human_goes_first=human_first)


if __name__ == "__main__":
    main()
