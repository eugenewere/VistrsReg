import sweetify
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from visitorsfront.forms import *
from visitorsfront.models import *


# Create your views here.

# # Base method with no type specified
# sweetify.sweetalert(self.request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')
#
# # Additional methods with the type already defined
# sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)
# sweetify.success(self.request, 'You successfully changed your password')
# sweetify.error(self.request, 'Some error happened here - reload the site', persistent=':(')
# sweetify.warning(self.request, 'This is a warning... I guess')

def home(request):
    carousels = Carousel.objects.all()
    context = {
        'carousels':carousels,
    }

    return render(request, 'mainindex.html', context)


def register(request):
    form = RegisterVisitorForm(request.POST)

    if form.is_valid():
        sweetify.success(request, 'Successfully Registered', timer=3000)
        form.save()
    else:
        sweetify.error(request, title='Error' 'Please correct the errors and continue '+str(form.error_messages), button='ok', timer=5000)
    carousels = Carousel.objects.all()
    context = {
        'form': RegisterVisitorForm(request.POST),
        'carousels': carousels,
    }
    return  render(request, 'mainindex.html', context)


def contuctus(request):
    form = MessageVisitorForm(request.POST)
    print(form)
    if form.is_valid():
        sweetify.success(request, 'Successfully Sent', timer=3000)
        form.save()
    else:
        sweetify.error(request, title='Error' 'Error Sending', button='ok', timer=5000)
    return redirect('Visitors:home')


def loginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        def adminusername(username):
            uzer=User.objects.filter(Q(username__exact=username) | Q(email__exact=username)).first()
            if uzer:
                return uzer.username
            return None
        def visitorusername(username):
            print(username)
            uz= Visitor.objects.filter(Q(email__exact=username)|Q(username__exact=username)).first()
            print(uz)
            if uz:
                print(
                    uz.username
                )
                return uz.username
            return None

        if User.objects.filter(Q(username__exact=username) | Q(email__exact=username)).first() or Visitor.objects.filter(Q(email__exact=username) | Q(username__exact=username)).first():
            if Visitor.objects.filter(Q(email__exact=username) | Q(username__exact=username)).first():
                user = authenticate(username=visitorusername(username), password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        sweetify.success(request, 'Success', text='Welcome to Digi-Guest', persistent='Continue')
                        return redirect('VisitorsAdmin:home')
                    else:
                        sweetify.error(request, 'Error', text='Lets Not Talk about This Again... YOU DONT HAVE AN ACCOUNT HERE PLIZ.',
                                       persistent='Retry')
                        return redirect('Visitors:home')
                else:
                    sweetify.error(request, 'Error',
                                   text='Lets Not Talk about This Again... YOU DONT HAVE AN ACCOUNT HERE PLIZ.',
                                   persistent='Retry')
                    return redirect('Visitors:home')
            elif User.objects.filter(Q(username__exact=username)|Q(email__exact=username) and Q(is_superuser=True)).first():
                user = authenticate(username=adminusername(username), password=password,)
                if user is not None:
                    if user.is_staff and user.is_active:
                        login(request, user)
                        sweetify.success(request, 'Success', text='Welcome Admin',persistent='Continue')
                        return redirect('VisitorsAdmin:home')
                    else:
                        sweetify.error(request, 'Error',
                                       text='Lets Not Talk about This Again... YOU DONT HAVE AN ACCOUNT HERE PLIZ.',
                                       persistent='Retry')
                        return redirect('Visitors:home')
                else:
                    sweetify.error(request, 'Error',
                                   text='Lets Not Talk about This Again... YOU DONT HAVE AN ACCOUNT HERE PLIZ.',
                                   persistent='Retry')
                    return redirect('Visitors:home')


    return