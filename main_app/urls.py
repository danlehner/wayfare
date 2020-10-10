from django.urls import path, include
from . import views
from django.conf.urls.static import static
from wayfare import settings 

urlpatterns = [
    path('', views.home, name='home'),
    path('cities/<int:city_id>', views.main, name='main'),
    path('new_post/<int:city_id>', views.new_post, name='new_post'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/<int:post_id>/delete', views.post_delete, name='post_delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('accounts/profile/edit', views.profile_edit, name='profile_edit'),
    path('accounts/', include('django.contrib.auth.urls')),
] +static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)