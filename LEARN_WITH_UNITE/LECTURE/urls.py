from django.urls import path
from .views import *

app_name = 'TUTORIALS'




urlpatterns = [
    path('physics5', Physics5ListView.as_view(), name='phy5_list'),
    path('physics5_topic/<int:pk>/', Physics5DetailView.as_view(), name='phy5_detail'),
    path('physics5_add_tutorial/', Physics5VideoCreateView.as_view(), name='tutorial_add_phy5'),
    path('physics5_add_topic/', Physics5TopicCreateView.as_view(), name='topic_add_phy5'),
    path('physics5_delete_tutorial/(?P<pk>\d+)/$', Physics5VideoDeleteView, name='tutorial_delete_phy5'),
    path('physics5_delete_topic/(?P<pk>\d+)/$', Physics5TopicDeleteView, name='topic_delete_phy5'),

    path('biology5', Biology5ListView.as_view(), name='bio5_list'),
    path('biology5_topic/<int:pk>/', Biology5DetailView.as_view(), name='bio5_detail'),
    path('biology5_add_tutorial/', Biology5VideoCreateView.as_view(), name='tutorial_add_bio5'),
    path('biology5_add_topic/', Biology5TopicCreateView.as_view(), name='topic_add_bio5'),
    path('biology5_delete_tutorial/(?P<pk>\d+)/$', Biology5VideoDeleteView, name='tutorial_delete_bio5'),
    path('biology5_delete_topic/(?P<pk>\d+)/$', Biology5TopicDeleteView, name='topic_delete_bio5'),

    path('chemistry5', Chemistry5ListView.as_view(), name='chem5_list'),
    path('chemistry5_topic/<int:pk>/', Chemistry5DetailView.as_view(), name='chem5_detail'),
    path('chemistry5_add_tutorial/', Chemistry5VideoCreateView.as_view(), name='tutorial_add_chem5'),
    path('chemistry5_add_topic/', Chemistry5TopicCreateView.as_view(), name='topic_add_chem5'),
    path('chemistry5_delete_tutorial/(?P<pk>\d+)/$', Chemistry5VideoDeleteView, name='tutorial_delete_chem5'),
    path('chemistry5_delete_topic/(?P<pk>\d+)/$', Chemistry5TopicDeleteView, name='topic_delete_chem5'),


    path('economics5', Economics5ListView.as_view(), name='eco5_list'),
    path('economics5_topic/<int:pk>/', Economics5DetailView.as_view(), name='eco5_detail'),
    path('economics5_add_tutorial/', Economics5VideoCreateView.as_view(), name='tutorial_add_eco5'),
    path('economics5_add_topic/', Economics5TopicCreateView.as_view(), name='topic_add_eco5'),
    path('economics5_delete_tutorial/(?P<pk>\d+)/$', Economics5VideoDeleteView, name='tutorial_delete_eco5'),
    path('economics5_delete_topic/(?P<pk>\d+)/$', Economics5TopicDeleteView, name='topic_delete_eco5'),


    path('english5', English5ListView.as_view(), name='lang5_list'),
    path('english5_topic/<int:pk>/', English5DetailView.as_view(), name='lang5_detail'),
    path('english5_add_tutorial/', English5VideoCreateView.as_view(), name='tutorial_add_lang5'),
    path('english5_add_topic/', English5TopicCreateView.as_view(), name='topic_add_lang5'),
    path('english5_delete_tutorial/(?P<pk>\d+)/$', English5VideoDeleteView, name='tutorial_delete_lang5'),
    path('english5_delete_topic/(?P<pk>\d+)/$', English5TopicDeleteView, name='topic_delete_lang5'),


    path('geography5', Geography5ListView.as_view(), name='geo5_list'),
    path('geography5_topic/<int:pk>/', Geography5DetailView.as_view(), name='geo5_detail'),
    path('geography5_add_tutorial/', Geography5VideoCreateView.as_view(), name='tutorial_add_geo5'),
    path('geography5_add_topic/', Geography5TopicCreateView.as_view(), name='topic_add_geo5'),
    path('geography5_delete_tutorial/(?P<pk>\d+)/$', Geography5VideoDeleteView, name='tutorial_delete_geo5'),
    path('geography5_delete_topic/(?P<pk>\d+)/$', Geography5TopicDeleteView, name='topic_delete_geo5'),


    path('history5', History5ListView.as_view(), name='his5_list'),
    path('history5_topic/<int:pk>/', History5DetailView.as_view(), name='his5_detail'),
    path('history5_add_tutorial/', History5VideoCreateView.as_view(), name='tutorial_add_his5'),
    path('history5_add_topic/', History5TopicCreateView.as_view(), name='topic_add_his5'),
    path('history5_delete_tutorial/(?P<pk>\d+)/$', History5VideoDeleteView, name='tutorial_delete_his5'),
    path('history5_delete_topic/(?P<pk>\d+)/$', History5TopicDeleteView, name='topic_delete_his5'),


    path('kiswahili5', Kiswahili5ListView.as_view(), name='kis5_list'),
    path('kiswahili5_topic/<int:pk>/', Kiswahili5DetailView.as_view(), name='kis5_detail'),
    path('kiswahili5_add_tutorial/', Kiswahili5VideoCreateView.as_view(), name='tutorial_add_kis5'),
    path('kiswahili5_add_topic/', Kiswahili5TopicCreateView.as_view(), name='topic_add_kis5'),
    path('kiswahili5_delete_tutorial/(?P<pk>\d+)/$', Kiswahili5VideoDeleteView, name='tutorial_delete_kis5'),
    path('kiswahili5_delete_topic/(?P<pk>\d+)/$', Kiswahili5TopicDeleteView, name='topic_delete_kis5'),



    path('mathematics5', Mathematics5ListView.as_view(), name='math5_list'),
    path('mathematics5_topic/<int:pk>/', Mathematics5DetailView.as_view(), name='math5_detail'),
    path('mathematics5_add_tutorial/', Mathematics5VideoCreateView.as_view(), name='tutorial_add_math5'),
    path('mathematics5_add_topic/', Mathematics5TopicCreateView.as_view(), name='topic_add_math5'),
    path('mathematics5_delete_tutorial/(?P<pk>\d+)/$', Mathematics5VideoDeleteView, name='tutorial_delete_math5'),
    path('mathematics5_delete_topic/(?P<pk>\d+)/$', Mathematics5TopicDeleteView, name='topic_delete_math5'),




]