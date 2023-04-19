from rest_framework import serializers

class MessageSerializer(serializers.Serializer) :
    signInMethod = serializers.CharField()