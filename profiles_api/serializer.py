from rest_framework import serializers

# second one after . is the base class so capital S
class HelloSerializer(serializers.Serializer):
    """Serializer a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)