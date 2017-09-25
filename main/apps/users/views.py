from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    # Get
    # a GET request to /users - calls the index method to display all the users. This will need a template.
    # first = request.session['first']
    # last = request.session['last']
    # email = request.session['email']
    # users = request.session['users']

    # users_model = User.objects.all()
    # for num in users_model:
    #     print num.first_name
    #     print num.last_name
    #     print num.email

    #     first = num.first_name
    #     last = num.last_name
    #     email = num.email
    context = {
        "users_info":User.objects.all()
        }

    return render(request, 'users/index.html', context)

def new(request):
    # Get
    # GET request to /users/new - calls the new method to display a form allowing users to create a new user. This will need a template.
    
    return render(request,'users/new.html')
def edit(request,id):    
    # GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id. This will need a template.
     
    # request.session['first'] = User.objects.get(id = id).first_name
    # request.session['last'] = User.objects.get(id = id).last_name
    # request.session['email'] = User.objects.get(id = id).email
    # request.session['id'] = User.objects.get(id = id).id  

    return render(request, 'users/edit.html', {"user":User.objects.get(id = id)})
def show(request,id):    
    #GET /users/<id> - calls the show method to display the info for a particular user with given id. This will need a template.

    return render(request, 'users/show.html',{"user":User.objects.get(id = id)})
def create(request):    
    # POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new. Have this redirect to /users/<id> once created.
     
    new_user = User(first_name = request.POST['first_n'] ,last_name = request.POST['last_n'], email = request.POST['email_addr'])
    new_user.save()

    return redirect('/users/new')
def destroy(request, id):    
    #GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id. Have this redirect back to /users once deleted.
    delete_user = User.objects.get(id = id)
    delete_user.delete()

    return redirect('/users')
def update(request, id):    
    #POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit. Have this redirect to /users/<id> once updated.
    update_user = User.objects.get(id = id)
    update_user.first_name = request.POST['f_name']   
    update_user.save()
    update_user.last_name = request.POST['l_name']
    update_user.email = request.POST['new_email']    
    update_user.save()
    return redirect('/users/'+str(update_user.id))

    