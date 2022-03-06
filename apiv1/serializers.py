from abc import ABC

from rest_framework import serializers

from shop.models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    # author_name = serializers.SerializerMethodField()
    # author = SimpleAuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']

    def get_author_name(self, instance):
        return instance.author.name


class SimpleBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'price', ]


class AuthorSerializer(serializers.ModelSerializer):
    book_set = SimpleBookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'book_set']


class SimpleAuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['name', ]
