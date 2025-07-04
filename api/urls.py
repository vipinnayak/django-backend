from django.urls import path
from .views import SignupAPI, LoginAPI
from .views import InsuranceAPIView

urlpatterns = [
    path('signup/', SignupAPI.as_view(), name='signup'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('insurance/', InsuranceAPIView.as_view(), name='insurance'),

]
