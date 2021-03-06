# Generated by Django 2.1.3 on 2018-12-10 12:57

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabu',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('recid', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=2, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'cabu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Canu',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('canuan', models.FloatField(blank=True, null=True)),
                ('canutx', models.CharField(blank=True, max_length=11, null=True)),
                ('sheet', models.CharField(blank=True, max_length=18, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('numpolice', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'canu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Capa',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('capakey', models.CharField(max_length=17)),
                ('casekey', models.CharField(blank=True, max_length=6, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'capa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GlobalNatures',
            fields=[
                ('nature_pk', models.IntegerField(primary_key=True, serialize=False)),
                ('nature_fr', models.CharField(blank=True, max_length=44, null=True)),
                ('nature_ge', models.CharField(blank=True, max_length=44, null=True)),
                ('nature_nl', models.CharField(blank=True, max_length=44, null=True)),
                ('obsolete', models.BooleanField()),
            ],
            options={
                'db_table': 'global_natures',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inli',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('inlity', models.CharField(blank=True, max_length=2, null=True)),
                ('inlitx', models.CharField(blank=True, max_length=50, null=True)),
                ('sheet', models.CharField(blank=True, max_length=18, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'inli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inpt',
            fields=[
                ('gid', models.AutoField(primary_key=True, serialize=False)),
                ('inptty', models.CharField(blank=True, max_length=2, null=True)),
                ('inpttx', models.CharField(blank=True, max_length=50, null=True)),
                ('sheet', models.CharField(blank=True, max_length=18, null=True)),
                ('the_geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'inpt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OwnersImp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertysituationidf', models.BigIntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('partytype', models.IntegerField(blank=True, null=True)),
                ('ownerright', models.CharField(blank=True, max_length=120, null=True)),
                ('right_trad', models.CharField(blank=True, max_length=102, null=True)),
                ('managedby', models.CharField(blank=True, max_length=4, null=True)),
                ('owner_officialid', models.CharField(blank=True, max_length=30, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=400, null=True)),
                ('owner_firstname', models.CharField(blank=True, max_length=180, null=True)),
                ('owner_birthdate', models.DateField(blank=True, null=True)),
                ('owner_country', models.CharField(blank=True, max_length=4, null=True)),
                ('owner_zipcode', models.CharField(blank=True, max_length=30, null=True)),
                ('owner_municipality_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_municipality_nl', models.CharField(blank=True, max_length=100, null=True)),
                ('owner_street_fr', models.CharField(blank=True, max_length=300, null=True)),
                ('owner_street_nl', models.CharField(blank=True, max_length=300, null=True)),
                ('owner_number', models.CharField(blank=True, max_length=20, null=True)),
                ('owner_boxnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('partner_officialid', models.CharField(blank=True, max_length=30, null=True)),
                ('partner_name', models.CharField(blank=True, max_length=400, null=True)),
                ('partner_firstname', models.CharField(blank=True, max_length=180, null=True)),
                ('partner_birthdate', models.DateField(blank=True, null=True)),
                ('partner_country', models.CharField(blank=True, max_length=4, null=True)),
                ('partner_zipcode', models.CharField(blank=True, max_length=30, null=True)),
                ('partner_municipality_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('partner_municipality_nl', models.CharField(blank=True, max_length=100, null=True)),
                ('partner_street_fr', models.CharField(blank=True, max_length=300, null=True)),
                ('partner_street_nl', models.CharField(blank=True, max_length=300, null=True)),
                ('partner_number', models.CharField(blank=True, max_length=20, null=True)),
                ('partner_boxnumber', models.CharField(blank=True, max_length=20, null=True)),
                ('coowner', models.CharField(blank=True, max_length=120, null=True)),
                ('anonymousowner', models.CharField(blank=True, max_length=120, null=True)),
                ('datesituation', models.DateField(blank=True, null=True)),
                ('divcad', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'owners_imp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ownersnames',
            fields=[
                ('owner_uid', models.AutoField(primary_key=True, serialize=False)),
                ('officialid', models.CharField(blank=True, max_length=30, null=True)),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('firstname', models.CharField(blank=True, max_length=180, null=True)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=4, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=30, null=True)),
                ('municipality_fr', models.CharField(blank=True, max_length=100, null=True)),
                ('municipality_nl', models.CharField(blank=True, max_length=100, null=True)),
                ('street_fr', models.CharField(blank=True, max_length=300, null=True)),
                ('street_nl', models.CharField(blank=True, max_length=300, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('boxnumber', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'ownersnames',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ownersproperties',
            fields=[
                ('situation_uid', models.AutoField(primary_key=True, serialize=False)),
                ('group_uid', models.BigIntegerField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('partytype', models.IntegerField(blank=True, null=True)),
                ('ownerright', models.CharField(blank=True, max_length=120, null=True)),
                ('right_trad', models.CharField(blank=True, max_length=102, null=True)),
                ('managedby', models.CharField(blank=True, max_length=4, null=True)),
                ('coowner', models.CharField(blank=True, max_length=120, null=True)),
                ('anonymousowner', models.CharField(blank=True, max_length=120, null=True)),
                ('datesituation', models.DateField(blank=True, null=True)),
                ('divcad', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ownersproperties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parcels',
            fields=[
                ('propertysituationid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('mukey', models.BigIntegerField(blank=True, null=True)),
                ('divcad', models.BigIntegerField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=2, null=True)),
                ('primarynumber', models.IntegerField(blank=True, null=True)),
                ('bisnumber', models.CharField(blank=True, max_length=6, null=True)),
                ('exponentletter', models.CharField(blank=True, max_length=2, null=True)),
                ('exponentnumber', models.CharField(blank=True, max_length=6, null=True)),
                ('partnumber', models.CharField(blank=True, max_length=10, null=True)),
                ('capakey', models.CharField(max_length=34)),
                ('nature', models.IntegerField(blank=True, null=True)),
                ('descriptprivate', models.CharField(blank=True, max_length=100, null=True)),
                ('block', models.CharField(blank=True, max_length=20, null=True)),
                ('floor', models.CharField(blank=True, max_length=20, null=True)),
                ('floorsituation', models.CharField(blank=True, max_length=60, null=True)),
                ('crossdetail', models.CharField(blank=True, max_length=60, null=True)),
                ('matutil', models.CharField(blank=True, max_length=60, null=True)),
                ('nottaxedmatutil', models.CharField(blank=True, max_length=10, null=True)),
                ('niscom', models.BigIntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('datesituation', models.DateField(blank=True, null=True)),
                ('group_uid', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parcels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelsCc',
            fields=[
                ('parcels_cc_pk', models.AutoField(primary_key=True, serialize=False)),
                ('constructionindication', models.IntegerField(blank=True, null=True)),
                ('constructiontype', models.CharField(blank=True, max_length=40, null=True)),
                ('constructionyear', models.CharField(blank=True, max_length=8, null=True)),
                ('floornumberaboveground', models.CharField(blank=True, max_length=510, null=True)),
                ('garret', models.CharField(blank=True, max_length=2, null=True)),
                ('physmodyear', models.CharField(blank=True, max_length=8, null=True)),
                ('constructionquality', models.CharField(blank=True, max_length=2, null=True)),
                ('garagenumber', models.IntegerField(blank=True, null=True)),
                ('centralheating', models.CharField(blank=True, max_length=2, null=True)),
                ('bathroomnumber', models.IntegerField(blank=True, null=True)),
                ('housingunitnumber', models.IntegerField(blank=True, null=True)),
                ('placenumber', models.IntegerField(blank=True, null=True)),
                ('builtsurface', models.BigIntegerField(blank=True, null=True)),
                ('usedsurface', models.BigIntegerField(blank=True, null=True)),
                ('cc', models.CharField(blank=True, max_length=110, null=True)),
            ],
            options={
                'db_table': 'parcels_cc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelsImp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertysituationidf', models.BigIntegerField(blank=True, null=True)),
                ('divcad', models.BigIntegerField(blank=True, null=True)),
                ('section', models.CharField(blank=True, max_length=2, null=True)),
                ('primarynumber', models.IntegerField(blank=True, null=True)),
                ('bisnumber', models.CharField(blank=True, max_length=6, null=True)),
                ('exponentletter', models.CharField(blank=True, max_length=2, null=True)),
                ('exponentnumber', models.CharField(blank=True, max_length=6, null=True)),
                ('partnumber', models.CharField(blank=True, max_length=10, null=True)),
                ('capakey', models.CharField(blank=True, max_length=34, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('nature', models.IntegerField(blank=True, null=True)),
                ('descriptprivate', models.CharField(blank=True, max_length=100, null=True)),
                ('block', models.CharField(blank=True, max_length=20, null=True)),
                ('floor', models.CharField(blank=True, max_length=20, null=True)),
                ('floorsituation', models.CharField(blank=True, max_length=60, null=True)),
                ('crossdetail', models.CharField(blank=True, max_length=60, null=True)),
                ('matutil', models.CharField(blank=True, max_length=60, null=True)),
                ('nottaxedmatutil', models.CharField(blank=True, max_length=10, null=True)),
                ('niscom', models.BigIntegerField(blank=True, null=True)),
                ('street_situation', models.CharField(blank=True, max_length=200, null=True)),
                ('street_translation', models.CharField(blank=True, max_length=200, null=True)),
                ('street_code', models.BigIntegerField(blank=True, null=True)),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('polwa', models.CharField(blank=True, max_length=20, null=True)),
                ('surfacenottaxable', models.BigIntegerField(blank=True, null=True)),
                ('surfacetaxable', models.BigIntegerField(blank=True, null=True)),
                ('surfaceverif', models.CharField(blank=True, max_length=2, null=True)),
                ('constructionyear', models.CharField(blank=True, max_length=8, null=True)),
                ('soilindex', models.BigIntegerField(blank=True, null=True)),
                ('soilrent', models.CharField(blank=True, max_length=10, null=True)),
                ('cadastralincomepersurface', models.BigIntegerField(blank=True, null=True)),
                ('cadastralincomepersurfaceotherdi', models.BigIntegerField(blank=True, null=True)),
                ('numbercadastralincome', models.BigIntegerField(blank=True, null=True)),
                ('charcadastralincome', models.CharField(blank=True, max_length=4, null=True)),
                ('cadastralincome', models.BigIntegerField(blank=True, null=True)),
                ('dateendexoneration', models.DateField(blank=True, null=True)),
                ('decrete', models.CharField(blank=True, max_length=40, null=True)),
                ('constructionindication', models.IntegerField(blank=True, null=True)),
                ('constructiontype', models.CharField(blank=True, max_length=40, null=True)),
                ('floornumberaboveground', models.CharField(blank=True, max_length=510, null=True)),
                ('garret', models.CharField(blank=True, max_length=2, null=True)),
                ('physmodyear', models.CharField(blank=True, max_length=8, null=True)),
                ('constructionquality', models.CharField(blank=True, max_length=2, null=True)),
                ('garagenumber', models.IntegerField(blank=True, null=True)),
                ('centralheating', models.CharField(blank=True, max_length=2, null=True)),
                ('bathroomnumber', models.IntegerField(blank=True, null=True)),
                ('housingunitnumber', models.IntegerField(blank=True, null=True)),
                ('placenumber', models.IntegerField(blank=True, null=True)),
                ('builtsurface', models.BigIntegerField(blank=True, null=True)),
                ('usedsurface', models.BigIntegerField(blank=True, null=True)),
                ('datesituation', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parcels_imp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ParcelsRc',
            fields=[
                ('parcels_rc_pk', models.BigIntegerField(primary_key=True, serialize=False)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('polwa', models.CharField(blank=True, max_length=20, null=True)),
                ('surfacenottaxable', models.BigIntegerField(blank=True, null=True)),
                ('surfacetaxable', models.BigIntegerField(blank=True, null=True)),
                ('surfaceverif', models.CharField(blank=True, max_length=2, null=True)),
                ('soilindex', models.BigIntegerField(blank=True, null=True)),
                ('soilrent', models.CharField(blank=True, max_length=10, null=True)),
                ('cadastralincomepersurface', models.BigIntegerField(blank=True, null=True)),
                ('cadastralincomepersurfaceotherdi', models.BigIntegerField(blank=True, null=True)),
                ('numbercadastralincome', models.BigIntegerField(blank=True, null=True)),
                ('charcadastralincome', models.CharField(blank=True, max_length=4, null=True)),
                ('cadastralincome', models.BigIntegerField(blank=True, null=True)),
                ('dateendexoneration', models.DateField(blank=True, null=True)),
                ('decrete', models.CharField(blank=True, max_length=40, null=True)),
                ('datesituation', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parcels_rc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parcelsstreets',
            fields=[
                ('street_uid', models.AutoField(primary_key=True, serialize=False)),
                ('niscom', models.BigIntegerField(blank=True, null=True)),
                ('street_situation', models.CharField(blank=True, max_length=200, null=True)),
                ('street_translation', models.CharField(blank=True, max_length=200, null=True)),
                ('street_code', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parcelsstreets',
                'managed': False,
            },
        ),
    ]
