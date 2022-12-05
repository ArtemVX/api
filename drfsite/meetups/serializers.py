from rest_framework import serializers

from meetups.models import MeetUp


class MeetUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetUp
        fields = ("title", "slug", "description", 'organizer_email')  # list or __all__


# using Serializer class
# class MeetUpSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     slug = serializers.SlugField()
#     description = serializers.CharField()
#     organizer_email = serializers.EmailField()
#
#     def create(self, validated_data):
#         return MeetUp.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.slug = validated_data.get('slug', instance.title)
#         instance.description = validated_data.get('description', instance.title)
#         instance.organizer_email = validated_data.get('organizer_email', instance.title)
#         instance.save()
#         return instance

