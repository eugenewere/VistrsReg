import sweetify
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from visitorsadmin.forms import *
from visitorsrecording import settings


def home(request):
    visitors_count = Visitor.objects.count()
    room_count = Room.objects.count()

    conference_count = Conference.objects.count()
    taken_conference_count = Conference.objects.filter(status='UNAVAILABLE').count()
    av_conference_count = Conference.objects.filter(status='AVAILABLE').count()
    taken_room_count = Room.objects.filter(status='UNAVAILABLE').count()
    av_room_count = Room.objects.filter(status='AVAILABLE').count()
    context={
        'visitors_count':visitors_count,
        'room_count':room_count,
        'taken_room_count':taken_room_count,
        'av_room_count':av_room_count,
        'conference_count':conference_count,
        'taken_conference_count':taken_conference_count,
        'av_conference_count':av_conference_count,
        'messages_count':Message.objects.count()
    }

    return render(request, 'tulia/home/index.html', context)


def logout_view(request):
    logout(request)
    return redirect('Visitors:home')


def carousel(request):
    carousels = Carousel.objects.all()
    context = {
        'carousels': carousels,
    }
    return render(request, 'tulia/product/carousel.html', context)


def addcarousel(request):
    if request.method == 'POST':
        carouselForm = CarouselImageForm(request.POST, request.FILES)
        if carouselForm.is_valid():
            carouselForm.save()
            messages.success(request, 'Advertisment Image Added Successfully')
            return redirect('VisitorsAdmin:carousel')
        else:
            messages.error(request, 'Advertisment Image not Added ')
            return redirect('VisitorsAdmin:carousel')
    return redirect('VisitorsAdmin:carousel')

