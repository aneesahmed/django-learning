from django import forms
import datetime
from django.contrib.admin import widgets
from .models import Portfolio , PortfolioReleases, PortfolioStatus,Userstory, Sprint, Task, TaskStatus
from django.contrib.admin.widgets import AdminDateWidget


class BloodgroupForm(forms.ModelForm):
   class Meta:
        model =  Bloodgroup
        fields = "__all__"
        #labels =
        #widgets = {'details': forms.Textarea(attrs={'cols': 80})}