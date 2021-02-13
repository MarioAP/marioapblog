from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tasks, name='lista'),
    path('detallu/<str:pk>/', views.detallu_tasks, name='detallu'),
    path('kria/', views.kria_tasks, name='kria'),
    path('hadia/<str:pk>/', views.hadia_tasks, name='hadia'),
    path('hamoos/<str:pk>/', views.hamoos_tasks, name='hamoos'),
]
