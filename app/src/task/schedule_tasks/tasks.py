from taskiq import TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource
# from tasks import broker
from taskiq_redis import RedisAsyncResultBackend, RedisStreamBroker

redis_url = "redis://localhost:6379"
result_backend = RedisAsyncResultBackend(redis_url=redis_url, result_ex_time=1000)
broker = RedisStreamBroker(url=redis_url).with_result_backend(result_backend)

scheduler = TaskiqScheduler(broker=broker, sources=[LabelScheduleSource(broker)])


@broker.task(schedule=[{"cron": "*/5 * * * *", "args": [42]}])
async def time_light_task(value: int) -> int:
    print(f"I got value of : {value}")
    return value + 1
