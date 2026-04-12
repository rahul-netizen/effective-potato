from taskiq import TaskiqScheduler
from taskiq_redis import (
    ListRedisScheduleSource,
    RedisAsyncResultBackend,
    RedisStreamBroker,
    ListQueueBroker
)

# Here's the broker that is going to execute tasks
redis_url = "redis://localhost:6379"
result_backend = RedisAsyncResultBackend(redis_url=redis_url, result_ex_time=1000)
broker = RedisStreamBroker(url=redis_url).with_result_backend(result_backend)


# broker = ListQueueBroker(f"{redis_url}/0")

# Here's the source that is used to store scheduled tasks
redis_source = ListRedisScheduleSource(url=redis_url)

# And here's the scheduler that is used to query scheduled sources
scheduler = TaskiqScheduler(broker=broker, sources=[redis_source])

@broker.task
async def my_task(arg1: str, arg2: str) -> str:
    print(f"These are my args : {arg1} & {arg2}")



async def main():
    await redis_source.startup()
    await my_task.schedule_by_cron(redis_source, "Hello", arg2=", world !", cron="*/5 * * * *")
    # await my_task.kicker
