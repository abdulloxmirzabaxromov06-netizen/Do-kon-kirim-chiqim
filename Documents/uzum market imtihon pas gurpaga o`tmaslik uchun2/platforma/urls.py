from django.urls import path
from .views import home, bos, acaunt
urlpatterns = [
    path('home/', home, name="home"),
    path('bos/', bos, name="bos"),
    path('acaunt/', acaunt, name="acaunt"),
   
    

]
