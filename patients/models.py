from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db import models
from  datetime import  date
from django.contrib.auth.models import User

#from scrum.submodels.userstorymodel import

class Bloodgroup(models.Model):
    bloodgroupId = models.AutoField(primary_key=True)
    bloodgroup   = models.CharField(max_length=100)


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('patients:bloodgroup-list')

class Meta:
    managed = False
    db_table = 'bloodgrroup'
class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bloodgroupId = models.ForeignKey('BloodGroup', models.DO_NOTHING, db_column='bloodgroupid')  
    