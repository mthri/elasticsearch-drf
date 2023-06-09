# Generated by Django 4.2.1 on 2023-05-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('num_cylinders', models.PositiveIntegerField(verbose_name='تعداد سیلندر')),
                ('num_seats', models.PositiveIntegerField(verbose_name='تعداد سرنشین')),
                ('color', models.CharField(max_length=20, verbose_name='رنگ')),
                ('engine_capacity', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='حجم سیلندر')),
                ('owner', models.CharField(max_length=50, verbose_name='مالک خودرو')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
            ],
            options={
                'verbose_name': 'خودرو',
                'verbose_name_plural': 'خودرو ها',
            },
        ),
    ]
