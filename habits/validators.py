from rest_framework.exceptions import ValidationError


class RewardAndHabitValidator:
    def __init__(self, reward, associated_habit):
        self.reward = reward
        self.associated_habit = associated_habit

    def __call__(self, value):
        reward = dict(value).get(self.reward)
        associated_habit = dict(value).get(self.associated_habit)
        if reward and associated_habit:
            raise ValidationError('Нельзя одновременно выбирать связанную привычку и вознаграждение')


class ActionTimeValidator:
    def __init__(self, action_time):
        self.action_time = action_time

    def __call__(self, value):
        action_time = dict(value).get(self.action_time)
        if action_time > 120:
            raise ValidationError('Время выполнения привычки не должно быть больше 120 секунд')


class IsNiceValidator:
    def __init__(self, associated_habit):
        self.associated_habit = associated_habit

    def __call__(self, value):
        if value.get(self.associated_habit):
            is_nice = dict(value).get(self.associated_habit).is_nice
            if not is_nice:
                raise ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки')


class NiceHabitValidator:
    def __init__(self, is_nice, reward, associated_habit):
        self.is_nice = is_nice
        self.reward = reward
        self.associated_habit = associated_habit

    def __call__(self, value):
        is_nice = dict(value).get(self.is_nice)
        reward = dict(value).get(self.reward)
        associated_habit = dict(value).get(self.associated_habit)
        if is_nice:
            if reward or associated_habit:
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodValidator:
    def __init__(self, period):
        self.period = period

    def __call__(self, value):
        period = dict(value).get(self.period)
        if period < 1:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
