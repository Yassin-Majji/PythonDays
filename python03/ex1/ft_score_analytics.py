import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    size = len(sys.argv)
    if (size < 2):
        print(f"No scores provided. Usage: python3 {sys.argv[0]}"
              " <score1> <score2> ...")
        return
    scores_list = []
    i = 1
    try:
        while (i < size):
            score_number = int(sys.argv[i])
            scores_list += [score_number]
            i += 1
    except ValueError:
        print("Error: You must enter a valid number as a score!!!")
        return
    print(f"Scores processed: {scores_list}")
    print(f"Total players: {size - 1}")
    total_scores = sum(scores_list)
    max_scores = max(scores_list)
    min_scores = min(scores_list)
    print(f"Total score: {total_scores}")
    print(f"Average score: {total_scores / (size - 1)}")
    print(f"High score: {max_scores}")
    print(f"Low score: {min_scores}")
    print(f"Score range: {max_scores - min_scores}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
