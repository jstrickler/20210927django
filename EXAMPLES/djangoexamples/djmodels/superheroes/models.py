from django.db import models

class Power(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name

# for DB views...
class Spam(models.Model):
    id = models.IntegerField()
    barf = models.CharField(max_length=16)
    blub = models.IntegerField()
    grutz = models.ForeignKey('OtherTable', on_delete=models.DO_NOTHING)

    class Meta:
        managed=False
        db_table = 'name_of_actual_view'

class City(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Enemy(models.Model):
    name = models.CharField(max_length=32, unique=True)
    powers = models.ManyToManyField(Power)

    def __str__(self):
        return self.name

class Superhero(models.Model):
    name = models.CharField(max_length=32, unique=True)
    real_name = models.CharField(max_length=32)
    secret_identity = models.CharField(max_length=32)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    powers = models.ManyToManyField(Power)
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name


