from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils.html import format_html


class employee(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    date_of_joining=models.DateField(null=True)
    status=models.BooleanField()
    
    def __str__(self):
        return self.first_name
    
class data(admin.ModelAdmin):
        model = employee
        list_display = ['first_name','last_name','email','date_of_joining','status']
        list_per_page = 2
        list_editable = ('email',)
        list_filter = ('date_of_joining',)
        search_fields = ('first_name',)
admin.site.register(employee,data)


class products(models.Model):
    product_name=models.CharField(max_length=100)
    comapany_name=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='images/')
    product_price=models.IntegerField()
    employee=models.ForeignKey(employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
     
class BlogAdmin(admin.ModelAdmin):
        model=products
        list_display = ['product_name','comapany_name','product_image_tag','product_price','employee']
        list_filter = ('employee',)
        search_fields = ('product_name',)
        list_per_page = 2
        list_display_links = ('comapany_name',)
        list_editable = ('product_price',)
        def product_image_tag(self,obj):
                return format_html("<img src='{}' style='max-width:150px; max-height:150px'>".format(obj.product_image.url))
            
            
admin.site.register(products,BlogAdmin)
    
choice=(('Chest','Chest'),
            ('Heart',' Heart'),
            ('General','General'),
            ('Orthopaedic','Orthopaedic'))
    
class doctors(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_specialisation=models.CharField(max_length=120,blank=True,null=True,choices=choice)
    contact_number=models.IntegerField()
    location=models.CharField(max_length=30)
    Entered_by=models.ForeignKey(employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.doctor_name
    
class doctors_data(admin.ModelAdmin):
    model = products
    list_display = ('doctor_name','doctor_specialisation','contact_number','location','Entered_by')
    list_per_page = 2
    list_display_links = ('location',)
    list_editable = ('contact_number',)
    list_filter = ('location',)
    search_fields = ('location',)
admin.site.register(doctors,doctors_data)
    
    
class doctor_appointment(models.Model):
    doctor=models.ForeignKey(doctors,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    enter_by=models.ForeignKey(employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.doctor)
    
class doct_done(admin.ModelAdmin):
        model = doctor_appointment
        list_display = ['id','doctor','date','time','enter_by']
        list_editable = ('time','date')
        list_filter = ('date',)
        list_per_page = 2
        list_display_links = ('doctor',)
        search_fields = ('date',)
    
admin.site.register(doctor_appointment,doct_done)

class deal_detail(models.Model):
    doctor_name=models.ForeignKey(doctors,on_delete=models.CASCADE)
    product_name=models.ForeignKey(products,on_delete=models.CASCADE)
    Quantity_ordered=models.PositiveIntegerField()
    Enter_by=models.ForeignKey(employee,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.doctor_name)
    
    
class mydata(admin.ModelAdmin):
    model = deal_detail
    list_display = ['id','product_name','Quantity_ordered','Enter_by']
    list_display_links = ('product_name',)
    list_editable = ('Quantity_ordered',)
    list_per_page = 2
    search_fields = ('Quantity_ordered',)
    list_filter = ('Enter_by',)
admin.site.register(deal_detail,mydata)
    
    
    

    
    
    






    

