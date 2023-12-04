from django.db import models

# Create your models here.
class employees_ModelTable(models.Model):
    a=[('male','Male'),('female','Female'),('transgender','Transgender')]
    b=[(' United States',' United States'),('Russia','Russia'),('China','China'),
    ('India','India'),('United Kingdom','United Kingdom'),('South Korea','South Korea'),
    ('Pakistan','Pakistan'),('Japan','Japan'),('France','France')]
    c=[(' Punjab',' Punjab'),('Rajasthan','Rajasthan'),('Tamil Nadu','Tamil Nadu'),('Telangana','Telangana'),
    ('munbai','munbai'),('kerala','kerala')]
    d=[(' Chennai',' Chennai'),('Kanchipuram','Kanchipuram'),('Kanyakumari','Kanyakumari'),
    ('Thoothukudi','Thoothukudi'),('Coimbatore','Coimbatore'),('madurai','mdurai')]
    id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    Mobilno=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Gender=models.CharField(choices=a,max_length=50)
    Country=models.CharField(choices=b,max_length=50)
    District=models.CharField(choices=c,max_length=50)
    State=models.CharField(choices=d,max_length=50)
    status=models.CharField(default='available',max_length=50,editable=False)
    class Meta:
        db_table='employee'
class complaint_ModelTable(models.Model):
    id=models.AutoField(primary_key=True)
    empid=models.IntegerField(null=True)
    Name=models.CharField(max_length=50)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100,default='Not Reply Yet',null=True)
    status=models.CharField(default='available',max_length=50,editable=False)
    class Meta:
        db_table='grievance'