
from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig
app_name = MainappConfig

urlpatterns = [


    path('', views.hello_world),

    path('blog/', views.blog),

    path('<str:word>/', views.about),
]
