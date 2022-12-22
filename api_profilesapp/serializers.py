from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing APIView"""
    first_name = serializers.CharField(max_length=32, min_length=2) 
    last_name = serializers.CharField(max_length=32, min_length=2)
