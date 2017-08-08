from django.conf.urls import url
#from . import views
from patients.views import BloodgroupList, PatientList, BloodgroupCreate

app_name = 'patients'
 
 
 
 # release Release
urlpatterns = [
    url(r'^$',BloodgroupList.as_view(), name='bloodgroup-list'),
    url(r'^BloodgroupList',  BloodgroupList.as_view(), name='bloodgroup-list'),
    url(r'^$',  BloodgroupList.as_view(), name='dashboard'),
    #url(r'^bloodgroup/(?P<pk>\d+)$', BloodgroupDetails.as_view(), name='bloodgroup-detail'),
    url(r'^bloodgroup/add/', BloodgroupCreate.as_view(), name='bloodgroup-add'),
    #url(r'^bloodgroup/update/(?P<pk>\d+)$', BloodgroupUpdate.as_view(), name='bloodgroup-update'),
    #url(r'^bloodgroup/delete/(?P<pk>\d+)$', BloodgroupDelete.as_view(), name='bloodgroup-delete'),
 ]