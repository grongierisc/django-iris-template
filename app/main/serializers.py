from rest_framework import serializers
from main.models import CommunityComment, CommunityPost, CommunityTag, IrisDemo

class CommunityCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityComment
        fields = '__all__'

class CommunityPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityPost
        fields = '__all__'

class CommunityTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityTag
        fields = '__all__'

class IrisDemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IrisDemo
        fields = '__all__'