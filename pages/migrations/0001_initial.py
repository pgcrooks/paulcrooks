# Generated by Django 2.0 on 2017-12-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_text', models.CharField(max_length=5000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
