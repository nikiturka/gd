from django.contrib import admin
from .models import Difficulty, Demon, Player, Nationality, Creator

admin.site.register(Demon)
admin.site.register(Difficulty)
admin.site.register(Player)
admin.site.register(Creator)
admin.site.register(Nationality)
