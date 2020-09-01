from rest_framework import serializers 

from employee.models import Employee

class EmpSerializer(serializers.ModelSerializer):
    '''
        Helps in serializing and deserializing the models 
        hence helping in sending and recieving json responses via apis.
        ModelSerializer handles create, update, etc operations
        Hence, minimal code..

    '''
    class Meta:
        model = Employee # model class to be serialiezed
    
        fields = (
            'id', 'name', 'salary', 'department' 
        ) # these are the field which are involved in serialization