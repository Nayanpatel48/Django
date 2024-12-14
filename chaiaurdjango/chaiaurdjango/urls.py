from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # whenever i am hitting this url i am transfering control to an app urls
    path('chai/', include('chai.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)