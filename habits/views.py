from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер создания привычки для авторизованного пользователя"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Контроллер вывода списка привычек авторизованного пользователя"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitAllAPIView(generics.ListAPIView):
    """Контроллер вывода списка публичных привычек для авторизованного пользователя"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.all().filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер вывода привычки авторизованного пользователя"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер редактирования привычки авторизованного пользователя"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """Контроллер удаления привычки авторизованного пользователя"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
