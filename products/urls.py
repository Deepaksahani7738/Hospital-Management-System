from django.urls import path
from . import views
from .views import mydata
from .views import employee_data
from .views import doctor_data
from .views import appointment
from .views import deal_detail
from .views import ProfileTemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import ChangePasswordView
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls import reverse_lazy




urlpatterns = [
       path('',views.index,name='home'),
       path('register/',views.register,name='register'),
       path('product/',login_required(mydata.as_view()),name='Add_Product'),
       path('employee/',login_required(employee_data.as_view()),name='employee_data'),
       path('add_doctor/',login_required(doctor_data.as_view()),name='Add_doctor'),
       path('appointment/schedule/',login_required(appointment.as_view()),name='doct_schedule'),
       path('deal_detail/',login_required(deal_detail.as_view()),name='deal_details'),
       path('profile/', ProfileTemplateView.as_view(),name='profile'),
       path('view_data/',views.data,name='view_data'),
       path('doctor_data/',views.doctors_data,name='doctor_data'),
       path('about_us/',views.about,name='about'),
       path('doct_appointment/',views.base_data,name='appointment'),
       path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
       path('logout/',auth_views.LogoutView.as_view(template_name='registration/logout.html'),name='logout'),
       path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
       path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
       path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
       path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
       path('change/password/',ChangePasswordView.as_view(success_url = reverse_lazy("password_change_done")),name='change'),
       path('change/password/done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name="password_change_done"),
        
       
      
       
    
]