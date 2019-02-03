from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'blog'
urlpatterns=[
    path('', views.main, name = 'main'),
    path('post_create/', views.post_create, name = 'post_create'),
    path('<int:pk>/comment/', views.comment_create, name = 'comment_create'),
    path('<int:pk>/edit/',views.post_edit, name = 'post_edit'),
    path('<int:pk>/delete/',views.post_delete, name = 'post_delete'),
    path('<int:pk>/', views.post_read, name = 'post_read'),
    path('post_list/',views.post_list, name = 'post_list'),

    path('login/',auth_views.LoginView.as_view(), name='login'), 
    path('signup/', views.CreateUserView.as_view(), name = 'signup'),  
    path('signup/done', views.RegisteredView.as_view(), name = 'create_user_done'),
    path('login_done/', views.RegisteredView.as_view(), name = 'login_done'),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),  
    path('permission_denied/', views.permission_denied, name = 'permission_denied'),  


]