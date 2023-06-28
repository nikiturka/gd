from django.urls import path, include
from main.views import *

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('api/v1/nationalities', NationalityListCreate.as_view()),
    path('api/v1/nationalities/<int:pk>', NationalityUpdateDestroy.as_view()),
    path('api/v1/difficulties', DifficultyListCreate.as_view()),
    path('api/v1/difficulties/<int:pk>', DifficultyUpdateDestroy.as_view()),
    path('api/v1/players', PlayerListCreate.as_view()),
    path('api/v1/players/<int:pk>', PlayerUpdateDestroy.as_view()),
    path('api/v1/players/top10', PlayersTop10.as_view()),
    path('api/v1/creators', CreatorListCreate.as_view()),
    path('api/v1/creators/<int:pk>', CreatorUpdateDestroy.as_view()),
    path('api/v1/creators/top10', CreatorsTop10.as_view()),
    path('api/v1/demons/top', DemonTop.as_view()),
    path('api/v1/demons/top-short/', DemonTop.as_view()),
    path('api/v1/demons/<int:pk>', DemonUpdateDestroy.as_view()),
]
