from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from accounts.views import CustomTokenAuthentication


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='api/register/')),  # Redirect to register URL
    path('api/', include('accounts.urls')),  # Include the app's URLs
]