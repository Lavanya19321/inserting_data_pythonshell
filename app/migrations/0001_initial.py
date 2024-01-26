# Generated by Django 4.2.6 on 2023-12-15 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=25)),
                ('dloc', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=25)),
                ('esal', models.IntegerField()),
                ('edate', models.DateField()),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
    ]