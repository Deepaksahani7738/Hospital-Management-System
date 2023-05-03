from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import products
from .models import employee
from .models import doctors
from .models import doctor_appointment
from .models import deal_detail
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.auth.forms import PasswordChangeForm


class product_data(forms.ModelForm):
    class Meta:
        model=products
        fields=['product_name','comapany_name','product_image','product_price','employee']
        widgets = {'product_name':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Product Name'}),
                   'comapany_name':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Company Name'}),
                   'product_price':forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Product Price'})
                }


class employee_data(forms.ModelForm):
    class Meta:
        model=employee
        fields=['user','first_name','last_name','email','date_of_joining','status']
        widgets = { 
                   'first_name':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Employee Name'}),
                   'last_name':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Last Name'}),
                    'email':forms.EmailInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Email'}),
                    'date_of_joining':forms.DateInput(attrs={'class':'form-control','type':'date','style':'max-width:400px','placeholder':'Enter Date'}),

                   }


class doctor_data(forms.ModelForm):
    class Meta:
        model=doctors
        fields=['doctor_name','doctor_specialisation','contact_number','location','Entered_by']
        widgets = { 'doctor_name':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Doctor Name'}),
                   'contact_number':forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Contact Number'}),
                    'location':forms.TextInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Location'}),
                     
                }

class appointment(forms.ModelForm):
    class Meta:
        model=doctor_appointment
        fields=['doctor','date','time','enter_by']
        # date = DateField(widget=AdminDateWidget)
        widgets = {
            
                   'date':forms.DateInput(attrs={'class':'form-control','type':'date','style':'max-width:400px','placeholder':'Enter Date'}),
                   'time':forms.TimeInput(attrs={'class':'form-control', 'type':'time','style':'max-width:400px','placeholder':'Enter Time'}),
                }


class deal_details(forms.ModelForm):
    class Meta:
        model=deal_detail
        fields=['doctor_name','product_name','Quantity_ordered','Enter_by']
        widgets = {
                   'doctor_name':forms.Select(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Select Doctor Name'}),
                     'product_name':forms.Select(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Select Product Name '}),
                     'Quantity_ordered':forms.NumberInput(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Quantity ordered '}),
                     'Enter_by':forms.Select(attrs={'class':'form-control','style':'max-width:400px','placeholder':'Enter Employee Name '}),
                     
                }

class changepassword(PasswordChangeForm):
    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields["old_password"].widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':"Existing Password"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter Password"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control","placeholder":"Enter Confirm Password"})


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password1','password2')
    email = forms.EmailField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:1000px','placeholder':'Enter Your Email'}))
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your FirstName'}))
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your Lastname'}))
    username = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control','style':'max-width:1000px','placeholder':'Enter Your Usename'}))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your password'}))
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','style':'max-width:600px','placeholder':'Enter Your Confirm password'}))
    check = forms.BooleanField(required=True)
    
    
