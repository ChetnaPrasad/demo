# Generated by Django 3.2.9 on 2022-01-03 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='enrolment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('classes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_seat', models.CharField(max_length=200)),
                ('room_no', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=900)),
                ('salary', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='schorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schorler_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Branch', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'student_name',
            },
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(max_length=200)),
                ('book', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestMigration_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schorler_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'test_migration_1',
            },
        ),
        migrations.CreateModel(
            name='tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_name', models.CharField(max_length=200)),
                ('rank', models.CharField(max_length=200)),
            ],
        ),
    ]
