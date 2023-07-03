from django.urls import path
from .views import *

app_name = 'blog'

# urlpatterns = [
#     path('', blog_list),
#     path('<int:pk>/', blog_detail),
# ]

urlpatterns = [
    path('', BlogList.as_view()),   # as_view를 꼭 붙이자.
    path('<int:pk>/', BlogDetail.as_view()),
]