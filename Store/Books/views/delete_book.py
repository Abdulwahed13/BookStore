#Genric
from Books.serializers import UpdateBookSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# All Serializers
from ..models import Book
from util.global_response import success_response,error_response
from util import messages

class DeleteBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    def delete(self, request,id):
        try:
            if Book.objects.filter(id=id).exists():
                delete_book=Book.objects.filter(id=id).delete()
                print(delete_book)
                if delete_book:
                    success_response.update(result = messages.SUCCESS['DELETE_BOOK'], code = status.HTTP_200_OK)
                    return Response(success_response, status = status.HTTP_200_OK)
                else:
                    error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['DELETE_ERROR'])
                    return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
            else:
                error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['ID_NOT_EXIST'])
                return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)