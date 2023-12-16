from django.urls import path
from . import views

app_name = 'touristapp'

urlpatterns = [
    
    path('',views.Kerala_tourism,name='Kerala_tourism'),
    path('About/',views.About,name='About'),
    path('E_brochures/',views.E_brochures,name='E_brochures'),
    path('E_Newsletter/',views.E_Newsletter,name='E_Newsletter'),
    path('Experience_kerala/',views.Experience_kerala,name='Experience_kerala'),
    path('Festivals/',views.Festivals,name='Festivals'),
    path('Plan_your_trip/',views.Plan_your_trip,name='Plan_your_trip'),
    path('Things_to_do/',views.Things_to_do,name='Things_to_do'),
    path('Where_to_go/',views.Where_to_go,name='Where_to_go'),
    path('Where_to_stay/',views.Where_to_stay,name='Where_to_stay')

]