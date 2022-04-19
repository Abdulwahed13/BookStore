from distutils.command.upload import upload
from unicodedata import category
from Books.models.book import Book
from Books.models.book_category import BookCategory
from rest_framework import fields, serializers
from util import messages


class AddBookSerializer(serializers.Serializer):
    name = serializers.CharField()
    category_id= serializers.CharField()
    data_file=serializers.FileField()
    #For Required field validation start
    def __init__(self, *args, **kwargs):
        super(AddBookSerializer, self).__init__(*args, **kwargs) # call the super()
        for field in self.fields: # iterate over the serializer fields
            self.fields[field].error_messages['blank'] = field.title().replace("_", " ")+messages.ERROR['FIELD_REQUIRED']
    #For Required field validation end
    def validate(self, data):
        errors = {}
        if not BookCategory.objects.filter(id=data.get('category_id')).exists():
            errors['topic_id'] = [messages.ERROR['ID_NOT_EXIST']]
        if len(errors) > 0:
            raise serializers.ValidationError(errors)
        else:
            return data


class UpdateBookSerializer(serializers.Serializer):
    id=serializers.CharField()
    name = serializers.CharField(required=False,allow_blank=True)
    category_id=serializers.CharField(required=False,allow_blank=True)
    file_url=serializers.FileField()

    def __init__(self, *args, **kwargs):
        super(UpdateBookSerializer, self).__init__(*args, **kwargs) # call the super()
        for field in self.fields: # iterate over the serializer fields
            self.fields[field].error_messages['blank'] = field.title().replace("_", " ")+messages.ERROR['FIELD_REQUIRED']
    # For Required field validation end
    def validate(self, data):
        errors = {}
        if "category_id" in data and data.get('category_id'):
            if not BookCategory.objects.filter(id=data.get('category_id')).exists():
                errors['cateogry_id'] = [messages.ERROR['ID_NOT_EXIST']]

        if not Book.objects.filter(id=data.get('id')).exists():
            errors['id'] = [messages.ERROR['ID_NOT_EXIST']]

        if len(errors) > 0:
            raise serializers.ValidationError(errors)
        else:
            return data





    