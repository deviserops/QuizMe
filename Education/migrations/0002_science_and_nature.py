# Generated by Django 3.2.23 on 2024-02-19 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Science_and_Nature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choices', models.TextField(blank=True, default=list)),
                ('correct_answer', models.TextField()),
            ],
        ),
    ]