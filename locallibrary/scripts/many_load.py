import csv

from unesco.models import Site, Category, States, Region, Iso

def run():

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()

    fn=open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fn)
    next(reader)



    for elements in reader:
        #print(elements)

        c, created = Category.objects.get_or_create(name=elements[7])
        s, created = States.objects.get_or_create(name=elements[8])
        r, created = Region.objects.get_or_create(name=elements[9])
        i, created = Iso.objects.get_or_create(name=elements[10])
        try:
            y = int(elements[3])
        except:
            y = None
        try:
            l = float(elements[4])
        except:
            l = None

        try:
            a = float(elements[5])
        except:
            a = None


        try:
            ar = float(elements[6])
        except:
            ar = None


        site= Site(name=elements[0], description=elements[1], justification=elements[2], year=y, longitude=l, latitude=a, area_hectares=ar, category=c, states=s, region=r, iso=i)
        site.save()


