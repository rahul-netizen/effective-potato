import asyncio

from taskiq_redis import RedisAsyncResultBackend, RedisStreamBroker

redis_url = "redis://localhost:6379"
result_backend = RedisAsyncResultBackend(redis_url=redis_url, result_ex_time=1000)
broker = RedisStreamBroker(url=redis_url).with_result_backend(result_backend)


@broker.task
async def best_task_ever_to_exist():
    await asyncio.sleep(5)
    print("This task has gone the ways of dodo")


async def main():
    task = await best_task_ever_to_exist.kiq()
    print(await task.wait_result())


if __name__ == "__main__":
    asyncio.run(main())
