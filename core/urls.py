from django.urls import path, include
from .views import upload_file , get_names

urlpatterns = [
    path('upload_excel',upload_file, name='upload_file' ),
    path('names', get_names, name='get_names' )

]
