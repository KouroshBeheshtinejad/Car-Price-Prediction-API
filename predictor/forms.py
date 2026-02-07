from django import forms


TRANSMISSION_CHOICES = [
    ('Automatic', 'Automatic'),
    ('Manual', 'Manual'),
    ('Semi-Automatic', 'Semi-Automatic'),
]

DRIVEN_WHEELS_CHOICES = [
    ('front', 'front'),
    ('rear', 'rear'),
    ('all', 'all'),
]

VEHICLE_SIZE_CHOICES = [
    ('Compact', 'Compact'),
    ('Midsize', 'Midsize'),
    ('Large', 'Large'),
]


class CarFeaturesForm(forms.Form):
    Make = forms.CharField(max_length=100)
    Year = forms.IntegerField(min_value=1990, max_value=2025)
    Engine_HP = forms.FloatField(min_value=0)
    Engine_Cylinders = forms.FloatField(min_value=0)
    Transmission_Type = forms.ChoiceField(choices=TRANSMISSION_CHOICES)
    Driven_Wheels = forms.ChoiceField(choices=DRIVEN_WHEELS_CHOICES)
    Vehicle_Size = forms.ChoiceField(choices=VEHICLE_SIZE_CHOICES)
    Vehicle_Style = forms.CharField(max_length=100)
    Number_of_Doors = forms.FloatField(min_value=2, max_value=5)
    avg_mpg = forms.FloatField(min_value=0)
