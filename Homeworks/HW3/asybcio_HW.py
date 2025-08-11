import asyncio
import time

async def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    await asyncio.sleep(0)
    return True

def find_primes_single_thread(start: int, end: int):
    primes = []
    for n in range(start, end + 1):
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            primes.append(n)
    return primes


async def find_primes_multi_async(start: int, end: int):
    tasks = [is_prime(n) for n in range(start, end + 1)]
    results = await asyncio.gather(*tasks)
    return [n for n, prime in zip(range(start, end + 1), results) if prime]


async def main():
    test_ranges = [
        (1, 10000),
        (1, 100),
        (1, 1000),
        (1, 50000),
        (1, 1000000)
    ]

    for start, end in test_ranges:
        print(f"\nДиапазон: {start} - {end}")

        t1 = time.time()
        primes_single = find_primes_single_thread(start, end)
        print(f"Одиночний: {len(primes_single)} чисел за {time.time() - t1:.2f} сек")

        t2 = time.time()
        primes_multi = await find_primes_multi_async(start, end)
        print(f"Asyncio: {len(primes_multi)} чисел за {time.time() - t2:.2f} сек")

        print("Чи збігаються результати:", primes_single == primes_multi)


if __name__ == "__main__":
    asyncio.run(main())