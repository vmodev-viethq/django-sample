from rest_framework import serializers

from polls.models import Poll


class PollCreateBodySerializer(serializers.Serializer):
    poll_name = serializers.CharField()
    description = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        return Poll.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.poll_name = validated_data.get("poll_name", instance.poll_name)
        instance.description = validated_data.get("poll_name", instance.description)
        instance.save()
        return instance


class PollSerializer(PollCreateBodySerializer):
    id = serializers.IntegerField()


class PollModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"
