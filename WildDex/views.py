from django.forms import inlineformset_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserType, Animal
from .forms import CarerForm, UserProfileForm, AnimalForm, AnimalFormCarer
from django.contrib.auth import logout, authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/login/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print
            ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_home(request, user):
    return render(request, 'home_templates/' + user + '_home.html', {'user': user})


def add_animal(request, user):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + user + '/animal_table/')
    else:
        form = AnimalForm()
    return render(request, 'animal_form.html', {'comment_form': form, 'user': user})


def edit_animal(request, animal_id, user):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        if user == 'carer':
            form = AnimalFormCarer(request.POST, instance=animal)
        else:
            form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + user + '/animal_table/')
    else:
        if user == 'carer':
            form = AnimalFormCarer(instance=animal)
        else:
            form = AnimalForm(instance=animal)
    return render(request, 'animal_form.html', {'comment_form': form, 'user': user})


def add_carer(request, user):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CarerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('submitted.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CarerForm()

    return render(request, 'user_form.html', {'comment_form': form})


'''def manage_animals(request, caller_id):
    caller = Caller.objects.get(pk=caller_id)
    animal_inline_formset = inlineformset_factory(Caller, Animal, fields=('species', 'gender'))
    if request.method == "POST":
        formset = animal_inline_formset(request.POST, request.FILES, instance=caller)
        if formset.is_valid():
            formset.save()
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(caller.get_absolute_url())
    else:
        formset = animal_inline_formset(instance=caller)
    return render(request, 'manage_books.html', {'formset': formset})'''


def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = CarerForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = CarerForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'user_form.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def table(request):
    query = UserType.objects.all()
    return render(request, 'table.html', {'query': query})


def animal_table(request, user):
    query = Animal.objects.all()
    return render(request, 'animal_table.html', {'query': query, 'user': user})


def submitted(request):
    return render(request, 'submitted.html')


def about(request, user=None):
    return render(request, 'about.html', {'user': user})
