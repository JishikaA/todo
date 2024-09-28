from django.urls import path

from todo_app import views, admin

urlpatterns = [
    path('',views.index_dashboard,name='index_dashboard'),
    path('test',views.test,name='test'),
    path('read',views.read,name='read'),
    path("delete/<int:id>/",views.remove,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('user',views.user,name='user')
]