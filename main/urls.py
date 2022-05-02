"""pydrive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('', views.home, name='index'),
    path('get_entry', views.get_entry, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('folders_display', views.folder_click, name='folders_display'),
    path('upload_files', views.upload_files, name='upload_files'),
    path('save_folder', views.save_folder, name='save_folder'),
    path('file_provider/', views.file_provider, name='file_provider'),
    path('folder_provider/',views.folder_provider, name='folder_provider'),
    path('file_download',views.file_download, name='file_download'),
    path('folder_download', views.download_folder,name='folder_download'),
    path('delete', views.delete_file, name='delete'),
    path('delete_folder',views.delete_folder, name='delete_folder'),
    path('get_shared',views.get_shared,name='get_shared'),
    path('check_share',views.check_share,name='check_share'),
    path('revoke_share',views.revoke_share,name="revoke_share"),
    path('shared_file_provider',views.shared_file_provider,name='shared_file_provider'),
    path('shared_folder_provider',views.shared_folder_provider,name='shared_file_provider'),
    path('shared_dashboard',views.render_shared,name='shared_dashboard'),
    path('logout', views.logout, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
