from collections import OrderedDict
from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'question', 'answer', 'box', 'date_created')

    def create(self, validated_data):
        card = Card(
            question=validated_data['question'],
            answer=validated_data['answer'],
            box=validated_data['box']
        )
        card.save()
        return card

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.box = validated_data.get('box', instance.box)
        instance.save()
        return instance

