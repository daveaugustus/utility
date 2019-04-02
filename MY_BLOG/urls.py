from django.urls import path
from . views import BlogHomeListView, PostDetailsView, PostBlogView

urlpatterns = [
    path('home/',  BlogHomeListView.as_view(), name='index_page_view'),
    # path('post/',  PostDetailsView.as_view(), name='blog_post_view'),
    path('post/',  PostBlogView.as_view(), name='blog_post_view'),

]
