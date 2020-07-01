# Generated by Django 3.0.6 on 2020-06-06 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_pattern'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='id_crew_member_1',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fist', to='app.crew_member'),
        ),
        migrations.AddField(
            model_name='flight',
            name='id_crew_member_2',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='app.crew_member'),
        ),
        migrations.AddField(
            model_name='flight',
            name='id_crew_member_3',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='third', to='app.crew_member'),
        ),
        migrations.DeleteModel(
            name='pattern',
        ),
    ]