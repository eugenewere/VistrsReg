from django import forms

from visitorsfront.models import *


class CarouselImageForm(forms.ModelForm):

    class Meta:
        model = Carousel
        fields = ['image','description',]

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['room_name', 'room_number','room_image']

class ConferenceForm(forms.ModelForm):

    class Meta:
        model = Conference
        fields = [
            'conference_name',
            'conference_number',
            'room_image',
            'size',
        ]

