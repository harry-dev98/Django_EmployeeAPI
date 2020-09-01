from django.db import models

class Employee(models.Model): 
    '''
        Employee model class inheriting from models.Model
        This class directly manages the database.
        Other main logics could be implemented here

        name : name of the employee :: str ::
        salary : salary of the employee :: big int ::
        department : department where employee works :: str ::
    '''

    name = models.CharField(max_length=100)
    salary = models.BigIntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        '''
            function represents the name of instance of the class

        '''

        return self.name