from rest_framework import serializers
from manager_task.models import Task


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'user', 'task_name', 'added_on', 'complete_by', 'completed', 'is_deleted' )