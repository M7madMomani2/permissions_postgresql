from django.urls.conf import path
from posts_app.views import PostList,PostDetail

urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
    path('<int:pk>/',PostDetail.as_view(),name='post_detail'),

]

