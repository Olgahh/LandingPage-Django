from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer


class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer
