from rest_framework import serializers

def MessageSerializer(serializers.Serializer) :
    signInMethod = serializers.CharField()