from django.contrib import admin

from .models import Lesson, Course, CourseSubscription


class LessonsInline(admin.TabularInline):
    model = Lesson
    extra = 1


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [LessonsInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'video', 'course')


class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'timestamp')


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseSubscription, CourseSubscriptionAdmin)
