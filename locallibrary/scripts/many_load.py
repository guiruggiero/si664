import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, States, Region, ISO, Site

def run():
    fhand = open('unesco/load.csv')
    reader = csv.reader(fhand)
    next(reader)

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    ISO.objects.all().delete()
    Site.objects.all().delete()

    # Format
    # name,description,justification,year,longitude,latitude,
    #   area_hectares,category,states,region,iso

    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        st, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = ISO.objects.get_or_create(name=row[10])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lo = float(row[4])
        except:
            lo = None

        try:
            la = float(row[5])
        except:
            la = None

        try:
            ah = float(row[6])
        except:
            ah = None

        si = Site(name=row[0], description=row[1], justification=row[2], year=y, longitude=lo, latitude=la, area_hectares=ah, category=c, states=st, region=r, iso=i)
        si.save()