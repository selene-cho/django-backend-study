from django.db import models

# Class => Lecture(수업)
# - 강사 (teacher) / CharField
# - 과목 (subject) / CharField
# - 시간 (lecturetime) / DateTimeField
# - 교제 (book) / CharField

class Lecture(models.Model):
    teacher = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    lecturetime = models.DateTimeField()
    book = models.CharField(max_length=20)