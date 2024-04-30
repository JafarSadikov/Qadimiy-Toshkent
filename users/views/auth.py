from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny#, IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import MyTokenObtainPairSerializer, RegisterSerializer#, ProfileSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response(
                {"access": access_token},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getProfile(request):
#     user = request.user
#     serializer = ProfileSerializer(user, many=False)
#     return Response(serializer.data)