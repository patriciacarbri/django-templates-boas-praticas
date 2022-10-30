from django.urls import path
from galeria.views import index

#Lista dos endpoints
urlpatterns = [
    path('', index)
]

