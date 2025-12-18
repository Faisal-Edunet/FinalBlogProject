
app_name = 'blogapp'
from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
     path('',views.blog_list, name='blog_list'),
    path('create',views.add_blog, name='create'),
    path('upadate/<int:id>',views.update_blog, name='update'),
    path('delete/<int:id>',views.delete_blog, name='delete'),

]

