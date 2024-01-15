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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.CharField(max_length=40)
    code = models.CharField(max_length=100000)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)  + "_day_" +str(self.day)

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    text = models.CharField(max_length=1000)
    resolution = models.ForeignKey(DayResolution, on_delete=models.CASCADE)

class RecentResolutions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resolution = models.ForeignKey(DayResolution, on_delete=models.CASCADE)