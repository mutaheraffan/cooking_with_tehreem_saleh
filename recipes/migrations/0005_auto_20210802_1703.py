# Generated by Django 2.1.3 on 2021-08-02 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20210802_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe_Category', verbose_name='Recipe Category'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='video_link',
            field=models.CharField(max_length=250),
        ),
    ]