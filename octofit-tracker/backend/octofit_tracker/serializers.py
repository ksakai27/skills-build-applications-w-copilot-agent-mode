from rest_framework import serializers
from .models import Team, User, Activity, Workout, Leaderboard

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)
    def to_internal_value(self, data):
        return data

class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    team = ObjectIdField()
    class Meta:
        model = User
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    user = ObjectIdField()
    class Meta:
        model = Activity
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    # suggested_for is a list of ObjectIds; represent it with a ListField whose child is ObjectIdField
    suggested_for = serializers.ListField(child=ObjectIdField())
    class Meta:
        model = Workout
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)
    team = ObjectIdField()
    class Meta:
        model = Leaderboard
        fields = '__all__'
