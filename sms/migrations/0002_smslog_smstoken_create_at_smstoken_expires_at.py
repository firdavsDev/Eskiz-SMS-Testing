# Generated by Django 4.1 on 2022-08-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMSLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'SMS Log',
                'verbose_name_plural': 'SMS Logs',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='smstoken',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='smstoken',
            name='expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
