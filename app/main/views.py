from rest_framework import viewsets
from main.models import CommunityComment, CommunityPost, CommunityTag, IrisDemo

from main.serializers import CommunityCommentSerializer, CommunityPostSerializer, CommunityTagSerializer, IrisDemoSerializer

class CommunityCommentViewSet(viewsets.ModelViewSet):
    queryset = CommunityComment.objects.all()
    serializer_class = CommunityCommentSerializer

class CommunityPostViewSet(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all()
    serializer_class = CommunityPostSerializer

class CommunityTagViewSet(viewsets.ModelViewSet):
    queryset = CommunityTag.objects.all()
    serializer_class = CommunityTagSerializer

class IrisDemoViewSet(viewsets.ModelViewSet):
    queryset = IrisDemo.objects.all()
    serializer_class = IrisDemoSerializer