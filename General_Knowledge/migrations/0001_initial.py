# Generated by Django 3.2.23 on 2024-02-28 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General_Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('choices', models.TextField(blank=True, default=list)),
                ('correct_answer', models.TextField()),
            ],
        ),
    ]