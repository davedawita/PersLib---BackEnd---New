
from .models import Year
from .models import Title
from .models import Perslib
from django.contrib.auth.models import User, Group

from rest_framework import serializers


class YearSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Year
    fields = ['id', 'year'] 

class TitleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Title
    fields = ['id', 'title']  # Here, the type of data is tuple. "Python tuples" store data that should not be modified. Note that the comma is needed if not it would have been a string.


class PerslibSerializer(serializers.HyperlinkedModelSerializer):    #The HyperlinkedModelSerializer class is similar to the ModelSerializer class except that it uses hyperlinks to represent relationships between entities in web API design, rather than primary keys.
  image_url = serializers.ImageField(required=False)
  class Meta:
    model = Perslib
    fields = ['id', 'image_url', 'description', 'date', 'time']