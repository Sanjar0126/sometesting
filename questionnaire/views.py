from rest_framework import viewsets
from .serializers import UserSerializer, TestSerializer, QuestionSerializer, AnswerSerializer
from django.contrib.auth.models import User
from .models import Question, Test, Answer
from rest_framework import permissions
from questionnaire.permissions import IsOwnerOrReadOnly, AnonCanGetList


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['indent'] = 4
        return context


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [AnonCanGetList, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_renderer_context(self):
        context = super().get_renderer_context()
        context['indent'] = 4
        return context

# class TestList(generics.ListCreateAPIView):
#     queryset=Test.objects.all()
#     serializer_class=TestSerializer
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#     def get_renderer_context(self):
#         context = super().get_renderer_context()
#         context['indent'] = 4
#         return context

# class TestDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Test.objects.all()
#     serializer_class=TestSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     def get_renderer_context(self):
#         context = super().get_renderer_context()
#         context['indent'] = 4
#         return context
