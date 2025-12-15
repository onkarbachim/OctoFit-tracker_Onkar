from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create Teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create Users
        users = [
            app_models.User.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            app_models.User.objects.create(email='captain@marvel.com', name='Captain America', team=marvel),
            app_models.User.objects.create(email='batman@dc.com', name='Batman', team=dc),
            app_models.User.objects.create(email='superman@dc.com', name='Superman', team=dc),
        ]

        # Create Activities
        for user in users:
            app_models.Activity.objects.create(user=user, type='Running', duration=30)
            app_models.Activity.objects.create(user=user, type='Cycling', duration=45)

        # Create Workouts
        for user in users:
            app_models.Workout.objects.create(user=user, name='Morning Cardio', description='Cardio session')

        # Create Leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=200)
        app_models.Leaderboard.objects.create(team=dc, points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
