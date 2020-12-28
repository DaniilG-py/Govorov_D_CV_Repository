from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import serializers

from ..models import CustomUser
from .serializers import LoginSerializer, RegistrationSerializer, ReadOnlyUserSerializer, WriteOnlyUserSerializer


class LoginAPIView(APIView):

    """
    Logs in an existing user.
    """

    # Allow not authenticated requests
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks if user exists.
        Username and password are required.
        Returns a JSON web token.
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(ListAPIView):

    """
    ViewSet for 'GET', 'POST', 'PUT', 'PATCH' and 'DELETE' requests.
    """

    # Allow only authenticated users to access this urls
    permission_classes = [IsAuthenticated, ]

    def get(self, request, **kwargs):

        """
        Handles `CustomUser` objects into JSON and sends to the client.
        -If function did not recieved primary_key into **kwargs, it serializes fields of all CustomUser models.
        -If function recieved primary_key and it is exists, then serializes this model, otherwise tells that primary_key recived does not exists.
        """

        try:
            pk = kwargs['pk']
            try:
                queryset = CustomUser.objects.get(id=pk)
            except:
                return Response({
                        "message": f"User with primary_key `{pk}`does not exists."},
                        status=status.HTTP_404_NOT_FOUND
                    )
        except:
            queryset = CustomUser.objects.all()
            serializer = ReadOnlyUserSerializer(queryset.values(), many=True)
        else:
            serializer = ReadOnlyUserSerializer(queryset, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        """

        serializer = RegistrationSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
                {
                    'id': serializer.data.get('id', None),
                    'username': serializer.data.get('username', None),
                    'first_name': serializer.data.get('first_name', None),
                    'last_name': serializer.data.get('last_name', None),
                    'is_active': serializer.data.get('is_active', None),
                    'last_login': serializer.data.get('last_login', None),
                    'is_superuser': serializer.data.get('is_superuser', None),
                },
                status=status.HTTP_201_CREATED,
            )


    def delete(self, request, *args, **kwargs):
        # Get object with this pk
        try:
            pk = kwargs['pk']
        except KeyError:
            raise serializers.ValidationError('"DELETE" requests avialable only with urls contains PrimaryKey')
        else:
            user = CustomUser.objects.get(id=pk)
            user.delete()

            return Response({
                    "message": f"User with username `{user}` has been deleted."
                }, status=204)


    def patch(self, request, **kwargs):
        try:
            pk = kwargs['pk']
        except KeyError:
            raise serializers.ValidationError('"PATCH" requests avialable only with urls contains PrimaryKey')
        else:
            data = request.data
            saved_user = CustomUser.objects.get(pk=pk)
            serializer = WriteOnlyUserSerializer(instance=saved_user, data=data, partial=True)

            if serializer.is_valid(raise_exception=True):
                saved_user = serializer.save()

                return Response({
                    "success": f"User with username '{saved_user}' patched successfully"})
            return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, format=None, **kwargs):
        """
        Functionality for 'PUT' requests is under construction.
        Will be realized soon.
        """

        return Response({
                "message": "Sorry, but 'PUT' requests are currently unavailable, will be realized in the next updates."
            })
