# Generated by Django 2.0 on 2017-12-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20171229_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='icon',
            field=models.ImageField(blank=True, default='clubs/clubdefault', upload_to='icons/'),
        ),
    ]