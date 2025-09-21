from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A test team')
        self.assertEqual(str(team), 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team2', description='A test team')
        user = User.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'test@example.com')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team3', description='A test team')
        user = User.objects.create(name='Test User2', email='test2@example.com', team=team)
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, calories_burned=200, date='2025-09-21')
        self.assertEqual(str(activity), 'test2@example.com - Run')

    def test_workout_creation(self):
        team = Team.objects.create(name='Test Team4', description='A test team')
        workout = Workout.objects.create(name='Test Workout', description='A test workout')
        workout.suggested_for.set([team])
        self.assertEqual(str(workout), 'Test Workout')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team5', description='A test team')
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, rank=1)
        self.assertEqual(str(leaderboard), 'Test Team5 - 1')
