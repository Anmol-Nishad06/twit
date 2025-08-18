from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.twit_list, name='home'),
    path('twit_list/', views.twit_list, name='twit_list'),
    path('create/', views.twit_create, name='twit_create'),
    path('edit/<int:id>/', views.twit_edit, name='twit_edit'),
    path('delete/<int:id>/', views.twit_delete, name='twit_delete'),
    path('register/',views.register,name="register"),
    path('profile/', views.profile, name='profile'),
]