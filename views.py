from django.shortcuts import render
from library_app.models import Books
from library_app.forms import BookForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts  import render_to_response,redirect
from utils import get_query


def home(request):
    books = Books.objects.all().order_by('-id')[:18]
    data={'books':books}
    return render_to_response('home.html', data)


def add(request):
    data = {}
    form = BookForm()
    # print form

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your book was saved. Thank you!')



    return render(request, 'add.html', {
        'form': form
    })

def search(request):
    query_string = ''
    found_entries = None
    data = {}
    if ('q' in request.POST) and request.POST['q'].strip():
        query_string = request.POST['q']

        entry_query = get_query(query_string, ['title', 'author','description'])

        found_entries = Books.objects.filter(entry_query)


    return render_to_response('search_results.html',
                          { 'query_string': query_string, 'found_entries': found_entries })

