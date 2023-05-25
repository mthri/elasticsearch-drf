from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    def handle(self, *args, **options):
        for group_name in ['sale', 'support']:
            if not Group.objects.filter(name=group_name).exists():
                Group.objects.create(name=group_name)
