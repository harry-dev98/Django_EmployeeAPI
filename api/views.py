from django.contrib.auth import authenticate # to manually authenticate user
from django.views.decorators.csrf import csrf_exempt # to use POST req without csrf
from rest_framework.authtoken.models import Token # generates/ get token for authenticated user
from rest_framework.decorators import api_view, permission_classes # some usefull decorators
from rest_framework.permissions import AllowAny # allowing all users to interact with the view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT
) # Some Basic HTTP responses
from rest_framework.response import Response # sending json response

# Some required imports

from employee.models import Employee 
from .serializers import EmpSerializer

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def getToken(request):
    # authenticating user manually
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Invalid'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid'},
                        status=HTTP_404_NOT_FOUND)

    # generating token for future authentication of a user
    token, _ = Token.objects.get_or_create(user=user)

    # returning token as a response
    return Response({
        'token': token.key,
        'message' : 'use this token to interact with our system\'s api'    
    }, status=HTTP_200_OK)

@csrf_exempt
@api_view(["PUT", "DELETE"])
def employee(request, pk):
    '''
        This function handles update and delete
        
        request: request recieved :: object :: 
        pk : primary key of employee :: int ::
    '''
    try:
        # Searching for employee
        emp = Employee.objects.get(pk = pk)
        if request.method == "PUT":
            # populating the Serializer with difference of existing instance of Employee
            # and data from update request recieved
            serialized = EmpSerializer(emp, data=request.data)

            # validating data
            if serialized.is_valid():
                serialized.save();
                return Response(
                    {
                        'message': 'Employee with pk = {} Data Updated'.format(pk)
                    }, 
                    status=HTTP_202_ACCEPTED
                )
            return Response(
                serialized.errors,
                status=HTTP_400_BAD_REQUEST
            )

        else:
            # deleting data
            emp.delete()
            return Response(
                {
                    'message' : 'Employee with pk = {} deleted.'.format(pk)
                },
                status=HTTP_204_NO_CONTENT
            )

    
    except Employee.DoesNotExist:
        # Exception cought here..
        return Response(
            {
                'message' : 'Employee with pk = {} doesnot exists.'.format(pk)    
            }, 
            status = HTTP_404_NOT_FOUND
        )

@csrf_exempt
@api_view(["POST"])
def add(request):
    '''
        this function accepts POST request
        and create new Employee instance via 
        Serializer and hence save the data to db

        request : request recieved :: object ::
    '''
    serialzied = EmpSerializer(data=request.data) # Serializing the data

    # validating nd hence saving
    if serialzied.is_valid():
        serialzied.save()
        return Response(
            {
                'message' : 'Employee Created!!'    
            }, 
            status=HTTP_200_OK
        )
    return Response(
        serialzied.errors,
        status=HTTP_400_BAD_REQUEST
    )


@api_view(["GET"])
@permission_classes((AllowAny,))
def employeeList(request):
    '''
        this function returns the serialized list
        of all employees.

        request : request received :: object ::
    '''
    emplist = Employee.objects.all()
    serialized = EmpSerializer(emplist, many=True)
    return Response(serialized.data, status=HTTP_200_OK)

