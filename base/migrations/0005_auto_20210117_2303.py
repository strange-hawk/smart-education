# Generated by Django 3.0.6 on 2021-01-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20210117_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.CharField(choices=[('chemistry', 'chemistry'), ('fauna', 'fauna'), ('flora', 'flora'), ('biology', 'biology'), ('astronomy', 'astronomy'), ('machinery', 'machinery'), ('default', 'default')], default='default', max_length=200),
        ),
    ]
