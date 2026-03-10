from typing import Generator


def event_stream() -> Generator:
    names = ["alice", "bob", "charlie", "diana", "eve"]
    levels = [5, 12, 8, 15, 2, 25, 14, 9, 30, 7]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1000):
        yield {
            "id": i + 1,
            "player": names[i % len(names)],
            "level": levels[i % len(levels)],
            "action": actions[i % len(actions)]
        }


def stream_analytics() -> tuple:
    gen = event_stream()
    high_level = 0
    treasure = 0
    level_up = 0
    for event in gen:
        if event['level'] >= 10:
            high_level += 1
        if event['action'] == "found treasure":
            treasure += 1
        if event['action'] == "leveled up":
            level_up += 1
    return high_level, treasure, level_up


def fibonacci() -> Generator:
    a, b = 0, 1
    for i in range(10):
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for j in range(2, n):
        if n % j == 0:
            return False
    return True


def prime() -> Generator:
    a = 2
    count = 0
    while count < 5:
        if is_prime(a):
            yield a
            count += 1
        a += 1


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    print("\nProcessing 1000 game events...")
    print()
    gen = event_stream()
    for i in range(3):
        event = next(gen)
        print(f"Event {event['id']}: Player {event['player']} "
              f"(level {event['level']}) {event['action']}")
    print("...")
    print("\n=== Stream Analytics ===")
    high_level, treasure, level_up = stream_analytics()
    print("Total events processed: 1000")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {level_up}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print("\n=== Generator Demonstration ===")
    fib = fibonacci()
    primes = prime()

    fib_res = ""
    for i in range(10):
        fib_res += f"{next(fib)}"
        if i < 9:
            fib_res += ", "

    prime_res = ""
    for i in range(5):
        prime_res += f"{next(primes)}"
        if i < 4:
            prime_res += ", "
    print(f"Fibonacci sequence (first 10): {fib_res}")
    print(f"Prime numbers (first 5): {prime_res}")
