from rest_framework import serializers
from main.models import Player, Creator, Demon, Nationality, Difficulty


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'


class DemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demon
        fields = '__all__'
