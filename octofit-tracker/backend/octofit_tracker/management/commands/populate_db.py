from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='ironman', email='tony@marvel.com', password='pass', team=marvel)
        steve = User.objects.create_user(username='captain', email='steve@marvel.com', password='pass', team=marvel)
        bruce = User.objects.create_user(username='hulk', email='bruce@marvel.com', password='pass', team=marvel)
        clark = User.objects.create_user(username='superman', email='clark@dc.com', password='pass', team=dc)
        bruce_dc = User.objects.create_user(username='batman', email='bruce@dc.com', password='pass', team=dc)
        diana = User.objects.create_user(username='wonderwoman', email='diana@dc.com', password='pass', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30)
        Activity.objects.create(user=steve, type='cycle', duration=45)
        Activity.objects.create(user=bruce, type='swim', duration=60)
        Activity.objects.create(user=clark, type='run', duration=50)
        Activity.objects.create(user=bruce_dc, type='cycle', duration=40)
        Activity.objects.create(user=diana, type='swim', duration=55)

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_team=marvel)
        Workout.objects.create(name='Strength Training', description='Strength for DC heroes', suggested_for_team=dc)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=135)
        Leaderboard.objects.create(team=dc, points=145)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))

# Models for reference (should be in octofit_tracker/models.py):
# class Team(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
# class Activity(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = models.CharField(max_length=50)
#     duration = models.IntegerField()
#
# class Workout(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     suggested_for_team = models.ForeignKey(Team, on_delete=models.CASCADE)
#
# class Leaderboard(models.Model):
#     team = models.ForeignKey(Team, on_delete=models.CASCADE)
#     points = models.IntegerField()
