import random
import typing


def gen_event(players, actions) -> typing.Generator[str, None, None]:
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events):
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        print("Got event from list: " + str(event))
        print("Got event from list: " + str(events))
        yield event


def main():
    print("=== Game Data Stream Processor ===")
    players = ["Alice", "Bob", "Charlie", "dylan"]
    actions  = ["run", "jump", "move", "grab", "climb", "swim", "eat", "sleep", "use", "release"]
    event_gen = gen_event(players, actions)
    for i in range(999):
        name, action = next(event_gen)
        print(f"Event {i}: Player '{name}' did action '{action}'")
    event_list = [next(event_gen) for _ in range(10)]
    print("Built list of 10 events: " + str(event_list))
    for event in consume_event(event_list):
        pass
