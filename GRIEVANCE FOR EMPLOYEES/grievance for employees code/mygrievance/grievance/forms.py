from django import forms
from grievance.models import employees_ModelTable,complaint_ModelTable
class userregforms(forms.ModelForm):
    class Meta:
        model=employees_ModelTable
        fields='__all__'
class complaintregforms(forms.ModelForm):
    class Meta:
        model=complaint_ModelTable
        fields='__all__'