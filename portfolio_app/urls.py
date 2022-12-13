from django.urls import path

from portfolio_app.views import PostDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, \
    CommentAPIView, PostCreateAPIView, BlogListAPIView, BlogDetailAPIView, ProjectListAPIView, ProjectDetailAPIView

urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('category/<int:category_id>/add_post', PostCreateAPIView.as_view(), name='add_post'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/add_comment', CommentAPIView.as_view(), name='add_comment'),
    path('blog/', BlogListAPIView.as_view(), name='blog_list'),
    path('blog/<int:pk>', BlogDetailAPIView.as_view(), name='blog_detail'),
    path('project', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>', ProjectDetailAPIView.as_view(), name='project_detail')
]
