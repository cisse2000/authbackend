from .serializers import DocumentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Document


class DocumentAPIView(APIView):
    """
    Retrieve, update or delete a Document instance.
    """
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        
        if(self.request.query_params):
            try:
                document = self.get_object(self.request.query_params['id'])
            except:
                raise Http404
            serializer = DocumentSerializer(document)
            return Response(serializer.data)
        else:
            documents = Document.objects.all()
            serializer = DocumentSerializer(documents, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():                    
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        
        try:
            document = self.get_object(self.request.query_params['id'])
        except:
            raise Http404
        
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        
        try:
            document = self.get_object(self.request.query_params['id'])
        except:
            raise Http404
        
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)