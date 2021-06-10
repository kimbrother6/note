from django.shortcuts import render, redirect
from .models import Sentence
from .forms import englishNoteForm
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:////Users/cubest_june/hj-django/note/db.sqlite3")


# Create your views here.
def english_note_home_page(request):
    sentence = Sentence.objects.all()

    with engine.connect() as conn, conn.begin():
            data = pd.read_sql_table("english_note_sentence", conn)
    class_list = data['Class'].unique()

    return render(request, 'english_note/home.html', {'sentenc': sentence, 'class_list': class_list})





def sentenceCard(request, listName, listId):
    sentence = Sentence.objects.filter(Class=listName)
    return render(request, 'english_note/sentenceCard.html', {'sentences':sentence, 'listId': listId})

def new_page(request):
    if request.method == 'POST':
        post_form = englishNoteForm(request.POST)
        post_form.save()

        return redirect('/english_note/')
    else:
        form = englishNoteForm
        return render(request, 'english_note/forms.html', {'form': form})
