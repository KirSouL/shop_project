import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@yandex.ru",
            first_name="Admin",
            last_name="Yandex",
            is_staff=True,
            is_active=True,
            is_superuser=True
        )
        admin_password = os.getenv('admin_password')
        user.password(admin_password)
        user.save()
