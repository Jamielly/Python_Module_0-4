#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    initial_players: list[str] = [
        "Alice", "bob",
        "Charlie", "dylan",
        "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {initial_players}")

    capitalized_players: list[str] = [
        name.capitalize() for name in initial_players
    ]
    print(f"New list with all names capitalized: {capitalized_players}")

    already_capitalized: list[str] = [
        name for name in initial_players if name and name.isupper()
    ]
    print(f"New list of capitalized names only: {already_capitalized}")

    random.seed(42)
    score_dict: dict[str, int] = {
        name: random.randint(50, 1000) for name in capitalized_players
    }
    print(f"Score dict: {score_dict}")

    total_score = sum(score_dict.values())
    total_players = len(score_dict)
    average_score: float = total_score / total_players if total_players > 0 else 0.0
    print(f"Score average is {round(average_score, 2)}")

    high_scores: dict[str, int] = {
        name: score for name,
        score in score_dict.items() if score > average_score
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()