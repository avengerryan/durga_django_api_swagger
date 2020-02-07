from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from durgaapi_with_restframework_APP.models import Employee
from durgaapi_with_restframework_APP.serializers import EmployeeSerializer
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework.schemas import SchemaGenerator
# from rest_framework.views import APIView
# from rest_framework_swagger import renderers

#____________________________________________________________________________________________________________________
# Create your views here.


# NOTE: ViewSets are the fastest way to create API's.
# Standard Operations: We use viewsets. and for customization, see below:
# Customization: We need to override the GET METHOD, PUT METHOD, POST METHOD, if we want customization. i.e API Views.


class EmployeeCRUDCBV(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# class SwaggerSchemaView(APIView):
#     permission_classes = [AllowAny]
#     renderer_classes = [
#         renderers.OpenAPIRenderer,
#         renderers.SwaggerUIRenderer
#     ]
#
#     def get(self, request):
#         generator = SchemaGenerator()
#         schema = generator.get_schema(request=request)
#
#         return Response(schema)