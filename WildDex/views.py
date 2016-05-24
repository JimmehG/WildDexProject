from django.core.files import File
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.datetime_safe import date

from .models import UserType, Animal, OfficeVolunteer, Carer, BranchCoordinator
from .forms import UserForm, AnimalForm, AnimalFormCarer, BranchCForm, CarerForm, OfficeForm
from django.contrib.auth import logout, authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login_user(request):
    wrong_password = False
    disabled = False
    display_dict = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect('/')
            else:
                disabled = True
        else:
            wrong_password = True
    display_dict['wrong_password'] = wrong_password
    display_dict['disabled'] = disabled
    if request.user is not None:
        if request.user.is_active:
            if UserType.objects.filter(pk=request.user).exists():
                display_dict['user_type'] = UserType.objects.get(pk=request.user)
    return render(request, 'index.html', display_dict)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            new_animal = form.save(commit=False)
            new_animal.office_volunteer = OfficeVolunteer.objects.get(
                pk=UserType.objects.get(pk=request.user).office.pk)
            if 'picture' in request.FILES:
                new_animal.picture = request.FILES['picture']
            new_animal.save()
            return HttpResponseRedirect('/office_animal_table/')
    else:
        form = AnimalForm()
    return render(request, 'animal_form.html', {'comment_form': form})


def office_edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            temp_animal = form.save(commit=False)
            if 'picture' in request.FILES:
                temp_animal.picture = request.FILES['picture']
            temp_animal.save()
            return HttpResponseRedirect('/office_animal_table/')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animal_form.html', {'comment_form': form})


def branch_edit_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    if request.method == 'POST':
        form = AnimalForm(request.POST, request.FILES, instance=animal)
        if form.is_valid():
            temp_animal = form.save(commit=False)
            if 'picture' in request.FILES:
                temp_animal.picture = request.FILES['picture']
            temp_animal.save()
            return HttpResponseRedirect('/branch_animal_table/')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'animal_form.html', {'comment_form': form})


def pick_up(request, animal_id):
    # TODO needs a user check here
    request.session['animal_id'] = animal_id
    words1 = ''
    pressed1 = False
    words2 = ''
    pressed2 = False

    if request.method == 'POST':
        if 'first' in request.session:
            if request.session.get('first'):
                words1 = "<p>Yes</p><p>Is death imminent or highly likely regardless of the care available?</p>"
                pressed1 = True
            else:
                words1 = "<p>No</p><p>Is the animal creating a nuisance for the public or in a dangerous location?</p>"
                pressed1 = True
        else:
            if 'yes1' in request.POST:
                words1 = "<p>Yes</p><p>Is death imminent or highly likely regardless of the care available?</p>"
                pressed1 = True
                request.session['first'] = True
            elif 'no1' in request.POST:
                words1 = "<p>No</p><p>Is the animal creating a nuisance for the public or in a dangerous location?</p>"
                pressed1 = True
                request.session['first'] = False

        if 'yes2' in request.POST:
            words2 = 'Yes'
            pressed2 = True
            request.session['second'] = True
        elif 'no2' in request.POST:
            words2 = 'No'
            pressed2 = True
            request.session['second'] = False
    else:
        if 'first' in request.session:
            del request.session['first']
        if 'second' in request.session:
            del request.session['second']

    return render(request, 'pick_up.html',
                  {'words1': words1, 'pressed1': pressed1, 'words2': words2, 'pressed2': pressed2})


def check(request):
    animal = Animal.objects.get(pk=request.session.get('animal_id'))
    animal.picked_up = True
    if request.session['first']:
        if request.session['second']:
            animal.status = 0
        else:
            animal.status = 1
    else:
        if request.session['second']:
            animal.status = 2
        else:
            animal.status = 3
    # TODO animal.status_date = date.today
    animal.save()
    return render(request, 'check.html', {'animal': animal})


def add_user(request):
    pass


