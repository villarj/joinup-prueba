from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

class UserProfileSelect(APIView):
    #permission_classes = [IsAuthenticated]

    #queryset = Ship.objects.none()

    def get(self, request: Request) -> Response:
        #ships = Ship.objects.all().only('name')
        resp = {
            "a":"Javier",
            "b": "pepe"
        }
        #serializer = ShipSelectSerializer(ships, many=True)
        return Response(resp, status.HTTP_200_OK)