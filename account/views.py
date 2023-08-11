from rest_framework import generics
from rest_framework.response import Response
from account.serializers import RegisterUserSerializer, LoginUserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import BlacklistedToken

# Create your views here.
 

class CreateUser(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        data = self.serializer_class(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'message':'Account Created! successfully'})


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message':'Login successful'})
        return Response({'message':'login failed check email and password and login gain '})

