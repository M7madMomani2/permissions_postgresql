from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .serializers import Postserializer
from posts_app.models import Posts

# Create your views here.
class PostList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = Postserializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = Postserializer