import generics as generics
from django.forms import model_to_dict
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Player, Nationality, Creator, Demon, Difficulty
from main.serializers import PlayerSerializer, NationalitySerializer, DifficultySerializer, CreatorSerializer,\
DemonSerializer, DemonSerializerShort


class NationalityListCreate(generics.ListCreateAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class NationalityUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class PlayerListCreate(APIView):
    def get(self, request):
        players = Player.objects.all()
        players_serialized = PlayerSerializer(players, many=True)

        return Response(players_serialized.data)

    def post(self, request):
        new_player = Player.objects.create(
            name=request.data["name"],
            rating=request.data["rating"],
            nationality=Nationality.objects.get(pk=request.data.get("nationality"))
        )

        return Response(model_to_dict(new_player))


class PlayerUpdateDestroy(APIView):
    def get(self, request, pk):
        player = Player.objects.get(pk=pk)
        player_serialized = PlayerSerializer(player)
        return Response(player_serialized.data)

    def put(self, request, pk):
        player = Player.objects.get(pk=pk)
        fields_to_update = request.data

        for key, value in fields_to_update.items():
            if key != 'nationality':
                setattr(player, key, value)
            else:
                nationality = Nationality.objects.get(pk=request.data["nationality"])
                setattr(player, key, nationality)

        player.save()

        player_serialized = PlayerSerializer(player)

        return Response(player_serialized.data)

    def delete(self, request, pk):
        player = Player.objects.get(pk=pk)
        player.delete()

        return Response({'Deleted player: ': player.name})


class PlayersTop10(APIView):
    def get(self, request):
        players = Player.objects.order_by('-rating')
        players_serialized = PlayerSerializer(players, many=True)

        return Response(players_serialized.data)


class CreatorListCreate(APIView):
    def get(self, request):
        creators = Creator.objects.all()
        creators_serialized = CreatorSerializer(creators, many=True)

        return Response(creators_serialized.data)

    def post(self, request):
        new_creator = Creator.objects.create(
            name=request.data["name"],
            rating=request.data["rating"],
            nationality=Nationality.objects.get(pk=request.data.get("nationality"))
        )

        return Response(model_to_dict(new_creator))


class CreatorUpdateDestroy(APIView):
    def get(self, request, pk):
        creator = Creator.objects.get(pk=pk)
        creator_serialized = CreatorSerializer(creator)
        return Response(creator_serialized.data)

    def put(self, request, pk):
        creator = Creator.objects.get(pk=pk)
        fields_to_update = request.data

        for key, value in fields_to_update.items():
            if key != 'nationality':
                setattr(creator, key, value)
            else:
                nationality = Nationality.objects.get(pk=request.data["nationality"])
                setattr(creator, key, nationality)

        creator.save()

        creator_serialized = CreatorSerializer(creator)

        return Response(creator_serialized.data)

    def delete(self, request, pk):
        creator = Creator.objects.get(pk=pk)
        creator.delete()

        return Response({'Deleted creator: ': creator.name})


class CreatorsTop10(APIView):
    def get(self, request):
        creators = Creator.objects.order_by('-rating')
        creators_serialized = CreatorSerializer(creators, many=True)

        return Response(creators_serialized.data)


class DemonTop(APIView):
    def get(self, request):
        demons = Demon.objects.all().order_by('-difficulty_as_number')
        url = request.get_full_path()

        if '/top-short/' in url:
            demons_serialized = DemonSerializerShort(demons, many=True)
        else:
            demons_serialized = DemonSerializer(demons, many=True)

        return Response(demons_serialized.data)

    def post(self, request):
        new_demon = Demon.objects.create(
            name=request.data["name"],
            position=request.data["position"],
            difficulty=Difficulty.objects.get(pk=request.data["difficulty"]),
        )

        creators = request.data["creators"]

        for creator_id in creators:
            creator = Creator.objects.get(pk=creator_id)
            new_demon.creators.add(creator)

        completed_by = request.data["completed_by"]

        for player_id in completed_by:
            player = Player.objects.get(pk=player_id)
            new_demon.completed_by.add(player)

        new_demon.save()

        new_demon_serialized = DemonSerializer(new_demon)

        return Response(new_demon_serialized.data)


class DemonUpdateDestroy(APIView):
    def get(self, request, pk):
        demon = Demon.objects.get(pk=pk)
        demons_serialized = DemonSerializer(demon)

        return Response(demons_serialized.data)

    def put(self, request, pk):
        demon = Demon.objects.get(pk=pk)
        fields_to_update = request.data

        for key, value in fields_to_update.items():
            if key != 'creators' and key != 'completed_by' and key != 'difficulty':
                setattr(demon, key, value)

            elif key == 'difficulty':
                difficulty = Difficulty.objects.get(pk=request.data["difficulty"])
                setattr(demon, key, difficulty)

            elif key == 'creators':
                for creator in demon.creators.all():
                    demon.creators.remove(creator)

                for creator_id in value:
                    creator = Creator.objects.get(pk=creator_id)

                    demon.creators.add(creator)

            elif key == 'completed_by':
                for player in demon.completed_by.all():
                    demon.completed.remove(player)

                for player_id in value:
                    player = Player.objects.get(pk=player_id)

                    demon.completed_by.add(player)

        demon.save()

        demon_serialized = DemonSerializer(demon)

        return Response(demon_serialized.data)

    def delete(self, request, pk):
        demon = Demon.objects.get(pk=pk)
        demon.delete()

        return Response({"Deleted demon: ": demon.name})