def add_carer(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('submitted.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'comment_form': form})


def register(request):
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            request.session['reg_user_id'] = user.pk
            # Update our variable to tell the template registration was successful.
            return HttpResponseRedirect('/reg_type/')

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request, 'user_form.html',
                  {'user_form': user_form})


def reg_user_type(request):
    registered = False
    reg_user = UserType.objects.get(pk=request.session.get('reg_user_id'))

    display_dict = {}

    if request.method == 'POST':
        # TODO Has the potential to make too many copies of branch manager and office volunteers if a field isn't valid
        valid = True
        if reg_user.b_carer:
            carer_form = CarerForm(request.POST)
            display_dict['carer_form'] = carer_form
            if carer_form.is_valid():
                carer = carer_form.save()
                reg_user.carer = carer
            else:
                valid = False
        if reg_user.b_office:
            office_form = OfficeForm(request.POST)
            display_dict['office_form'] = office_form
            if office_form.is_valid():
                office = office_form.save()
                reg_user.office = office
            else:
                valid = False
        if reg_user.b_branch_c:
            branch_c_form = BranchCForm(request.POST)
            display_dict['branch_c_form'] = branch_c_form
            if branch_c_form.is_valid():
                branch_c = branch_c_form.save()
                reg_user.branch_c = branch_c
            else:
                valid = False

        if valid:
            registered = True
            reg_user.save()

    else:
        if reg_user.b_carer:
            carer_form = CarerForm()
            display_dict['carer_form'] = carer_form
        if reg_user.b_office:
            office_form = OfficeForm()
            display_dict['office_form'] = office_form
        if reg_user.b_branch_c:
            branch_c_form = BranchCForm()
            display_dict['branch_c_form'] = branch_c_form

    display_dict['registered'] = registered
    display_dict['reg_user'] = reg_user
    return render(request, 'register_type.html', display_dict)


def table(request):
    query = UserType.objects.all()
    return render(request, 'table.html', {'query': query})


def animal_table(request):
    query = Animal.objects.all()
    return render(request, 'animal_table.html', {'query': query})


def branch_animal_table(request):
    display_dict = {}
    if UserType.objects.filter(pk=request.user).exists:
        display_dict['query'] = Animal.objects.filter(branch_coordinator=UserType.objects.get(pk=request.user).branch_c)
    return render(request, 'branch_animal_table.html', display_dict)


def office_animal_table(request):
    query = Animal.objects.all()
    return render(request, 'office_animal_table.html', {'query': query})


def carer_animal_table(request):
    display_dict = {}
    if Carer.objects.filter(pk=request.user.pk).exists:
        query = Animal.objects.filter(carer=UserType.objects.get(pk=request.user).carer)
        query.filter(Q(status__isnull=True, picked_up=False) | Q(status=1, picked_up=True))
        display_dict['query'] = query
    return render(request, 'carer_animal_table.html', display_dict)


def carer_edit_animal(request, animal_id):
    display_dict = {}
    # TODO Change to check if u have permission to view the animal too
    if UserType.objects.filter(pk=request.user.pk).exists:
        animal = Animal.objects.get(carer=UserType.objects.get(pk=request.user).carer, status=1, pk=animal_id)

        if request.method == 'POST':
            animal_form = AnimalFormCarer(request.POST, request.FILES, instance=animal)
            if animal_form.is_valid():
                temp_animal = animal_form.save(commit=False)
                if 'picture' in request.FILES:
                    temp_animal.picture = request.FILES['picture']
                temp_animal.save()
            return HttpResponseRedirect('/carer_animal_table/')
        else:
            animal_form = AnimalFormCarer(instance=animal)
            display_dict['comment_form'] = animal_form
    else:
        return HttpResponse('You ain\'t got permission buddy <p><a href="/">Home</a></p>')
    return render(request, 'carer_edit_animal.html', display_dict)


def submitted(request):
    return render(request, 'submitted.html')


def about(request):
    return render(request, 'about.html')
