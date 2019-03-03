from django.urls import path
from . views import BlogHomeListView

urlpatterns = [
    path('',  BlogHomeListView.as_view(), name='index_page_view'),

]
