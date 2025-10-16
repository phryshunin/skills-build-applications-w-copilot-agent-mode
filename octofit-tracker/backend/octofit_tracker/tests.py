from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        self.assertEqual(team.name, 'Test Team')

    def test_user_creation(self):
        team = Team.objects.create(name='Test Team', description='A team for testing')
        user = User.objects.create(name='Test User', email='test@example.com', team=team, is_superhero=False)
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.team.name, 'Test Team')
