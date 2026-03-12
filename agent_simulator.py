import asyncio
import httpx
import random
import time

SERVER_URL = "http://127.0.0.1:8000"


async def simulated_agent(agent_id):

    async with httpx.AsyncClient() as client:

        await asyncio.sleep(random.uniform(0.1, 1.5))

        choice = random.choice(["calculator", "weather"])

        try:

            if choice == "calculator":

                a = random.randint(1, 100)
                b = random.randint(1, 100)

                start = time.time()

                response = await client.get(
                    f"{SERVER_URL}/add",
                    params={"a": a, "b": b}
                )

                latency = time.time() - start

                print(f"Agent {agent_id} → add({a},{b}) → {response.json()}")
                print(f"Agent {agent_id} latency: {latency:.3f}s")

            else:

                city = random.choice(["Delhi", "Surat", "Mumbai", "Ahmedabad"])

                start = time.time()

                response = await client.get(
                    f"{SERVER_URL}/weather",
                    params={"city": city}
                )

                latency = time.time() - start

                print(f"Agent {agent_id} → weather({city}) → {response.json()}")
                print(f"Agent {agent_id} latency: {latency:.3f}s")

        except Exception as e:
            print(f"Agent {agent_id} error: {e}")


async def run_agents(num_agents=100):

    tasks = [simulated_agent(i) for i in range(num_agents)]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(run_agents(500))