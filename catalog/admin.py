from django.contrib import admin

# Register your models here.
from .models import Category, Teacher, Location, Age_recommend, Duration, Course

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Age_recommend)
class Age_recommendAdmin(admin.ModelAdmin):
    pass

@admin.register(Duration)
class DurationAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'display_category', 'display_age_recommend', 'duration', 'teacher')
    pass


