from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/api/task-headers/')),  # Redirect home to API
    path('admin/', admin.site.urls),
    path('api/', include('mtt_api.urls')),  
]
