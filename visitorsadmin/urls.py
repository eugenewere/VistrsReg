from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from visitorsadmin import views

app_name='VisitorsAdmin'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout_view', views.logout_view, name='logout_view'),

    path('carousel/', views.carousel, name='carousel'),
    path('addcarousel/', views.addcarousel, name='addcarousel'),
    path('carousel/delete/<int:carousel_id>', views.carousel_delete, name='carousel-delete'),
    path('carousel/edit/<int:carousel_id>', views.carousel_edit, name='carousel-edit'),

    path('room', views.room, name='room'),
    path('addroom', views.addroom, name='addroom'),
    path('deletedroom<int:room_id>', views.deleteroom, name='deleteroom'),
    path('editroom<int:room_id>', views.editroom, name='editroom'),
    path('editroomstatus<int:room_id>', views.editroomstatus, name='editroomstatus'),

    path('conference', views.conference, name='conference'),
    path('addconference', views.addconference, name='addconference'),
    path('deletedconference<int:conference_id>', views.deleteconference, name='deleteconference'),
    path('editconference<int:conference_id>', views.editconference, name='editconference'),
    path('editconferencestatus<int:conference_id>', views.editconferencestatus, name='editconferencestatus'),

    path('visitors/', views.visitors, name='visitors'),
    path('deletevisitor/<int:visitor_id>', views.deletevisitor, name='deletevisitor'),

    path('ListVisitors', views.ListVisitors, name='ListVisitors'),
    path('ListRooms', views.listRooms, name='ListRooms'),
    path('Listconferences', views.listconferences, name='Listconferences'),
    path('Listmessagess', views.listmessagess, name='Listmessagess'),
    path('Listbookings', views.listbookings, name='Listbookings'),
    path('Listuserbookings', views.listuserbookings, name='Listuserbookings'),
    path('Listuserroomsbookings', views.listuserroomsbookings, name='Listuserroomsbookings'),
    path('Listuserconferencebookings', views.listuserconferencebookings, name='Listuserconferencebookings'),

    path('messages', views.viewmessages, name='messages'),
    path('replymessages', views.replymessages, name='replymessages'),
    path('deletemessages<int:messsage_id>', views.deletemessages, name='deletemessage'),


    path('bookroom<int:room_id>', views.bookroom, name='bookroom'),
    path('bookconference<int:conference_id>', views.bookconference, name='bookconference'),



]