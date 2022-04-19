from Books.models.book import Book
from Books.serializers import UpdateBookSerializer
from rest_framework import generics,status,viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView
from ..pagination import CustomPagination

class ListBook(ListAPIView):
    serializer_class = UpdateBookSerializer
    queryset=Book.objects.all()
    pagination_class=CustomPagination
    # def get(self,request):
    #     pagination_class = CustomPagination
    #     get_book=Book.objects.filter(is_delete=False).values()
    #     return Response({'result':get_book, 'code' : status.HTTP_200_OK})
