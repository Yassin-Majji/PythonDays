def ft_index(lst: list, value: str) -> int:
    i = 0
    while i < len(lst):
        if lst[i] == value:
            return i
        i += 1


def main() -> None:
    print("=== Game Analytics Dashboard ===\n")
    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    activity = [True, True, True, False]
    achievements = {
        "alice": ["first_kill", "level_10", "boss_slayer", "treasure_hunter",
                  "speed_demon"],
        "bob": ["first_kill", "level_10", "collector"],
        "charlie": ["first_kill", "level_10", "boss_slayer", "speed_demon",
                    "treasure_hunter", "arena_winner", "explorer"],
        "diana": ["first_kill", "level_10"]
    }

    print("=== List Comprehension Examples ===")
    high_scores = [player for player in players
                   if scores[ft_index(players, player)] > 2000]
    print(f"High scorers (>2000): {high_scores}")
    scores_doubled = [i * 2 for i in scores]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [player for player in players
                      if activity[ft_index(players, player)]]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {key: scores[ft_index(players, key)] for key in players}
    print(f"Active players: {player_scores}")
    score_categories = {
        "high": len([s for s in scores if s > 2100]),
        "medium": len([s for s in scores if 2000 <= s <= 2100]),
        "low": len([s for s in scores if s < 2000])
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {key: len(achievements[key]) for key in achievements}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    players2 = ["alice", "bob", "charlie", "diana", "alice", "bob",
                "charlie", "diana"]
    achievements2 = ["first_kill", "level_10", "boss_slayer", "speed_demon",
                     "treasure_hunter", "arena_winner", "explorer",
                     "first_kill", "level_10", "boss_slayer",
                     "treasure_hunter", "speed_demon"]

    unique_players = {player for player in players2}
    unique_achievements = {achievement for achievement in achievements2}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    regions = ["north", "east", "north", "central"]
    regions_activity = [True, True, False, True]
    active_regions = {region for region in regions
                      if regions_activity[ft_index(regions, region)]}
    print(f"Active regions: {active_regions}")
    print("\n=== Combined Analysis ===")

    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {sum(scores)/len(scores)}")
    top_score = max(scores)
    top_player = players[ft_index(scores, top_score)]

    top_achievements = len(achievements[top_player])
    print(f"Top performer: {top_player} ({top_score} points, "
          f"{top_achievements} achievements)")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
