from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Day(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)

class DayResolution(models.Model):
    id = models.IntegerField(primary_key = True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    answer_part_one = models.CharField(max_length=1000)
    answer_part_two = models.CharField(max_length=1000)
    input = models.TextField()
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.day)

