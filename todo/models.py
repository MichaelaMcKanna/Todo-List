from django.db import models

class Todo(models.Model):
    #this is a schema that needs to be added to a database 
    name = models.CharField(max_length=100) 
    # traslates to a SQL table with a name and a string length restriction of 100
    due_date = models.DateField()
    # creates a colomn "due_date" that takes data from the DateField model 
    def __str__(self):
        return "self.name"
    # a string representation of the current model     

