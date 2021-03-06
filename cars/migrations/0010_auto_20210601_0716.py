# Generated by Django 3.2.3 on 2021-06-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_no_of_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District Of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='vin_no',
            field=models.CharField(max_length=50),
        ),
    ]
