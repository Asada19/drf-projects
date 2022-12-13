from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from portfolio_app.models import Post, Category, Comment, Blog, Project
from portfolio_app.serializers import PostSerializer, CategoryDetailSerializer, CommentSerializer, \
    CategoryListSerializer, BlogSerializer, ProjectSerializer

User = get_user_model()


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        category_id = self.kwargs.get('category_id')
        category = Category.objects.get(id=category_id)
        serializer.save(category=category)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    model = Post
    serializer_class = PostSerializer


class CategoryListAPIView(ListCreateAPIView):
    model = Category
    serializer_class = CategoryListSerializer
    parser_classes = (MultiPartParser, FormParser)
    ordering = '-created_on'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class CommentAPIView(CreateAPIView):
    model = Comment
    serializer_class = CommentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        user = self.request.user
        serializer.save(author=user, post=post)


class BlogListAPIView(ListCreateAPIView):
    model = Blog
    serializer_class = BlogSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    model = Blog
    serializer_class = BlogSerializer


class ProjectListAPIView(ListCreateAPIView):
    model = Project
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    model = Project
    serializer_class = ProjectSerializer
