from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('upload/', views.upload_file, name='upload_file'),
    path('filelist/', views.file_list, name='file_list'),
    path('signout/', views.signout_view, name='signout'),
    # ... other URL patterns
]
