# Generated by Django 4.2 on 2025-04-18 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0008_shipment_contents_shipment_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='code',
        ),
        migrations.AddField(
            model_name='shipment',
            name='loading_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاريخ التحميل'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='notes_customer',
            field=models.TextField(blank=True, null=True, verbose_name='ملاحظات العميل'),
        ),
        migrations.AddField(
            model_name='shipment',
            name='notes_recipient',
            field=models.TextField(blank=True, null=True, verbose_name='ملاحظات المستلم'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='actual_delivery_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الوصول الفعلي'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاريخ الانشاء'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='days_to_arrive',
            field=models.IntegerField(blank=True, default=3, null=True, verbose_name='عدد الأيام  الوصول'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='expected_arrival_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاريخ الوصول المتوقع'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='ملاحظات'),
        ),
        migrations.AlterField(
            model_name='shipment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='تاريخ التحديث'),
        ),
    ]
