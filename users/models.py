from django.db import models

# User (학생정보)
# - 이름 (CharField)
# - 나이 (PositiveInteger) 나이는 양수니까!
# - 성별 (CharField)
# - 수업데이터 () => Lecture

class User(models.Model):
  name = models.CharField(max_length=20)
  age = models.PositiveIntegerField()
  gender = models.CharField(max_length=20)