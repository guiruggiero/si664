from django.db import models

# When updated, update also:
#  - dbdiagram.io/Divelog-MVP
#  - export Divelog-MVP.sql
#  - si507/finalproject/classes.py

'''
Questions/answers
- fields with choices here or on forms? to speed MVP do it in models, Django will autopopulate dropdowns from it :-)
    https://docs.djangoproject.com/en/2.2/topics/db/models/#field-options
- validate with ads/models.py
- only show logs from the user (where is this?!): all() --> filter(owner=request.user)
'''

class Dive(models.Model):
    diver = models.ForeignKey('Diver', on_delete=models.CASCADE)
    site = models.ForeignKey('Site', on_delete=models.SET_NULL)
    start_date = models.DateField(blank=False)
    start_time = models.TimeField(blank=False)
    total_time = models.PositiveSmallIntegerField(blank=False)
    max_depth = models.FloatField(blank=False)
    start_pressure = models.PositiveSmallIntegerField()
    end_pressure = models.PositiveSmallIntegerField()
    surface_temp = models.FloatField()
    bottom_temp = models.FloatField()
    equipment = models.ManyToManyField('Equipment')
    weights = models.PositiveSmallIntegerField()
    dive_center = models.CharField(max_length=255)
    boat = models.CharField(max_length=255)
    structures = models.TextField()
    animals = models.TextField()
    rating = models.PositiveSmallIntegerField()
    favorite = models.BooleanField(default=False)
    photo_album = models.CharField(max_length=255)
    notes = models.TextField()
    validated = models.BooleanField(default=False)
    gas = models.CharField(max_length=255)
    share_oxygen = models.FloatField()
    share_nitrogen = models.FloatField()
    share_helium = models.FloatField()
    surface_supplied = models.BooleanField(default=False)
    transportation = models.CharField(max_length=255) # boat, shore, etc.
    water = models.CharField(max_length=255) # salty, fresh, etc.
    body = models.CharField(max_length=255) # lake, river, ocean, etc.
    entry = models.CharField(max_length=255) # giant step, backroll, etc.
    drift = models.BooleanField(default=False)
    night = models.BooleanField(default=False)
    deep = models.BooleanField(default=False)
    wreck = models.BooleanField(default=False)
    cave = models.BooleanField(default=False)
    ice = models.BooleanField(default=False)
    altitude = models.BooleanField(default=False)
    decompression = models.BooleanField(default=False)
    rescue = models.BooleanField(default=False)
    photo = models.BooleanField(default=False)
    training = models.BooleanField(default=False)
    buddy = models.CharField(max_length=255)
    # buddy_id = models.ForeignKey('Diver', on_delete=models.SET_NULL)
    stop_depth = models.FloatField()
    stop_duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Diver " + self.diver + " @ site " + self.site + " on " + start_date

class Diver(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(blank=False, unique=True)
    birthday = models.DateField()
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=255, null=True, help_text='The MIMEType of the file')
    depth_unit = models.CharField(max_length=2)
    pressure_unit = models.CharField(max_length=3)
    temp_unit = models.CharField(max_length=1)
    weight_unit = models.CharField(max_length=3)
    communication = models.BooleanField(default=False)
    dives_offset = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.email + ")"

class Certification(models.Model):
    diver = models.ForeignKey('Diver', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    agency = models.CharField(max_length=255, blank=False)
    date = models.DateField()
    number = models.CharField(max_length=255)
    card_front = models.BinaryField(null=True, editable=True)
    card_front_content_type = models.CharField(max_length=255, null=True, help_text='The MIMEType of the file')
    card_back = models.BinaryField(null=True, editable=True)
    card_backcontent_type = models.CharField(max_length=255, null=True, help_text='The MIMEType of the file')
    instructor = models.CharField(max_length=255)
    # instructor_id = models.ForeignKey('Diver', on_delete=models.SET_NULL)
    dive_center = models.CharField(max_length=255)
    validated = models.BooleanField(default=False)
    notes = models.TextField()

    def __str__(self):
        return "Diver " + self.diver + " - " + self.name + " (" + self.agency + ")"

class Equipment(models.Model):
    diver = models.ForeignKey('Diver', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    type_ = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    thickness = models.FloatField()
    specs = models.TextField()
    valve = models.CharField(max_length=255)
    twin = models.BooleanField(default=False)
    dive = models.ManyToManyField('Dive')

    def __str__(self):
        return "Diver " + self.diver + " - " + self.name

class Site(models.Model):
    created_by = models.ForeignKey('Diver', on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, blank=False)
    country = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255)
    lat = models.FloatField()
    lon = models.FloatField()
    notes = models.TextField()
    picture = models.BinaryField(null=True, editable=True)
    content_type = models.CharField(max_length=255, null=True, help_text='The MIMEType of the file')

    def __str__(self):
        return self.name + " @ " + self.country