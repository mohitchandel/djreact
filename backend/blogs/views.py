from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

class BlogListView(GenericAPIView):
    
    queryset = 

    serializer_class = BlogSerializer

    def get(self, request):
        objects = Blog.objects.all()
        serializer = BlogSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=self.request.data)
        if serializer.is_valid():
            posts = serializer.validated_data['title']
            return Response(status.HTTP_200_OK) 

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        


