from rest_framework import serializers

from .models import ToDoList, ToDoItem


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ('id', 'title')

    def create(self, validated_data):
        todo_list = ToDoList(title=validated_data['title'])
        todo_list.save()
        return todo_list

    def to_representation(self, instance):
        todo_items = ToDoItem.objects.filter(todo_list=instance)
        representation = super().to_representation(instance)
        representation['items'] = ToDoItemSerializer(todo_items, many=True, context=self.context).data
        return representation


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ('id', 'title', 'description', 'created_date', 'due_date', 'todo_list')

    def create(self, validated_data):
        todo_item = ToDoItem(
            title=validated_data['title'],
            description=validated_data['description'],
            due_date=validated_data.get('due_date', None),
            todo_list=validated_data.get('todo_list')
        )
        todo_item.save()

        return todo_item

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.todo_list = validated_data.get('todo_list', instance.todo_list)
        instance.save()

        return instance
