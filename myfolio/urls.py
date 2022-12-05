from django.urls import path
from myfolio.views import index
urlpatterns = [
    path('', index, name='index'),
    
]