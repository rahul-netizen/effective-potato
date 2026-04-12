from tasks import broker


@broker.task
async def worst_task_ever():
    print("I am the wrost tas ever")
