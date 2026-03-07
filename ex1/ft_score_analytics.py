import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    i = 1
    score_list = []
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            while i < len(sys.argv):
                score_list.append(int(sys.argv[i]))
                i += 1
            print(f"Scores processed: {score_list}")
            print(f"Total players: {len(score_list)}")
            print(f"Total score: {sum(score_list)}")
            print(f"Average score: {sum(score_list) / len(score_list)}")
            print(f"High score: {max(score_list)}")
            print(f"Low score: {min(score_list)}")
            print(f"Score range: {max(score_list) - min(score_list)}")
        except ValueError:
            print("please enter an valid inputs (only numeric values)")
