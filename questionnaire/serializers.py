from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Test, Question, Answer
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AnswerSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Answer
        fields = ['id', 'answer', 'is_true']


class QuestionSerializer(WritableNestedModelSerializer):
    answers = AnswerSerializer(many=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'point', 'answers']


class TestSerializer(WritableNestedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username', read_only=True)
    solved = serializers.ReadOnlyField(read_only=True)
    questions = QuestionSerializer(many=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = Test
        fields = ['id', 'title', 'owner', 'solved', 'questions', ]

    def solved_count(self, obj):
        obj.solved += 1
        obj.save()


class UserSerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['id', 'username', 'tests']
