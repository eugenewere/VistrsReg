import statistics

from django import template
from django.contrib.auth.models import User
# from django.shortcuts import render_to_response
from django.views import View

from visitorsfront.models import *

register = template.Library()


# @register.filter(name='seller_image')
# def seller_image(request):
#     seller = Seller.objects.filter(user_ptr_id = request.user.id).first()
#     print(seller)
    # if seller.store_logo.url:
    #     return seller.store_logo.url
    # return seller.store_logo.url

@register.filter(name='messagesss')
def allmessages(request):
    messages = Message.objects.order_by('-created_at')

    if messages:
        return messages
    return None

@register.filter(name='if_admin')
def if_admin(request):
    user=request.user.id
    admin = User.objects.filter(id=user, is_superuser=True).first()

    if admin:
        return True
    return False










