from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Creator(models.Model):
    name = models.CharField(max_length=64)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Demon(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    difficulty_as_number = models.DecimalField(max_digits=6, decimal_places=2)
    verifier = models.ForeignKey(Player, on_delete=models.PROTECT)
    creators = models.ManyToManyField(Creator)

    def __str__(self):
        return self.name
