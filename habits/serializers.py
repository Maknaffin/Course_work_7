from rest_framework import serializers

from habits.models import Habit
from habits.validators import RewardAndHabitValidator, ActionTimeValidator, IsNiceValidator, NiceHabitValidator, \
    PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardAndHabitValidator(reward='reward', associated_habit='associated_habit'),
            ActionTimeValidator(action_time='action_time'),
            IsNiceValidator(associated_habit='associated_habit'),
            NiceHabitValidator(is_nice='is_nice', reward='reward', associated_habit='associated_habit'),
            PeriodValidator(period='period')
        ]
