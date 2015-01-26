# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('text', models.CharField(max_length=200)),
                ('poll', models.ForeignKey(to='polls.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollFinishFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollStartFlag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('poll', models.OneToOneField(to='polls.Poll')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PollVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('weight', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(to='donors.Donor')),
                ('poll_choice', models.OneToOneField(to='polls.PollChoice')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pollfinishflag',
            name='poll_start',
            field=models.OneToOneField(to='polls.PollStartFlag'),
            preserve_default=True,
        ),
    ]
