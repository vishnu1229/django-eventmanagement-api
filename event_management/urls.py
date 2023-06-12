from django.urls import include ,path
from django.contrib import admin
urlpatterns = [
    # ... other URL patterns ...

    path('admin/', admin.site.urls),
      path('', include('events.urls')),
]
