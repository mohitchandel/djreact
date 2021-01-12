from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from .models import Blog, Author
from .serializers import BlogSerializer, AuthorSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

class AuthorListView(GenericAPIView):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        objects = Author.objects.all()
        serializer = AuthorSerializer(objects, many=True)
        return Response(serializer.data)


class BlogListView(GenericAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request):
        objects = Blog.objects.all()
        serializer = BlogSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status.HTTP_200_OK) 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(GenericAPIView): 

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, pk, *args, **kwargs):
        objects = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(objects)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        objects = Blog.objects.get(pk=pk)
        Postobjects = JSONParser().parse(request) 
        serializer = BlogSerializer(objects, data=Postobjects)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, *args, **kwargs):
        objects = Blog.objects.get(pk=pk)
        objects.delete()
        return Response(status.HTTP_200_OK)
        


