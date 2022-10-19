
from django.db import models


# import datetime, random
# def genID(dat):
#     num = random.sample(range(1,1999),1)
#     # yea = dat.strftime("%y")
#     # dat = datetime.datetime(dat)
#     yea= dat.strftime("%y")
#     mon = dat.strftime("%m")
#     emp_id = "CLN"+"-"+mon+yea+"-"+str(num[0])
#     return emp_id

class employee(models.Model):
    firstname = models.CharField(max_length = 25)
    lastname = models.CharField(max_length = 25)
    role = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    mailAdd = models.EmailField(max_length=254)
    employedDT = models.DateField()
    employeeID = models.CharField(max_length = 20,primary_key=True)
    # employeeID = models.CharField(max_length = 20,primary_key=True, default = genID(employedDT), editable=False)
    

    def __str__(self):
        return self.firstname + ' ' + self.employeeID