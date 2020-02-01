# Generated by Django 3.0.2 on 2020-02-01 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('F', 'FAKE'), ('R', 'REAL')], max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('target', models.CharField(max_length=255)),
                ('action', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('identifier', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Soldier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('P', 'Peon'), ('S', 'Spy')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in_minutes', models.IntegerField(max_length=255)),
                ('status', models.CharField(choices=[('C', 'COMPLETED'), ('I', 'INTERCEPTED'), ('T', 'TRANSIT'), ('D', 'DAMAGED')], max_length=255)),
                ('cost', models.IntegerField()),
                ('command', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Command')),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='soldier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Unit'),
        ),
    ]
