from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from user_profile.api.serializers import ContactSerializer
from user_profile.models import Contact


class ContactList(APIView):
    #permission_classes = [IsAuthenticated]

    queryset = Contact.objects.none()

    def get(self, request: Request) -> Response:
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ValidationEmail(APIView):

    def generateURL(self):
        url = f'aaa'
