from django.contrib import admin
from nested_admin.nested import NestedModelAdmin, NestedTabularInline
from .models import Test,Question,Answer

class AnswerInLine(NestedTabularInline):
    model=Answer
    extra=3

class QuestionInLine(NestedTabularInline):
    model=Question
    extra=1
    inlines=[AnswerInLine]


class TestAdmin(NestedModelAdmin):
    fieldsets=[
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['created_at']}),
        ('User', {'fields': ['owner']}),
    ]
    list_display=['title','owner','created_at']
    inlines=[QuestionInLine]
    list_filter=['created_at']
    search_fields = ['title']
    

admin.site.register(Test,TestAdmin)
# admin.site.register(Question)
# admin.site.register(Answer)

