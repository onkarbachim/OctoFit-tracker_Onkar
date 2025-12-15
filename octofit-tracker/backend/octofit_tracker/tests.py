from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30)
        self.workout = Workout.objects.create(user=self.user, name='Test Workout', description='Test Desc')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team.name, 'Test Team')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.duration, 30)

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
