# Generated by Django 2.0 on 2017-12-28 23:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20171227_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='board',
            field=models.ManyToManyField(blank=True, related_name='_club_board_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='club',
            name='memberList',
            field=models.ManyToManyField(blank=True, related_name='_club_memberList_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='club',
            name='presidents',
            field=models.ManyToManyField(blank=True, related_name='_club_presidents_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='club',
            name='weeklyMeeting',
            field=models.TimeField(verbose_name='Weekly Meeting'),
        ),
        migrations.AlterField(
            model_name='user',
            name='current_clubs',
            field=models.ManyToManyField(blank=True, related_name='_user_current_clubs_+', to='clubs.Club'),
        ),
    ]
