def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = ["alice", "bob", "charlie"]
    achievemnts = [{'first_kill', 'level_10', 'treasure_hunter',
                    'speed_demon'},
                   {'first_kill', 'level_10', 'boss_slayer', 'collector'},
                   {'level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist'}]
    size = len(players)

    players_achievement = {}
    i = 0
    while i < size:
        players_achievement[players[i]] = achievemnts[i]
        i += 1
    i = 0
    while (i < size):
        print(f"Player {players[i]} achievements: {achievemnts[i]}")
        i += 1
    print()

    print("=== Achievement Analytics ===")
    unique_achievements = achievemnts[0]
    i = 1
    while (i < size):
        unique_achievements = unique_achievements.union(achievemnts[i])
        i += 1
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print()

    common_achievements = achievemnts[0]
    i = 1
    while (i < size):
        common_achievements = common_achievements.intersection(achievemnts[i])
        i += 1
    print(f"Common to all players: {common_achievements}")
    rare_achievements = set()

    i = 0
    while (i < size):
        rare = achievemnts[i]
        j = 0
        while (j < size):
            if (j == i):
                j += 1
                continue
            rare = rare.difference(achievemnts[j])
            j += 1
        rare_achievements = rare_achievements.union(rare)
        i += 1

    print("Rare achievements (1 player): ", rare_achievements)
    print()

    player1 = "alice"
    player2 = "bob"
    common = players_achievement[player1].intersection(
        players_achievement[player2])
    print(f"Alice vs Bob common:{common}")

    unique = players_achievement[player1].difference(
        players_achievement[player2])
    print(f"Alice unique: {unique}")

    unique = players_achievement[player2].difference(
        players_achievement[player1])
    print(f"Bob unique: {unique}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
