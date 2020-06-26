import floppyforms.__future__ as forms
#import floppyforms
#from django.forms import *
from .models import *
from .choices import *


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Hardware
        organization = {i[0]:i[0] for i in ORGANIZATION}
        type_dev = {i.id:i.type_dev for i in Type_devs.objects.all()}
        building = {i.id:i.building for i in Buildings.objects.all()}
        employ = {i.id:f'{i.surname} {i.name}' for i in Employes.objects.all()}
        vendor = {i[0]:i[0] for i in VENDOR}
        status = {i[0]:i[0] for i in STATUS}
        seller = {i[0]:i[0] for i in SELLER}
        mol = {i[0]:i[0] for i in MOL}
        fields = '__all__'
        widgets = {
            'type_dev' : forms.widgets.Input(datalist = type_dev),
            'organization': forms.widgets.Input(datalist = organization),
            'vendor': forms.widgets.Input(datalist = vendor),
            'status': forms.widgets.Input(datalist = status),
            'buildings': forms.widgets.Input(datalist = building),
            'employ': forms.widgets.Input(datalist = employ),
            'note': forms.widgets.Textarea(),
            'seller': forms.widgets.Input(datalist = seller),
            'date_of_sale': forms.widgets.DateInput(),
            'MOL': forms.widgets.Input(datalist = mol),


        }
       
