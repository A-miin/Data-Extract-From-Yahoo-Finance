from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class APIDataView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        company = request.GET['company']
        return Response(status=status.HTTP_200_OK)
