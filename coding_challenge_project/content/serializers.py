from rest_framework import serializers

from .models import Content, Score
from .exceptions import NotExistContentException


class CreateUpdateScoreSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1, max_value=5)
    content_id = serializers.IntegerField()

    def validate_content_is(self, content_id):
        if not Content.objects.filter(id=content_id):
            raise NotExistContentException

    def save(self, *args, **kwargs):
        request = self.context.get('request')
        score_obj, _ = Score.objects.get_or_create(
            user=request.user,
            content_id=self.validated_data.get('content_id')
        )
        score_obj.number = self.validated_data.get('number')
        score_obj.save()
        return score_obj


class ContentListSerializer(serializers.ModelSerializer):
    total_vote = serializers.IntegerField()
    average_score = serializers.IntegerField()
    my_score_number = serializers.IntegerField()

    class Meta:
        model = Content
        exclude = ('text', )

