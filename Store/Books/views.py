# import code
# from dataclasses import field
# from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .models import Book
# from django.http import HttpResponse
# Create your views here.

# def b_list(request):
#     return render(request, 'Books/bforms.html')

# class BookCreate(CreateView):
#     model=Book
#     fields = ['name']

#Genric
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# All Serializers
from .serializers import AddBookSerializer,UpdateBookSerializer
from .models import Book
class AddBook(generics.GenericAPIView):
    serializer_class = AddBookSerializer
    def post(self, request):
        try:
            add_book=Book.objects.create(name=request.data['name'],category_id=request.data['category_id'])
            if add_book:
                return Response({'result':'The Book has been added succesfully', 'code' : status.HTTP_200_OK})
            else:
                return Response({'error':'There is some error', 'code' : status.HTTP_400_BAD_REQUEST})
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)

class UpdateBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    def put(self, request):
        try:
            update_book=Book.objects.filter(id=request.data['id']).update(name=request.data['name'],category_id=request.data['category_id'])
            if update_book:
                return Response({'result':'The Book has been udated succesfully', 'code' : status.HTTP_200_OK})
            else:
                return Response({'error':'There is some error', 'code' : status.HTTP_400_BAD_REQUEST})
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)

class GetBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    def get(self, request,id):
        try:
            get_book=Book.objects.filter(id=id).values('id','category_id','name')
            print(get_book)
            if get_book:
                return Response({'result':get_book, 'code' : status.HTTP_200_OK})
            else:
                return Response({'error':'There is some error', 'code' : status.HTTP_400_BAD_REQUEST})
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)

class DeleteBook(generics.GenericAPIView):
    serializer_class = UpdateBookSerializer
    def delete(self, request,id):
        try:
            delete_book=Book.objects.filter(id=id).delete()
            print(delete_book)
            if delete_book:
                return Response({'result': 'The book has been deleted succesfully', 'code' : status.HTTP_200_OK})
            else:
                return Response({'error':'There is some error', 'code' : status.HTTP_400_BAD_REQUEST})
        except Exception as error:
            return Response({"exception":str(error)}, status = status.HTTP_400_BAD_REQUEST)

