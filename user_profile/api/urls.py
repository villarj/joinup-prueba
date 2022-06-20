from django.urls import path
from user_profile.api.views import ContactList

urlpatterns = [
    path('v1/contact', ContactList.as_view(), name='contacts'),
    #path('management/contacts/<int:pk>', ContactDetail.as_view(), name='contacts-detail'),

]
