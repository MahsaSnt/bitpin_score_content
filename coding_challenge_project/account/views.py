from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle

from .serializers import SignUpSerializer, UserSerializer


@permission_classes((AllowAny,))
@throttle_classes([AnonRateThrottle])
class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data=UserSerializer(serializer.instance).data,
            status=status.HTTP_201_CREATED,
        )
