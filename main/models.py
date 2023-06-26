from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver


class Nationality(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name_plural = 'Nationalities'

    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = 'Difficulties'

    def __str__(self):
        return self.name


class Creator(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField(null=True, blank=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    position_in_rating = models.IntegerField()

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=64)
    rating = models.IntegerField(null=True, blank=True)
    nationality = models.ForeignKey(Nationality, on_delete=models.PROTECT)
    position_in_rating = models.IntegerField()

    def __str__(self):
        return self.name


class Demon(models.Model):
    name = models.CharField(max_length=100)
    position = models.IntegerField()
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
    difficulty_as_number = models.IntegerField(null=True, blank=True)
    creators = models.ManyToManyField(Creator)
    completed_by = models.ManyToManyField(Player)

    def __str__(self):
        return self.name


# AUTO-COUNT RATING
# For top 10 players
@receiver(m2m_changed, sender=Demon.completed_by.through)
def update_player_rating(sender, instance, action, pk_set, **kwargs):
    if action in ['post_add', 'post_remove']:
        for player_id in pk_set:
            rating = Demon.objects.filter(completed_by=player_id).aggregate(rating=models.Sum('difficulty_as_number'))['rating']
            Player.objects.filter(pk=player_id).update(rating=rating)


# For top 10 creators
@receiver(m2m_changed, sender=Demon.creators.through)
def update_creator_rating(sender, instance, action, pk_set, **kwargs):
    for player_id in pk_set:
        if action in ['post_add', 'post_remove']:
            rating = Demon.objects.filter(creators=player_id).aggregate(rating=models.Count('creators'))['rating']
            Creator.objects.filter(pk=player_id).update(rating=rating)


# For Demon rating calculations
@receiver(post_save, sender=Demon)
def update_demon_position(sender, instance, **kwargs):
    position = instance.position
    new_difficulty_as_number = 10000 - (100 * position)
    instance.difficulty_as_number = new_difficulty_as_number

# Position for players, creators, demons