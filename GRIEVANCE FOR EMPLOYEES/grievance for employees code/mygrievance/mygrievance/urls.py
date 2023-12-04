from django.contrib import admin
from django.urls import path
from grievance import views
urlpatterns = [
    path('', views.home,name='home'),
    path('admin', views.admin,name='admin'),
    path('About', views.About,name='About'),
    path('adminlog',views.adminlog,name='adminlog'),
    path('Adminhome',views.Adminhome,name='Adminhome'),
    path('empy',views.empy,name='empy'),
    path('employeeview',views.employeeview,name='employeeview'),
    path('editiuser',views.editiuser,name='editiuser'),
    path('deleteuser',views.deleteuser,name='deleteuser'),
    path('EDIT',views.EDIT,name='EDIT'),
    path('customerupdate',views.customerupdate,name='customerupdate'),
    path('complaint',views.complaint,name='complaint'),
    path('complaintview',views.complaintview,name='complaintview'),
    path('logout',views.logout,name='logout'),
    path('emlog',views.emlog,name='emlog'),
    path('emlogin',views.emlogin,name='emlogin'),
    path('mycompaint',views.mycompaint,name='mycompaint'),
    path('REPLY',views.REPLY,name='REPLY'),
    path('rly',views.rly,name='rly'),
    #Employee Home
    path('emphome',views.emphome,name='emphome'),
    path('complaint1',views.complaint1,name='complaint1'),
    path('replay2',views.replay2,name='replay2'),
] 
