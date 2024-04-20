from django.urls import include, path
from rest_framework import routers

from .views import UsersViewSet


router = routers.DefaultRouter()
router.register('userslist', UsersViewSet)


urlpatterns = [
    path('', include(router.urls)),
]