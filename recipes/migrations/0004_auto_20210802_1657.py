# Generated by Django 2.1.3 on 2021-08-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210802_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe Details', 'verbose_name_plural': 'Recipes Details'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe_Category', verbose_name='Recipe Category'),
        ),
    ]
