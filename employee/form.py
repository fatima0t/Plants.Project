from django import forms  
from employee.models import Employee
from employee.models import plant

from django.forms import fields

class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Employee  
        fields = "__all__"   #all fileds that appear in html page


class plantForm(forms.ModelForm):  
    class Meta:  
        model = plant  
        fields = "__all__"

        
      
    