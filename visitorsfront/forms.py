from django import forms
from django.contrib.auth.forms import UserCreationForm

from visitorsfront.models import *


class CarouselImageForm(forms.ModelForm):

    class Meta:
        model = Carousel
        fields = ['image','description',]

class RegisterVisitorForm(UserCreationForm):

    class Meta:
        model = Visitor
        fields = ['password1',
                  'password2',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'username',
                  'id_no',
                  'phone_number',
                  'person_to_meet',
                  'date_from',
                  'date_to',
                  'address'
                  ]
class MessageVisitorForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
                  'first_name',
                  'last_name',
                  'email',
                  'subject',
                  'msg'
                  ]



