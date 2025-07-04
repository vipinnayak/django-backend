from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Django App Deployed Successfully on Railway!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', home),  # 👈 Ye line add karo homepage ke liye
]
