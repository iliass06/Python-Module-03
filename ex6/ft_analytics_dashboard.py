if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    players_data = [
            {
                "name": "alice",
                "score": 2300,
                "active": True,
                "achievements": [
                    "first_kill", "level_10", "boss_slayer",
                    "explorer", "pacifist"
                ],
                "region": "north"
            },
            {
                "name": "bob",
                "score": 1800,
                "active": True,
                "achievements": ["first_kill", "level_10"],
                "region": "east"
            },
            {
                "name": "charlie",
                "score": 2150,
                "active": True,
                "achievements": ["first_kill", "boss_slayer", "explorer"],
                "region": "central"
            },
            {
                "name": "diana",
                "score": 2050,
                "active": False,
                "achievements": ["level_10", "explorer"],
                "region": "south"
            }
        ]
    print("\n=== List Comprehension Examples ===")

    high_scores = [
        player["name"] for player in players_data if player["score"] > 2000
    ]
    print(f"High scorers (>2000): {high_scores}")

    scores_doubled = [player["score"] * 2 for player in players_data]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [
        player["name"] for player in players_data if player["active"]
    ]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")

    player_scores = {
        player["name"]: player["score"] for player in players_data
    }
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": sum(1 for player in players_data if player["score"] >= 2300),
        "medium": sum(
            1 for player in players_data if 2000 <= player["score"] < 2300
        ),
        "low": sum(1 for player in players_data if player["score"] < 2000)
    }
    print(f"Score categories: {score_categories}")

    ach_count = {
        player["name"]: len(
            player["achievements"]
        ) for player in players_data if player["active"]
    }
    print(f"Achievement counts: {ach_count}")

    print("\n=== Set Comprehension Examples ===")

    unique_players = {player["name"] for player in players_data}
    print(f"Unique players: {unique_players}")

    unique_ach = {
        ach for player in players_data for ach in player["achievements"]
    }
    print(f"Unique achievements: {unique_ach}")

    active_reg = {
        player["region"] for player in players_data if player["active"]
    }
    print(f"Active regions: {active_reg}")

    print("\n=== Combined Analysis ===")

    total = len(players_data)
    print(f"Total players: {total}")
    print(f"Total unique achievements: {len(unique_ach)}")
    sum_scores = sum(player["score"] for player in players_data)
    print(f"Average score: {(sum_scores / total):.1f}")
    max_score = max(player["score"] for player in players_data)
    top_player = [
        player for player in players_data if player["score"] == max_score
    ][0]
    print(f"Top performer: {top_player['name']} ({top_player['score']} "
          f"points, {len(top_player['achievements'])} achievements)")
