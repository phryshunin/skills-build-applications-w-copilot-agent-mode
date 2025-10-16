from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = []
        user_data = [
            {'name': 'Tony Stark', 'email': 'tony@marvel.com', 'team': marvel, 'is_superhero': True},
            {'name': 'Steve Rogers', 'email': 'steve@marvel.com', 'team': marvel, 'is_superhero': True},
            {'name': 'Bruce Wayne', 'email': 'bruce@dc.com', 'team': dc, 'is_superhero': True},
            {'name': 'Clark Kent', 'email': 'clark@dc.com', 'team': dc, 'is_superhero': True},
        ]
        for data in user_data:
            user = User(**data)
            user.save()
            users.append(user)

        # Create activities
        for user in User.objects.all():
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, points=50)
            Activity.objects.create(user=user, activity_type='Strength', duration_minutes=45, points=70)

        # Create workouts
        for user in User.objects.all():
            Workout.objects.create(user=user, workout_type='Cardio', description='Morning run', date='2025-10-15')
            Workout.objects.create(user=user, workout_type='Weights', description='Gym session', date='2025-10-16')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=240, month='October 2025')
        Leaderboard.objects.create(team=dc, total_points=240, month='October 2025')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
