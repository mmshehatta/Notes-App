

from django.urls import  path
from . import views
app_name = 'notes'
urlpatterns = [
    path('', views.allNotes, name='all-notes'),
    path('<str:slug>' , views.noteDetails , name='note-details')

]
