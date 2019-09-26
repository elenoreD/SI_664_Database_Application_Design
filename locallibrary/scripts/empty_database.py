import csv

from unesco.models import Site, Category, States, Region, Iso

def run():

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()


