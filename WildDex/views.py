from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PersonForm


# Create your views here.


# def index(request):
#    return HttpResponse("Hello world!")


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
     # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/wilddex/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = PersonForm()

    return render(request, 'personform.html', {'form': form})

def about(request):
    #return HttpResponse("about")
    return render(request, 'about.html', {})
