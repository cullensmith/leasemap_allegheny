import csv
from django.core.management.base import BaseCommand
from leasemap.models import Parceldetails2
# from datetime import datetime

class Command(BaseCommand):
    help = 'Imports books from a CSV file'

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_file', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = 'E:\\CMapS\\fractracker\\project_data\\allegheny/parcel_docdetails_u255.csv'

        # Open and read the CSV file
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # id = row['id']
                pin = row['pin']
                geomjson = row['geomjson']
                doc_num = row['doc_num']
                company = row['company']
                file_date = row['file_date']
                agmt_type = row['agmt_type']
                dv_url = row['dv_url']
                classdesc = row['classdesc']
                schooldesc = row['schooldesc']
                munidesc = row['munidesc']
                bk_vol_pg = row['bk_vol_pg']
                usedesc = row['usedesc']
                calcacreag = row['calcacreag']
                fairmarkettotal = row['fairmarkettotal']
                geomjson = row['geomjson']

                # # Parse the date string into a Date object
                # try:
                #     published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
                # except ValueError:
                #     self.stdout.write(self.style.ERROR(f"Invalid date format for book: {title}"))
                #     continue

                # Create and save the book record
                well, created = Parceldetails2.objects.get_or_create(
                    # id=id,
                    pin=pin,
                    geomjson=geomjson,
                    doc_num = doc_num,
                    company = company,
                    file_date = file_date,
                    agmt_type = agmt_type,
                    dv_url = dv_url,
                    classdesc = classdesc,
                    schooldesc = schooldesc,
                    munidesc = munidesc,
                    bk_vol_pg = bk_vol_pg,
                    usedesc = usedesc,
                    calcacreag = calcacreag,
                    fairmarkettotal = fairmarkettotal
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added book: {doc_num}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Book already exists: {doc_num}"))