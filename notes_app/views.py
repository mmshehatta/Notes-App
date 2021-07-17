from django.shortcuts import render
from .models import Notes

# Create your views here.


# *************** to get all Notes **************

def allNotes(request):
    notes_list = Notes.objects.all()
    context= {
    'notes_list':notes_list
    }
    return render(request, 'notes_app/notes_list.html',context)


# **************** to git one note*********************

def noteDetails(request , slug):
    one_note_details = Notes.objects.get(slug=slug)
    context={
    'one_note_details':one_note_details
    }
    return render(request , 'notes_app/note_details.html',context)
