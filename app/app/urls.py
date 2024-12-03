#from django.contrib import admin
#from django.urls import path
#from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hello, World! This is a Django app running on port 5000.")

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', index),
#]


from django.contrib import admin
from django.urls import path
from .views import data_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data_view),  # Endpoint for data input and retrieval
]

