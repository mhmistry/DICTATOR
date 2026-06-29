# generator/management/commands/load_wordlist.py
from django.core.management.base import BaseCommand
from generator.models import Password
import re
import os

class Command(BaseCommand):
    help = 'Load master_wordlist.txt from project root'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            nargs='?',
            default='master_wordlist.txt',
            help='Wordlist file in project root (default: master_wordlist.txt)'
        )

    def handle(self, *args, **options):
        filename = options['filename']
        file_path = filename  # Already in root

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
            return

        # Clear DB
        Password.objects.all().delete()
        self.stdout.write('Cleared existing passwords...')

        batch = []
        batch_size = 5000
        total_loaded = 0

        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                word = line.strip()
                if word:
                    batch.append(Password(
                        word=word,
                        length=len(word),
                        has_upper=bool(re.search(r'[A-Z]', word)),
                        has_lower=bool(re.search(r'[a-z]', word)),
                        has_digit=bool(re.search(r'\d', word)),
                        has_symbol=bool(re.search(r'[^A-Za-z0-9]', word))
                    ))

                    if len(batch) >= batch_size:
                        Password.objects.bulk_create(batch, ignore_conflicts=True)
                        total_loaded += len(batch)
                        batch.clear()

                    if line_num % 500_000 == 0:
                        self.stdout.write(f'Processed {line_num:,} lines...')

            if batch:
                Password.objects.bulk_create(batch, ignore_conflicts=True)
                total_loaded += len(batch)

        self.stdout.write(self.style.SUCCESS(
            f'Loaded {total_loaded:,} passwords from {file_path}!'
        ))