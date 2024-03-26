# Generated by Django 3.2.23 on 2024-03-21 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.categories'),
        ),
        migrations.AlterField(
            model_name='history',
            name='subcategory',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.subcategories'),
        ),
        migrations.AlterField(
            model_name='mythology',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.categories'),
        ),
        migrations.AlterField(
            model_name='mythology',
            name='subcategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Education.subcategories'),
        ),
        migrations.AlterField(
            model_name='science_and_nature',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.categories'),
        ),
        migrations.AlterField(
            model_name='science_and_nature',
            name='subcategory',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.subcategories'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Education.categories'),
        ),
    ]
