#!/usr/bin/env python3
import random

ACHIEVEMENTS_POOL = [
    "First Steps",
    "Master Explorer",
    "Treasure Hunter",
    "Boss Slayer",
    "Crafting Genius",
    "Collector Supreme",
    "Untouchable",
    "Unstoppable",
    "World Savior",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:

    num_achievements = random.randint(5, 9)
    selected = random.sample(ACHIEVEMENTS_POOL, num_achievements)
    return set(selected)


def main() -> None:
    print("=== Achievement Tracker System ===")

    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")

    all_unlocked: set[str] = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_unlocked}")

    common_achievements: set[str] = set(players["Alice"]).intersection(
        players["Bob"], players["Charlie"], players["Dylan"]
    )
    print(f"Common achievements: {common_achievements}\n")

    for name, achievements in players.items():
        other_players_union = set().union(
            *(p_set for p_name, p_set in players.items() if p_name != name)
        )
        exclusive = achievements.difference(other_players_union)
        print(f"Only {name} has: {exclusive}")

    print()

    pool_set = set(ACHIEVEMENTS_POOL)
    for name, achievements in players.items():
        missing = pool_set.difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
