from django.urls import path
from .views import ListUser, UserRetrieveUpdateDestroyAPIView

urlpatterns = [

    path("users/", ListUser.as_view()),
    path("users/<int:pk>/", UserRetrieveUpdateDestroyAPIView.as_view()),

]

''' 
Plural mejor que singular, para lograr uniformidad:
    Obtenemos un listado de clientes: GET /v1/clientes/
    Obtenemos un cliente en partícular: GET /v1/clientes/1234/

Url's lo más cortas posibles
Evita guiones y guiones bajos
Deben ser semánticas para el cliente
Utiliza nombres y no verbos
Estructura jerárquica para indicar la estructura: /v1/clientes/1234/pedidos/203/ '''

#Fuente: https://juanda.gitbooks.io/webapps/content/api/arquitectura-api-rest.html