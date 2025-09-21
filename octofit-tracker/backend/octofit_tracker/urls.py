"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import TeamViewSet, UserViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
from urllib.parse import urljoin

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'users', UserViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    # Prefer a Codespaces-hosted URL using the environment variable CODESPACE_NAME
    # e.g. https://$CODESPACE_NAME-8000.app.github.dev/
    codespace = os.environ.get('CODESPACE_NAME')
    if codespace:
        base = f"https://{codespace}-8000.app.github.dev/api/"
        # use urljoin to safely append paths
        return Response({
            'teams': urljoin(base, 'teams/'),
            'users': urljoin(base, 'users/'),
            'activities': urljoin(base, 'activities/'),
            'workouts': urljoin(base, 'workouts/'),
            'leaderboard': urljoin(base, 'leaderboard/'),
        })

    # Fallback to request-built absolute URIs (works on localhost or tunneled envs)
    return Response({
        'teams': request.build_absolute_uri('teams/'),
        'users': request.build_absolute_uri('users/'),
        'activities': request.build_absolute_uri('activities/'),
        'workouts': request.build_absolute_uri('workouts/'),
        'leaderboard': request.build_absolute_uri('leaderboard/'),
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include(router.urls)),
    path('', api_root),
]
