from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# All Serializers
from ..serializers import AddBookSerializer
from ..models import Book
from util.global_response import success_response,error_response
from util import messages
class AddBook(generics.GenericAPIView):
    serializer_class = AddBookSerializer
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                add_book=Book.objects.create(name=request.data['name'],category_id=request.data['category_id'],file_url=request.data['data_file'])
                if add_book:
                    success_response.update(result = messages.SUCCESS['ADD_BOOK'], code = status.HTTP_200_OK)
                    return Response(success_response, status = status.HTTP_200_OK)
                else:
                    error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['ADD_ERROR'])
                    return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
            else:
                #Only One Error shoule be shown at a time.
                error, *_ = serializer.errors.values()
                error_response.update(code = status.HTTP_400_BAD_REQUEST, message = error, errors = serializer.errors)
                return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
            
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)