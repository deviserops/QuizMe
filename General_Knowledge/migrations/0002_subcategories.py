# Generated by Django 3.2.23 on 2024-03-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('General_Knowledge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.TextField()),
                ('description', models.TextField()),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='General_Knowledge.categories')),
            ],
        ),
    ]
