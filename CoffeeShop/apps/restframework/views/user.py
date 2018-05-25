import jwt
from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from CoffeeShop import settings as main_settings
from ..serializers.user import UserSerializer
from ..models import MyUser


class UserViewSet(viewsets.ModelViewSet):
    """
        Create ViewSet of MyUser Model
    """

    # authenticate user with JWT token
    permission_classes = (IsAuthenticated,)
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class CreateUserAPIView(APIView):
    """
       serialize and save userl
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    """
        Generate and assign token into user
    :param request: login request
    :return: jwt token
    """

    try:
        email = request.data['email']
        password = request.data['password']
        user = MyUser.objects.get(email=email)
        if user:

            try:
                # create jwt web token
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, main_settings.SECRET_KEY)
                user_details = {'name': '{first_name} {last_name}'.format(first_name=user.first_name,
                                                                          last_name=user.last_name), 'token': token}
                user_logged_in.send(sender=user.__class__, request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)

            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide a email and a password'}
        return Response(res)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # only authenticated user can access this url
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSON field and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        # update user information
        serializer_data = request.data.get('user', {})

        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
