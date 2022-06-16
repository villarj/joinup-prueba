from django.urls import path
from views import UserProfileSelect

urlpatterns = [
    path('userprofile', UserProfileSelect.as_view(), name='companies'),

]
