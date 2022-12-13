from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('id', 'title', 'content', 'date_created')

    def create(self, validated_data):
        obj = Entry(
            title=validated_data['title'],
            content=validated_data['content']
        )
        obj.save()

        return obj

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
