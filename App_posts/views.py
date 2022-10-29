from turtle import pos
from django.http import Http404

from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters

from .serializers import  PostSerializer, PostRetrieveSerializer
from .models import Post


class PostsPagination(PageNumberPagination):
    page_size = 2


class PostsViewSet(viewsets.ModelViewSet):
    
    pagination_class = PostsPagination
    posts = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title','content',)
    
    @action(detail=True, methods=['get'])
    def show(self, request, pk=None):
        post = self.get_object()
        
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)   
        
    def perform_update(self, serializer):
        post = self.get_object()
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.posts
    



# class PostsPIView(GenericAPIView):
#     """
#     Retrieve, update or delete a Post instance.
#     """
#     # pagination_class = PostsPagination
    
    
    
#     def get_object(self, pk):
#         try:
#             return Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
    
#     def get(self, request, format=None):
        
#         if(self.request.query_params):
#             try:
#                 post = self.get_object(self.request.query_params['id'])
#             except:
#                 raise Http404
#             serializer = PostRetrieveSerializer(post)
#             return Response(serializer.data)
#         else:
#             posts = Post.objects.all()
#             serializer = PostRetrieveSerializer(posts, many=True)
#             return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():                    
#             serializer.save(created_by=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def put(self, request, format=None):
        
#         try:
#             post = self.get_object(self.request.query_params['id'])
#         except:
#             raise Http404
        
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, format=None):
        
#         try:
#             post = self.get_object(request.query_params['id'])
#         except:
#             raise Http404

#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    