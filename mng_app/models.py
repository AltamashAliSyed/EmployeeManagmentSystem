from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    sno =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100,)

    def __str__(self):
        return f"{self.name} from {self.location}"

class Role(models.Model):
    sno =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return f"{self.name}"

class Employee(models.Model):
    emp_id =models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def save(self, *args, **kwargs):
        # Check if this is a new instance (i.e., not yet saved to the database)
        if not self.pk:
            # Query the maximum emp_id in the Employee table
            max_id_employee = Employee.objects.aggregate(max_id=models.Max('emp_id'))['max_id']
            # If there are existing records, increment the max ID; otherwise, start from 1
            self.emp_id = max_id_employee + 1 if max_id_employee is not None else 1
        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Feedback(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_feedbacks')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_feedbacks')
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
