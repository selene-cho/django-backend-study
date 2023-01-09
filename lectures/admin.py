from django.contrib import admin
from .models import Lecture

# Register your models here.

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
  list_display = ("teacher", "subject", "lecturetime", "book")
