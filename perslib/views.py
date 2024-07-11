from django.shortcuts import render

from .models import Year, Title, Perslib
from .serializers import YearSerializer, TitleSerializer, PerslibSerializer

from rest_framework import viewsets
from rest_framework import permissions

# from rest_framework.settings import api_settings

# from rest_framework.permissions import IsAuthenticated

# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status

# from rest_framework.parsers import MultiPartParser, FormParser, JSONParser

#Note: ReadOnlyModelViewSet only provide 'read-only' actions:list & .retrieve(). But, ModelViewSet on the otherhand provides the actions: .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().

class YearViewSet(viewsets.ModelViewSet):
  #Note: If ReadOnlyModelViewSet is used in place of ModelViewSet, it does not allow editing! If checked by postman,POST & PUT will not succeed to create or change anything.
  queryset = Year.objects.all()
  serializer_class = YearSerializer
  permission_classes = [permissions.AllowAny]
  


#First show page (Titles):
class TitleViewSet(viewsets.ModelViewSet):   
  queryset = Title.objects.all()
  serializer_class = TitleSerializer
  permission_classes = [permissions.AllowAny]
      

#Second show page (Perlib):
class PerslibViewSet(viewsets.ModelViewSet):              
  queryset = Perslib.objects.all()
  serializer_class = PerslibSerializer
  permission_classes = [permissions.AllowAny]
  # parser_classes = (MultiPartParser, FormParser, JSONParser)
 

 
