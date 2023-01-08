# Generated by Django 4.1.4 on 2023-01-07 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('air', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('residence', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentialComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.residentialcomment')),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residential_comment', to='residence.residential')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelRoomComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('hotel_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_room_comment', to='residence.hotelroom')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.hotelroomcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HotelComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_comment', to='residence.hotel')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.hotelcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AirPortComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airport_comment', to='air.airport')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.airportcomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AirLineComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(10, 'Created'), (20, 'Approved'), (30, 'Rejected'), (40, 'Deleted')], default=10)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airline_comment', to='air.airline')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comment.airlinecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s', to=settings.AUTH_USER_MODEL)),
                ('validated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='validated_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]