from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Criar grupos: Uploader, Leitor, Pending"

    def handle(self, *args, **options):
        for name in ("Uploader", "Leitor", "Pending"):
            g, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Grupo criado: {name}"))
            else:
                self.stdout.write(f"Grupo já existe: {name}")
