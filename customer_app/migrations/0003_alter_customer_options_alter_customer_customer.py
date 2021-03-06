# Generated by Django 4.0.1 on 2022-01-09 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        ('customer_app', '0002_alter_customer_profile_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='user_app.myuser'),
        ),
    ]
