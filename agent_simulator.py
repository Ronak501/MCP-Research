import asyncio
import httpx
import random
import time

SERVER_URL = "http://127.0.0.1:8000"
latencies = []
errors = 0


async def simulated_agent(agent_id):

    async with httpx.AsyncClient() as client:

        await asyncio.sleep(random.uniform(0.1, 1.5))

        choice = random.choice(["calculator", "weather"])

        try:

            if choice == "calculator":

                a = random.randint(1, 100)
                b = random.randint(1, 100)

                start = time.perf_counter()

                await client.get(
                    f"{SERVER_URL}/add",
                    params={"a": a, "b": b}
                )

                latency = time.perf_counter() - start
                latencies.append(latency)

            else:

                city = random.choice(["Delhi", "Surat", "Mumbai", "Ahmedabad"])

                start = time.perf_counter()

                await client.get(
                    f"{SERVER_URL}/weather",
                    params={"city": city}
                )

                latency = time.perf_counter() - start
                latencies.append(latency)

        except Exception:
            global errors
            errors += 1


async def run_agents(num_agents=100):

    start_test = time.perf_counter()

    tasks = [simulated_agent(i) for i in range(num_agents)]
    await asyncio.gather(*tasks)

    end_test = time.perf_counter()

    total_time = end_test - start_test

    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    max_latency = max(latencies) if latencies else 0

    throughput = num_agents / total_time

    print("\n===== Benchmark Results =====")
    print(f"Agents: {num_agents}")
    print(f"Total time: {total_time:.2f}s")
    print(f"Average latency: {avg_latency:.3f}s")
    print(f"Max latency: {max_latency:.3f}s")
    print(f"Throughput: {throughput:.2f} req/sec")
    print(f"Errors: {errors}")


if __name__ == "__main__":
    asyncio.run(run_agents(100))