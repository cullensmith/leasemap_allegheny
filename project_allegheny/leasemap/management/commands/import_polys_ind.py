import csv
from django.core.management.base import BaseCommand
from leasemap.models import PolyModel
# from datetime import datetime

class Command(BaseCommand):
    help = 'Imports books from a CSV file'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_file', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = 'E:\\CMapS\\fractracker\\project_data\\allegheny/unique_u255.csv'

        # Open and read the CSV file
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = row['id']
                pin = row['pin']
                geomjson = row['geomjson']

                # # Parse the date string into a Date object
                # try:
                #     published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
                # except ValueError:
                #     self.stdout.write(self.style.ERROR(f"Invalid date format for book: {title}"))
                #     continue

                # Create and save the book record
                well, created = PolyModel.objects.get_or_create(
                    id=id,
                    pin=pin,
                    geomjson=geomjson
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added book: {id}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Book already exists: {id}"))