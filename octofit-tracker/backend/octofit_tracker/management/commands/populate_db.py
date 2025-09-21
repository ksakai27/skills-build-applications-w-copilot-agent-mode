from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes team')
        dc = Team.objects.create(name='DC', description='DC superheroes team')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel, is_leader=True),
            User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel),
            User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc, is_leader=True),
            User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, calories_burned=300, date=date.today())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, calories_burned=400, date=date.today())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, calories_burned=500, date=date.today())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, calories_burned=200, date=date.today())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        w1 = Workout.objects.create(name='Super Strength', description='Strength workout for heroes')
        w2 = Workout.objects.create(name='Flight Training', description='Aerobic workout for flyers')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        self.stdout.write(self.style.SUCCESS('Creating leaderboard...'))
        Leaderboard.objects.create(team=marvel, total_points=700, rank=1)
        Leaderboard.objects.create(team=dc, total_points=600, rank=2)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
