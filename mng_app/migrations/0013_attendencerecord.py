# Generated by Django 4.2.6 on 2024-05-01 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mng_app', '0012_remove_feedback_created_at_remove_feedback_message_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendenceRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('clock_in_time', models.TimeField()),
                ('clock_out_time', models.TimeField(blank=True, null=True)),
                ('is_present', models.BooleanField(default=True)),
                ('empolyee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mng_app.employee')),
            ],
        ),
    ]
