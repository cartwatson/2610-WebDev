# Generated by Django 4.1.2 on 2022-10-19 03:50

from django.db import migrations

def populate_db(appreg, ed):
    # get model
    unit = appreg.get_model('unitconv', 'unitconv')
    # create rows
    USTon = unit(
        name='U.S. Ton',
        abbreviation='T',
        conversionFactor='0.0005'
    )
    Gram = unit(
        name='Gram',
        abbreviation='g',
        conversionFactor='453.592'
    )
    TroyOunce = unit(
        name='Troy Ounce',
        abbreviation='t_oz',
        conversionFactor='14.5833'
    )
    Kilogram = unit(
        name='Kilogram',
        abbreviation='kg',
        conversionFactor='0.453592'
    )
    ImperialPound = unit(
        name='Imperial Pound',
        abbreviation='lb',
        conversionFactor='1'
    )
    Ounce = unit(
        name='Ounce',
        abbreviation='oz',
        conversionFactor='16'
    )
    # populate database
    USTon.save()
    Gram.save()
    TroyOunce.save()
    Kilogram.save()
    TroyOunce.save()
    ImperialPound.save()
    Ounce.save()
    
class Migration(migrations.Migration):

    dependencies = [
        ('unitconv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db),
    ]
