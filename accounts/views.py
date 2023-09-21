from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from .authentication import create_access_token,create_refresh_token,decode_access_token
from rest_framework.authtoken.models import Token
from rest_framework.authentication import get_authorization_header
from .serializer import UserSerializer
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed


class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginUser(APIView):
    def post(self, request):
        user = CustomUser.objects.filter(email=request.data['email']).first()

        if not user:
            raise APIException('Invalid credentials')

        if not user.check_password(request.data['password']):
            raise APIException('Invalid credentials')

        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)

        response.data = {
            "access_token": access_token
        }
        return response
    

class UserAPIView(APIView):
    def get(self,request):
        auth = request.headers.get("Authorization").split()
        if auth:
            token = auth[1]
            id = decode_access_token(token)

            user = CustomUser.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)
        else:
             raise AuthenticationFailed('unauthenticated')