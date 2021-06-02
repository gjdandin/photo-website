from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('post/', views.image_upload_view, name='post'),
    path('post/<str:pk>/', views.image_view, name='image_view'),
    path('post/edit/<str:pk>/', views.edit_image, name='image_edit'),
    path('delete/<str:pk>', views.delete_image, name="delete_image"),
    path('about/', views.about_us, name='about_us'),
    path('all/grid/', views.view_all, name='view_all'),
    #path('all/big/', views.view_big, name='view_big'), #Due to compression, low quality
    path('contact/', views.contact, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
