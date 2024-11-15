from django.core.management.base import BaseCommand
from apps.home.models import User, Company, UserProfile
from django.db import IntegrityError


class Command(BaseCommand):
    help = 'Seeds initial data into the database'

    def handle(self, *args, **kwargs):
        # Check if the user already exists
        user, created = User.objects.get_or_create(
            username='system',
            defaults={'email': 'system@example.com', 'password': 'password123'}
        )

        if created:
            self.stdout.write(self.style.SUCCESS('User created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('User already exists'))

        # Check if the company exists, otherwise create it
        company, created = Company.objects.get_or_create(
            name="HelloWorld Company")

        if created:
            self.stdout.write(self.style.SUCCESS(
                'Company created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Company already exists'))

        # Create UserProfile if not already created
        profile, created = UserProfile.objects.get_or_create(
            user=user, company=company)

        if created:
            self.stdout.write(self.style.SUCCESS(
                'UserProfile created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('UserProfile already exists'))

        self.stdout.write(self.style.SUCCESS(
            'Successfully seeded initial data'))
