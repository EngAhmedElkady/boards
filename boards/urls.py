from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('board/<int:id>/',views.Board_topics,name='boards'),
    path('board/<int:id>/new',views.new_topic,name='topic'),
    path('board/<int:id>/topics/<int:topic_id>/',views.all_posts,name='posts'),




]
