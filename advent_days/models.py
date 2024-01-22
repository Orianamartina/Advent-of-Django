from django.db import models
# Create your models here.
class Day(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)

class Language(models.Model):
    name = models.CharField(max_length=100)

class DayResolution(models.Model):
    id = models.IntegerField(primary_key = True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    answer_part_one = models.CharField(max_length=1000)
    answer_part_two = models.CharField(max_length=1000)
    input = models.TextField()
    user = models.ForeignKey('adventapi.CustomUser', on_delete=models.CASCADE)
    code = models.CharField(max_length=100000)
    description = models.TextField()
    comments_quantity = models.IntegerField(default=0)
    link_to_repo = models.CharField(max_length=200, default="none")
    likes = models.IntegerField(default=0)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.user)  + "_day_" +str(self.day)