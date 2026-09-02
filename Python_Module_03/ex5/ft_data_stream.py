#!/usr/bin/env python3
import random
import typing

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    while True:
        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        random_index = random.randrange(len(event_list))
        selected_event = event_list.pop(random_index)
        yield selected_event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    ten_events = [next(event_generator) for _ in range(10)]
    print(f"\nCreated a list of 10 events: {ten_events}")

    print("\nConsuming events randomly:")
    for player, action in consume_event(ten_events):
        print(f"Consumed Event: Player {player} did action {action}")

    print(f"\nRemaining list size: {len(ten_events)}")


if __name__ == "__main__":
    main()
