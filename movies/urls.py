from django.urls import path
from movies.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]