def carousel_delete(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    carousel.delete()
    messages.success(request, 'Advertisment Image Deleted Succesfully')

    return redirect('VisitorsAdmin:carousel')

def carousel_edit(request, carousel_id):
    carousel = Carousel.objects.filter(id=carousel_id).first()
    form = CarouselImageForm(request.POST, request.FILES, instance=carousel)
    if form.is_valid():
        form.save()
        messages.success(request, 'Advertisment Image Updated Succesfully')

    return redirect('VisitorsAdmin:carousel')


def room(request):
    rooms =Room.objects.all()
    context = {
        'rooms': rooms,
    }
    return render(request, 'tulia/orders/new_orders.html', context)


def addroom(request):
    form = RoomForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        form.save()
        sweetify.success(request, 'Successfully Added', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Adding', button='ok', timer=5000)

    return redirect('VisitorsAdmin:room')


def deleteroom(request,room_id):
    room = Room.objects.filter(id=room_id).first()
    if room is not None:
        room.delete()
        sweetify.success(request, 'Successfully Deleted', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Deleting', button='ok', timer=5000)

    return redirect('VisitorsAdmin:room')


def editroom(request,room_id):
    room = Room.objects.filter(id=room_id).first()
    form = RoomForm(request.POST, request.FILES, instance=room)
    print(form)
    if form.is_valid():
        form.save()
        sweetify.success(request, 'Successfully updated', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error updating', button='ok', timer=5000)

    return redirect('VisitorsAdmin:room')

def editroomstatus(request, room_id):
    room = Room.objects.filter(id=room_id).first()
    if room.status == 'AVAILABLE':
        Room.objects.filter(id=room.id).update(
            status='UNAVAILABLE',
        )
    else:
        Room.objects.filter(id=room.id).update(
            status='AVAILABLE',
        )
    return redirect('VisitorsAdmin:room')

def conference(request):
    conferences = Conference.objects.all()
    context = {
        'conferences': conferences,
    }
    return render(request, 'tulia/orders/confernce.html', context)


def addconference(request):
    form = ConferenceForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        form.save()
        sweetify.success(request, 'Successfully Added', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Adding', button='ok', timer=5000)

    return redirect('VisitorsAdmin:conference')


def deleteconference(request, conference_id):
    conference = Conference.objects.filter(id=conference_id).first()
    if conference is not None:
        conference.delete()
        sweetify.success(request, 'Successfully Deleted', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Deleting', button='ok', timer=5000)
    return redirect('VisitorsAdmin:conference')


def editconference(request, conference_id):
    conference = Conference.objects.filter(id=conference_id).first()
    form = ConferenceForm(request.POST, request.FILES, instance=conference)
    print(form)
    if form.is_valid():
        form.save()
        sweetify.success(request, 'Successfully updated', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error updating', button='ok', timer=5000)
    return redirect('VisitorsAdmin:conference')


def editconferencestatus(request, conference_id):
    conference = Conference.objects.filter(id=conference_id).first()
    if conference.status == 'AVAILABLE':
       Conference.objects.filter(id=conference.id).update(
         status ='UNAVAILABLE',
       )
    else:
       Conference.objects.filter(id=conference.id).update(
            status='AVAILABLE',
       )
    return redirect('VisitorsAdmin:conference')


def visitors(request):
    visitors= Visitor.objects.all()
    context={
        'visitors':visitors,
    }
    return render(request, 'tulia/orders/visitors.html',context )


def deletevisitor(request, visitor_id):
    visitor = Visitor.objects.filter(id=visitor_id).first()
    if visitor is not None:
        visitor.delete()
        sweetify.success(request, 'Visitor Successfully Deleted', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Deleting Visitor', button='ok', timer=5000)
    return redirect('VisitorsAdmin:visitors')






def ListVisitors(request):
    user=request.user.id
    import datetime
    month_data = []
    months_choices=[]
    months_choices_int=[]
    for i in range(1,13):
        months_choices.append(( datetime.date(2008, i, 1).strftime('%B')[0:3]))

    labels2 = months_choices

    for z in range(1,13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))


    for months_choice in months_choices_int:
        month_data.append(Visitor.objects.filter(created_at__month=months_choice).count())

    defaultData2 = month_data
    context2={
        'labels2':labels2,
        'defaultData23':defaultData2,


    }
    return JsonResponse(context2)


def listRooms(request):
    user = request.user.id
    import datetime
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    labels2 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        month_data.append(Room.objects.filter(created_at__month=months_choice).count())

    defaultData2 = month_data
    context2 = {
        'labels2': labels2,
        'defaultData23': defaultData2,

    }
    return JsonResponse(context2)


def listconferences(request):
    user = request.user.id
    import datetime
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    labels2 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        month_data.append(Conference.objects.filter(created_at__month=months_choice).count())

    defaultData2 = month_data
    context2 = {
        'labels2': labels2,
        'defaultData23': defaultData2,

    }
    return JsonResponse(context2)


def listmessagess(request):
    user = request.user.id
    import datetime
    month_data = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    labels2 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        month_data.append(Message.objects.filter(created_at__month=months_choice).count())

    defaultData2 = month_data
    context2 = {
        'labels2': labels2,
        'defaultData23': defaultData2,

    }
    return JsonResponse(context2)


def listbookings(request):
    user = request.user.id
    import datetime
    month_data = []
    month_data2 = []
    months_choices = []
    months_choices_int = []
    for i in range(1, 13):
        months_choices.append((datetime.date(2008, i, 1).strftime('%B')[0:3]))

    labels2 = months_choices

    for z in range(1, 13):
        months_choices_int.append((datetime.date(2008, z, 1).strftime('%m')))

    for months_choice in months_choices_int:
        month_data.append(Room_visitor.objects.filter(created_at__month=months_choice).count())

    for months_choice in months_choices_int:
        month_data2.append(Conference_visitor.objects.filter(created_at__month=months_choice).count())



    defaultData2 = month_data
    defaultData3 = month_data2
    context2 = {
        'labels2': labels2,
        'defaultData23': defaultData2,
        'defaultData33': defaultData3,

    }
    return JsonResponse(context2)


def viewmessages(request):
    messagess=Message.objects.all().order_by('-created_at')
    context={
        'messagess':messagess,
    }
    return render(request, 'tulia/orders/messages.html',context)


def deletemessages(request, messsage_id):
    message = Message.objects.filter(id=messsage_id).first()
    if message is not None:
        message.delete()
        sweetify.success(request, 'Successfully Deleted', timer=3000)
    else:
        sweetify.error(request, title='Error' 'Error Deleting', button='ok', timer=5000)
    return redirect('VisitorsAdmin:messages')


def replymessages(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        subject = subject
        body = message
        k = send_mail(
            subject=subject,
            message=body,
            from_email=email_from,
            recipient_list=recipient_list,

        )
        print(k)
        sweetify.success(request, 'Successfully sent', timer=3000)
        return redirect('VisitorsAdmin:messages')
    else:
        sweetify.error(request, title='Error' 'Error sending', button='ok', timer=5000)
        return redirect('VisitorsAdmin:messages')