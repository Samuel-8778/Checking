from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from .serializers import TaskSerializer, TaskSerializer1, TaskSerializer2
from .models import Employee, Person, Address
import logging
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger('django')


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            employee = Employee.objects.all()
            person = Person.objects.all()
            address = Address.objects.all()
            serializers = TaskSerializer(employee, many=True)
            serializers1 = TaskSerializer1(person, many=True)
            serializers2 = TaskSerializer2(address, many=True)
            result = ({
                "Employee details": serializers.data,
                "Person Details": serializers1.data,
                "address Details": serializers2.data
            })
            return Response(result)
        except:
            logger.critical("Token Invalid ")
            raise ValueError("Token Invalid")
