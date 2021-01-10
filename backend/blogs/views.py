from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

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
            # posts = serializer.validated_data['title', 'description']
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

    def put(pk, request):
        try: 
            BlogById = Blog.objects.get(pk=blogId)  
        except BlogById.DoesNotExist: 
            return JsonResponse({'message': 'The Blog Post does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        if request.method == 'PUT': 
            serializer = BlogSerializer(data=BlogById)
            serializer.save()
            return Response(status.HTTP_200_OK, "Blog Post Added") 

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def delete(pk, request):
        try: 
            BlogById = Blog.objects.get(pk=blogId)  
        except BlogById.DoesNotExist: 
            return JsonResponse({'message': 'The Blog Post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        if request.method == 'DELETE':
            BlogById.delete() 
            return JsonResponse({'message': 'Blog Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        


