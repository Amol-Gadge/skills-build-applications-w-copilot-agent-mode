from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='pass', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for_team=self.team)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Test Workout')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
