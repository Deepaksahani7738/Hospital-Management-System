# Generated by Django 4.1.7 on 2023-04-01 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('comapany_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='images/')),
                ('product_price', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
            ],
        ),
        migrations.CreateModel(
            name='doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_specialisation', models.CharField(blank=True, choices=[('Chest', 'Chest'), ('Heart', ' Heart'), ('General', 'General'), ('Orthopaedic', 'Orthopaedic')], max_length=120, null=True)),
                ('contact_number', models.IntegerField()),
                ('location', models.CharField(max_length=30)),
                ('Entered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
            ],
        ),
        migrations.CreateModel(
            name='doctor_appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.doctors')),
                ('enter_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
            ],
        ),
        migrations.CreateModel(
            name='deal_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity_ordered', models.PositiveIntegerField()),
                ('Enter_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.employee')),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.doctors')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
