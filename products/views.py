from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .forms import RegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import products
from .models import employee
from .models import doctors
from .models import doctor_appointment
from .models import deal_detail
from .forms import product_data
from .forms import employee_data
from .forms import doctor_data
from .forms import appointment
from .forms import  deal_details
from .forms import changepassword
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView


@login_required(login_url='login')
def index(request):
    return render(request,'myapp/index.html')


def register(request):
    if request.method=='GET':
        form=RegistrationForm()
        return render(request,'myapp/registers.html',{'form':form})
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was Successfuly created for '+username)
            return redirect('home')
        else:
            return render(request,'myapp/registers.html',{'form':form})
    return render(request,'myapp/registers.html',{'form':form})




class mydata(SuccessMessageMixin,CreateView):
    model = products
    form_class = product_data
    template_name = "myapp/product_data.html"
    success_message = 'Product has been successfuly !!'
    success_url = reverse_lazy('view_data')
    
    
    
class employee_data(SuccessMessageMixin,CreateView):
    model = employee
    form_class = employee_data
    template_name = "myapp/employee_data.html"
    success_message = 'Employee has been successfuly !!'
    success_url = reverse_lazy('home')
    
class doctor_data(SuccessMessageMixin,CreateView):
    model = doctors
    form_class = doctor_data
    template_name = "myapp/doctor_data.html"
    success_message = 'Doctor has been successfuly !!'
    success_url = reverse_lazy('doctor_data')
    
     
class appointment(SuccessMessageMixin,CreateView):
    model = doctor_appointment
    form_class = appointment
    template_name = "myapp/appointment_schedule.html"
    success_message = 'Appointment has been successfuly !!'
    success_url = reverse_lazy('appointment')
    
class deal_detail(SuccessMessageMixin,CreateView):
    model = deal_detail
    form_class = deal_details
    template_name = "myapp/deal_detail.html"
    success_message = 'Order has been successfuly !!'
    success_url = reverse_lazy('home')
    

@login_required(login_url='login')  
def data(request):
    data=products.objects.all()
    res={"data":data}
    return render(request,'myapp/view_data.html',res)


@login_required(login_url='login') 
def base_data(request):
    dt=doctor_appointment.objects.all()
    deep={"forms":dt}
    return render(request,'myapp/appointment.html',deep)


@login_required(login_url='login') 
def doctors_data(request):
    res=doctors.objects.all()
    return render(request,'myapp/doctors_data.html',{"result":res})


class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'


@login_required(login_url='login')
def about(request):
    return render(request,'myapp/about.html')
        
class ChangePasswordView(PasswordChangeView):
    form_class = changepassword
    template_name = "myapp/changepass.html"  

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'myapp/password_change_done.html'