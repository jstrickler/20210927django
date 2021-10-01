from django.db import models

class TimeOfDay(models.Model):
    timeofday = models.CharField(max_length=32)

    def __str__(self):
        return self.timeofday


class Greeting(models.Model):
    greeting = models.CharField(max_length=32)
    timeofday = models.ForeignKey('TimeOfDay', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.greeting} ({self.timeofday})"


