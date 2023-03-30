from django.urls import path
from .views import home, registration_view, logout_view


urlpatterns = [
    path('', home, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
]