from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Case, When, IntegerField, Sum, Avg

from .models import Content
from .serializers import (
    CreateUpdateScoreSerializer,
    ContentListSerializer,
)


@permission_classes((IsAuthenticated, ))
class CreateUpdateScoreView(generics.CreateAPIView):
    serializer_class = CreateUpdateScoreSerializer


class ContentListView(generics.ListAPIView):
    serializer_class = ContentListSerializer
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    search_fields = (
        'title',
    )
    ordering_fields = (
        'total_vote',
        'average_score',
        'id',
    )
    filterset_fields = (
        'title',
        'score__user__username',
        'id',
    )

    def get_queryset(self):
        user = self.request.user
        if user:
            user_id = user.id
        else:
            user_id = None
        queryset = Content.objects.annotate(
            total_vote=Count('score', distinct=True),
            average_score=Avg('score__number', distinct=True),
            my_score_number=Sum(
                Case(
                    When(score__user=user_id, then='score__number'),
                    default=None,
                    output_field=IntegerField(),
                ),
                distinct=True),
        )
        return queryset
