from django.urls import path
from . import views

urlpatterns = [
    path("", views.station ,name = 'station'),
    path('st<int:my_id>/',views.station_det,name='station_det'),
]
