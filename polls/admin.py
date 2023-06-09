from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['qu_text']}),
        ('Date info', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]
    list_display = 'qu_text', 'pub_date', 'was_published_recently'
    list_filter = ['pub_date']
    search_fields = ['qu_text']


admin.site.register(Question, QuestionAdmin)
