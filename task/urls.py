from django.contrib import admin
from django.urls import path, include
from users.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/', include('users.api_urls')),
]
