from django.urls import path, include
from django.conf import settings
from api.room.views import *
from api.book.views import *
from api.mail.views import *
from api.views import *

urlpatterns = [
    path('access-right/', v_access_right),
    path('pages-app-list/', v_page_list),
    
    # Room
    path('room/', v_room),
    
    # Book
    path('book/', v_book),
    
    # Available
    path('available-room/', v_availableroom),
    
    # Switch
    path('switch-book/', v_switch),
    
    #
    path('mail-manage/', v_mail_manage),
]