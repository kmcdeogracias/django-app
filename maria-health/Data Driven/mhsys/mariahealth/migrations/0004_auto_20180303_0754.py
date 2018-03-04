# Generated by Django 2.0.2 on 2018-03-03 07:54

from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    HMOProvider = apps.get_model("mariahealth", "HMOProvider")
    db_alias = schema_editor.connection.alias
    HMOProvider.objects.using(db_alias).bulk_create([
        HMOProvider(name="PhilCare"),
        HMOProvider(name="Asian Life"),
        HMOProvider(name="MaxiCare"),
        HMOProvider(name="Medi Card"),
        HMOProvider(name="Lifeline"),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two HMOProvider instances,
    # so reverse_func() should delete them.
    HMOProvider = apps.get_model("mariahealth", "HMOProvider")
    db_alias = schema_editor.connection.alias
    HMOProvider.objects.using(db_alias).filter(name="PhilCare").delete()
    HMOProvider.objects.using(db_alias).filter(name="Asian Life").delete()
    HMOProvider.objects.using(db_alias).filter(name="MaxiCare").delete()
    HMOProvider.objects.using(db_alias).filter(name="Medi Card").delete()
    HMOProvider.objects.using(db_alias).filter(name="Lifeline").delete()

class Migration(migrations.Migration):

    dependencies = [
        ('mariahealth', '0003_auto_20180303_0753'),
    ]

    operations = [
    	migrations.RunPython(forwards_func, reverse_func),
    ]