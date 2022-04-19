#Genric
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# All Serializers
from ..serializers import UpdateBookSerializer
from ..models import Book
from util.global_response import success_response,error_response
from util import messages
import os


class UpdateBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    def put(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                if "name" in request.data and request.data['name']:
                    update_book=Book.objects.filter(id=request.data['id']).update(name=request.data['name'])
                if "category_id" in request.data and request.data['category_id']:
                    update_book=Book.objects.filter(id=request.data['id']).update(name=request.data['category_id'])
                if Book.objects.filter(id=request.data['id']).values('file_url').exists():
                    var_name=Book.objects.filter(id=request.data['id']).values('file_url')
                    filepath="C:/Users/abdul/Saved Games/Store/media/{}".format(var_name[0]['file_url'])
                    filepath=filepath.replace('os.sep','/')
                    os.remove(filepath)
                    update_book=Book.objects.filter(id=request.data['id']).update(file_url=request.data['file_url'])
                    # update_book=Book.objects.filter(id=request.data['id']).create(file_url=request.data['file_url'])

                if update_book:
                    success_response.update(result = messages.SUCCESS['UPDATE_BOOK'], code = status.HTTP_200_OK)
                    return Response(success_response, status = status.HTTP_200_OK)
                else:
                    error_response.update(code = status.HTTP_400_BAD_REQUEST, message = messages.ERROR['UPDATE_ERROR'])
                    return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
            else:
                #Only One Error shoule be shown at a time.
                error, *_ = serializer.errors.values()
                error_response.update(code = status.HTTP_400_BAD_REQUEST, message = error, errors = serializer.errors)
                return Response(error_response, status = status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)
