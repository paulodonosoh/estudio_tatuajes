from django.db import migrations, models
from django.db.models import F, Q
from django.utils import timezone


def separar_fecha_y_horas(apps, schema_editor):
    reserva_model = apps.get_model('reserva', 'Reserva')

    for reserva in reserva_model.objects.all().iterator():
        inicio = reserva.inicio
        fin = reserva.fin
        if timezone.is_aware(inicio):
            inicio = timezone.localtime(inicio)
        if timezone.is_aware(fin):
            fin = timezone.localtime(fin)
        reserva.fecha = inicio.date()
        reserva.hora_inicio = inicio.time().replace(tzinfo=None)
        reserva.hora_fin = fin.time().replace(tzinfo=None)
        reserva.save(update_fields=['fecha', 'hora_inicio', 'hora_fin'])


def restaurar_inicio_y_fin(apps, schema_editor):
    reserva_model = apps.get_model('reserva', 'Reserva')

    for reserva in reserva_model.objects.all().iterator():
        inicio = timezone.make_aware(
            timezone.datetime.combine(reserva.fecha, reserva.hora_inicio),
        )
        fin = timezone.make_aware(
            timezone.datetime.combine(reserva.fecha, reserva.hora_fin),
        )
        reserva.inicio = inicio
        reserva.fin = fin
        reserva.save(update_fields=['inicio', 'fin'])


class Migration(migrations.Migration):
    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_inicio',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_fin',
            field=models.TimeField(null=True),
        ),
        migrations.RunPython(
            separar_fecha_y_horas,
            restaurar_inicio_y_fin,
        ),
        migrations.RemoveConstraint(
            model_name='reserva',
            name='reserva_fin_despues_de_inicio',
        ),
        migrations.RemoveIndex(
            model_name='reserva',
            name='reserva_res_artista_6e36f5_idx',
        ),
        migrations.RemoveIndex(
            model_name='reserva',
            name='reserva_res_estado_6e185c_idx',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='inicio',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='fin',
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_inicio',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_fin',
            field=models.TimeField(),
        ),
        migrations.AddConstraint(
            model_name='reserva',
            constraint=models.CheckConstraint(
                condition=Q(hora_fin__gt=F('hora_inicio')),
                name='reserva_hora_fin_despues_de_inicio',
            ),
        ),
        migrations.AddIndex(
            model_name='reserva',
            index=models.Index(
                fields=['artista', 'fecha', 'hora_inicio'],
                name='reserva_res_artista_fecha_idx',
            ),
        ),
        migrations.AddIndex(
            model_name='reserva',
            index=models.Index(
                fields=['estado', 'fecha'],
                name='reserva_res_estado_fecha_idx',
            ),
        ),
    ]
