from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
    path('post', views.post, name='post'),
    path('update/<int:update_id>/<str:title>/<str:content>/<str:tag>', views.update, name='update'),
    path('specific_tag/update/<int:update_id>/<str:title>/<str:content>/<str:tag>', views.update, name='specific_tag'),
    path('tags', views.tags, name='tags'),
    path('specific_tag/<str:tag>', views.specific_tag, name='specific_tag'),
]