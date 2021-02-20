from django.urls import path
from . import views
#from .views import SearchTaskView


urlpatterns = [
    path('', views.lista_tasks, name='lista'),
    path('detallu/<str:pk>/', views.detallu_tasks, name='detallu'),
    path('kria/', views.kria_tasks, name='kria'),
    path('hadia/<str:pk>/', views.hadia_tasks, name='hadia'),
    path('hamoos/<str:pk>/', views.hamoos_tasks, name='hamoos'),
    #path('search/', SearchTaskView.as_view(), name='search_task'),
    path('search/', views.search_tasks, name='search_task'),
]
