from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Player, Nationality, Creator, Demon, Difficulty
from main.serializers import PlayerSerializer, NationalitySerializer, DifficultySerializer, CreatorSerializer,\
DemonSerializer

# NATIONALITY ENDPOINTS


# Create + Read
class NationalityListCreate(APIView):
    def get(self, request):
        nationalities = Nationality.objects.all()
        nationalities_serialized = NationalitySerializer(nationalities, many=True)

        return Response(nationalities_serialized.data)

    def post(self, request):
        new_nationality = Nationality.objects.create(
            name=request.data["name"]
        )

        return Response(model_to_dict(new_nationality))


# Update + Delete
class NationalityUpdateDestroy(APIView):
    def get(self, request, pk):
        nationality = Nationality.objects.get(pk=pk)
        nationality_serialized = NationalitySerializer(nationality)

        return Response(nationality_serialized.data)

    def put(self, request, pk):
        nationality = Nationality.objects.get(pk=pk)
        fields_to_update = request.data

        for key, value in fields_to_update.items():
            setattr(nationality, key, value)

        nationality.save()

        nationality_serialized = NationalitySerializer(nationality)

        return Response(nationality_serialized.data)

    def delete(self, request, pk):
        nationality = Nationality.objects.get(pk=pk)
        nationality_name = nationality.name

        nationality.delete()

        return Response({'Deleted object:' + nationality_name})


class DifficultyListCreate(APIView):
    def get(self, request):
        difficultes = Difficulty.objects.all()
        difficultes_serialized = DifficultySerializer(difficultes, many=True)

        return Response(difficultes_serialized.data)

    def post(self, request):
        new_difficulty = Difficulty.objects.create(
            name=request.data["name"]
        )

        return Response(model_to_dict(new_difficulty))


# Update + Delete
class DifficultyUpdateDestroy(APIView):
    def get(self, request, pk):
        difficulty = Difficulty.objects.get(pk=pk)
        difficulty_serialized = DifficultySerializer(difficulty)

        return Response(difficulty_serialized.data)

    def put(self, request, pk):
        difficulty = Difficulty.objects.get(pk=pk)
        fields_to_update = request.data

        for key, value in fields_to_update.items():
            setattr(difficulty, key, value)

        difficulty.save()

        difficulty_serialized = DifficultySerializer(difficulty)

        return Response(difficulty_serialized.data)

    def delete(self, request, pk):
        difficulty = Difficulty.objects.get(pk=pk)
        difficulty_name = difficulty.name

        difficulty.delete()

        return Response({'Deleted object:' + difficulty_name})


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
