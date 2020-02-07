from durgaapi_with_restframework_APP.models import Employee
from rest_framework.serializers import ModelSerializer


#____________________________________________________________________________________________________________________


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'