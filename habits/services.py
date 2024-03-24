from django_celery_beat.models import PeriodicTask, \
    IntervalSchedule


def set_schedule(period):
    # Создаем интервал для повтора
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=period,
        period=IntervalSchedule.DAYS,
    )

    # Создаем задачу для повторения
    PeriodicTask.objects.create(
        interval=schedule,
        name='Importing contacts',
        task='habits.tasks.habit_operate',
    )
