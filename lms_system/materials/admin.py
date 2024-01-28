from django.contrib import admin

from .models import Lesson, Course


class LessonsInline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [LessonsInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'video', 'course')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)