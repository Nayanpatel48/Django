from django.urls import path, include
# path is used to define url patterns, 
# "include" is used to include URL configurations from other django apps.

from . import views
# imported views, this views are classes or functions which handles the request for specific
# urls

from django.contrib import admin
# imports django's built-in admin panel

from django.conf import settings 
# imported project settings which are used to configure things like media files.

from django.conf.urls.static import static
# used to serve the static and media files in development.

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/admin/ will show the Django admin panel.

    path('', views.home, name='home'),
    # This defines the root URL (http://127.0.0.1:8000/).

    path('about/', views.about, name='about'),
    # Defines the URL http://127.0.0.1:8000/about/.

    path('contact/', views.contact, name='contact'),
    # Defines the URL http://127.0.0.1:8000/contact/.

    # whenever i am hitting this url i am transfering control to an app urls
    # This routes all URLs starting with http://127.0.0.1:8000/chai/ to the chai app.
    # The chai.urls file must define the routes for the app.
    path('chai/', include('chai.urls')),

    # whenever i am hitting this url i am transfering control to an app urls
    # Routes all URLs starting with http://127.0.0.1:8000/login/ to the login app.
    # The login.urls file defines the routes for the app. 
    path('login/', include('login.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)