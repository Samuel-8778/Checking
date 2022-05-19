from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import TaskSerializer, TaskSerializer1, TaskSerializer2
from .models import Employee, Person, Address
import logging

logger = logging.getLogger('django')


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        "TABLE-1": "Employee",
        'Emp_List': '/task-list/',
        'Emp_Detail View': '/task-detail/<str:id>/',
        'Emp_Create': '/task-create/',
        'Emp_Update': '/task-update/<str:id>/',
        'Emp_Delete': '/task-delete/<str:id>/',
        "TABLE-2": 'Person',
        "per_List": '/task-list-1/',
        "Per_Detail View": '/task-detail-1/<str:id>/',
        'Per_Create': '/task-create-1/',
        'Per_Update': '/task-update-1/<str:id>/',
        'Per_Delete': '/task-delete-1/<str:id>/',
        "TABLE-3": 'Address',
        "add_List": '/task-list-add/',
        "add_Detail View": '/task-detail-add/<str:id>/',
        'add_Create': '/task-create-add/',
        'add_Update': '/task-update-add/<str:id>/',
        'add_Delete': '/task-delete-add/<str:id>/'

    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    try:
        logger.info("Getting ALl the Employees")
        tasks = Employee.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    except:
        logger.warning("Employee getting failed")
        raise ValueError("Error involved in Values")


@api_view(['GET'])
def taskList1(request):
    try:
        logger.info("Getting ALl the Person")
        tasks = Person.objects.all()
        serializer = TaskSerializer1(tasks, many=True)
        return Response(serializer.data)
    except:
        logger.warning("person getting failed")
        raise ValueError("Error involved in Values")


@api_view(['GET'])
def taskList2(request):
    tasks = Address.objects.all()
    serializer = TaskSerializer2(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    try:
        tasks = Employee.objects.get(id=pk)
        serializer = TaskSerializer(tasks, many=False)
        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


@api_view(['GET'])
def taskDetail1(request, pk):
    try:
        tasks = Person.objects.get(id=pk)
        serializer = TaskSerializer1(tasks)
        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


@api_view(['GET'])
def taskDetail2(request, pk):
    try:
        tasks = Address.objects.get(id=pk)
        serializer = TaskSerializer2(tasks, many=False)
        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


user_response = openapi.Response('response description', TaskSerializer)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer)
@api_view(['POST'])
def taskCreate(request):
    try:
        logger.info("New Employee adding....")
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


user_response0 = openapi.Response('response description', TaskSerializer1)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer1)
@api_view(['POST'])
def taskCreate1(request):
    serializer = TaskSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


user_response1 = openapi.Response('response description', TaskSerializer2)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer2)
@api_view(['POST'])
def taskCreate2(request):
    serializer = TaskSerializer2(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


user_response2 = openapi.Response('response description', TaskSerializer)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer)
@api_view(['POST'])
def taskUpdate(request, pk):
    try:

        task = Employee.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")

user_response4 = openapi.Response('response description', TaskSerializer1)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer1)
@api_view(['POST'])
def taskUpdate1(request, pk):
    try:
        task = Person.objects.get(id=pk)
        serializer = TaskSerializer1(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


user_response5 = openapi.Response('response description', TaskSerializer)


@swagger_auto_schema(methods=["POST"], request_body=TaskSerializer)
@api_view(['POST'])
def taskUpdate2(request, pk):
    try:
        task = Address.objects.get(id=pk)
        serializer = TaskSerializer2(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


@api_view(['DELETE'])
def taskDelete(request, pk):
    try:

        task = Employee.objects.get(id=pk)
        task.delete()

        return Response('Item successfully delete!')
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")


@api_view(['DELETE'])
def taskDelete1(request, pk):
    task = Person.objects.get(id=pk)
    task.delete()

    return Response('Item successfully delete!')


@api_view(['DELETE'])
def taskDelete2(request, pk):
    try:
        logger.info("Address deleted")
        task = Address.objects.get(id=pk)
        task.delete()

        return Response('Item successfully delete!')
    except:
        logger.error("Value Error")
        raise ValueError("some error involved in values")

