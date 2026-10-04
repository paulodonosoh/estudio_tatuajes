from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='nombre_cliente',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]