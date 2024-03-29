# Generated by Django 4.2.10 on 2024-03-04 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Brand name')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Model')),
                ('condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=20, verbose_name='Condition')),
                ('no_previous_owners', models.IntegerField(default=0, verbose_name='No. of previous owners')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Colour name')),
                ('paint_code', models.CharField(max_length=50, verbose_name='Paint code')),
            ],
        ),
        migrations.CreateModel(
            name='OwnerRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100, verbose_name='Owner name')),
                ('owned_from', models.DateField(verbose_name='Owned from')),
                ('owned_to', models.DateField(blank=True, null=True, verbose_name='Owned to')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.colour'),
        ),
    ]
