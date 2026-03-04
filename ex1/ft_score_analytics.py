import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    list = []
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            while i < len(sys.argv):
                list.append(int(sys.argv[i]))
                i += 1
            print(f"Scores processed: {list}")
            print(f"Total players: {len(list)}")
            print(f"Total score: {sum(list)}")
            print(f"Average score: {sum(list) / len(list)}")
            print(f"High score: {max(list)}")
            print(f"Low score: {min(list)}")
            print(f"Score range: {max(list) - min(list)}")
        except ValueError:
            print("please enter an valid inputs (numeric values)")
    