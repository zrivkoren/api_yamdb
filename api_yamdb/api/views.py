from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from api.serializers import ReviewSerializer, CommentSerializer
from reviews.models import Title


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Title, id=title_id).reviews.all()

    def perform_create(self, serializer):  # to do
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        review_id = self.kwargs.get('review_id')

        reviews_in_title = get_object_or_404(Title, id=title_id).reviews.all()
        return get_object_or_404(reviews_in_title, id=review_id).comments.all()

    def perform_create(self, serializer):  # to do
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)
