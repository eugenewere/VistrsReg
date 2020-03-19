

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class Visitor(get_user_model()):
    phone_number = models.CharField(max_length=200, null=False, blank=False)
    prof_image = models.ImageField(max_length=200, null=True, blank=True, upload_to='visitors')
    person_to_meet = models.CharField(max_length=20, null=False, blank=False)
    address = models.TextField()
    id_no = models.CharField(max_length=20, null=False, blank=False)
    date_from = models.DateTimeField(default=timezone.now())
    date_to = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)




class Room(models.Model):
    room_name = models.CharField(max_length=200, null=False, blank=False)
    room_number = models.CharField(max_length=200, null=False, blank=False)
    room_image = models.ImageField(max_length=200, null=False, blank=False, upload_to='rooms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ROOM_STATUS=(
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE','Unavailable'),
    )
    status = models.CharField(choices=ROOM_STATUS, max_length=200, null=False, blank=False, default='AVAILABLE')

    def __str__(self):
        return '%s ($s)' % (self.room_name, (self.status))

class Conference(models.Model):
    conference_name = models.CharField(max_length=200, null=False, blank=False)
    conference_number = models.CharField(max_length=200, null=False, blank=False)
    size = models.CharField(max_length=200, null=False, blank=False)
    room_image = models.ImageField(max_length=200, null=False, blank=False, upload_to='conferences')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    CONFERENCE_STATUS=(
        ('AVAILABLE', 'Available'),
        ('UNAVAILABLE','Unavailable'),
    )
    status = models.CharField(choices=CONFERENCE_STATUS, max_length=200, null=False, blank=False, default='AVAILABLE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s ($s)' % (self.conference_name, (self.status))


class Room_visitor(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=False, blank=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=False, blank=False)
    ROOM_VISITOR_STATUS = (
        ('BOOKED', 'Booked'),
        ('UNBOOKED', 'Unbooked'),
    )
    status = models.CharField(choices=ROOM_VISITOR_STATUS, max_length=200, null=False, blank=False, default='BOOKED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.room.room_name)

class Conference_visitor(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, null=False, blank=False)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, null=False, blank=False)
    CONFERENCE_VISITORS_STATUS = (
        ('BOOKED', 'Booked'),
        ('UNBOOKED', 'Unbooked'),
    )
    status = models.CharField(choices=CONFERENCE_VISITORS_STATUS, max_length=200, null=False, blank=False, default='BOOKED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.room.room_name)

class Carousel(models.Model):
    image = models.ImageField(default="no_carousel.jpg", upload_to='couresel')  # height_field=None, width_field=None,
    description = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.image, self.description)

class Message(models.Model):
    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    subject = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    msg = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s ' % (self.first_name, self.last_name)
