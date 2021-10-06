from django import forms
from fbvApp.models import Student
from django.contrib.auth.forms import AuthenticationForm
# class LoginForm(AuthenticationForm):
#     username = forms.TextInput(
#                 attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
#                        'focus': 'outline-none focus:shadow-outline', 'id': 'username', 'type': 'text',
#                        ' placeholder': 'Username'}),
#     password = forms.TextInput(
#                 attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
#                        'focus': 'outline-none focus:shadow-outline', 'id': 'username', 'type': 'password',
#                        ' placeholder': 'Username'}),

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'firstName': forms.TextInput(
                attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
                       'focus': 'outline-none focus:shadow-outline', 'id': 'username', 'type': 'text',
                       ' placeholder': 'Username'}),

            'Topic': forms.TextInput(
                attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
                       'focus': 'outline-none focus:shadow-outline', 'id': 'username', 'type': 'text',
                       ' placeholder': ''}),
            'lastName': forms.Textarea(
                attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
                       'focus': 'outline-none focus:shadow-outline', 'id': 'username', 'type': 'text',
                       ' placeholder': ''}),
            'testScore': forms.TextInput(
                attrs={'class': 'shadow-mg appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight',
                       'focus': 'outline-none focus:shadow-outline', 'type': 'number'})
        }
