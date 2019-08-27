# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver', models.ForeignKey(related_name='invites_received', to='profiles.Profile')),
                ('sender', models.ForeignKey(related_name='invites_sent', to='profiles.Profile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
