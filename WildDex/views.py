from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def add_user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/submitted/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'userform.html', {'comment_form': form})


def table(request):
    query = User.objects.all()
    return render(request, 'table.html', {'query': query})


def submitted(request):
    return render(request, 'submitted.html')


def about(request):
    return render(request, 'about.html')
