from django.urls import path
# path is used to define url patterns, 
# "include" is used to include URL configurations from other django apps.

from . import views
# imported views, this views are classes or functions which handles the request for specific
# urls

# localhost:8000/chai
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
    # When the base URL for the chai app (http://127.0.0.1:8000/chai/) is accessed 
    # (i.e., no additional path is provided), the all_chai view will be called.

    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    # pending understanding ...........................................=========

    path('chai_stores/', views.chai_store_view, name='chai_stores'),
    # http://127.0.0.1:8000/chai/chai_stores/
    # When this URL is accessed, the chai_store_view view function will be called.
]