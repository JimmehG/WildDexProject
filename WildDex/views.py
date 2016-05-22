from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserType, Animal
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
                user_type = UserType.objects.get(pk=user)
                display_dict['user_type'] = user_type
                print(user_type.b_office)
                # return HttpResponseRedirect('/')
            else:
                disabled = True
        else:
            wrong_password = True
    display_dict['wrong_password'] = wrong_password
    display_dict['disabled'] = disabled
    return render(request, 'index.html', display_dict)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


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

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

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
                  {'user_form': user_form, 'registered': registered})


def reg_user_type(request):
    registered = False
    reg_user = UserType.objects.get(pk=request.session.get('reg_user_id'))

    display_dict = {}

    if request.method == 'POST':
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


def animal_table(request, user):
    query = Animal.objects.all()
    return render(request, 'animal_table.html', {'query': query, 'user': user})


def submitted(request):
    return render(request, 'submitted.html')


def about(request, user=None):
    return render(request, 'about.html', {'user': user})
