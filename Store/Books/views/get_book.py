#Genric
from Books.serializers import UpdateBookSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# All Serializers
from ..models import Book
from util.global_response import success_response,error_response
from util import messages

class GetBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    queryset = Book.objects.all()
    def get(self, request,id):
        try:
            if Book.objects.filter(id=id).exists():
                get_book=Book.objects.filter(id=id).values('id','category_id','name','file_url')
                print(get_book)
                if get_book:
                    success_response.update(result = get_book, code = status.HTTP_200_OK)
                    return Response(success_response, status = status.HTTP_200_OK)
                else:
                    error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['GET_ERROR'])
                    return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
            else:
                error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['ID_NOT_EXIST'])
                return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)