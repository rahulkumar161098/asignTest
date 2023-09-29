# Generated by Django 4.2.5 on 2023-09-29 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateBid',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('base_price', models.IntegerField()),
                ('bid_date', models.DateField(auto_now_add=True)),
                ('bid_desc', models.TextField()),
                ('win_by', models.CharField(blank=True, max_length=10)),
                ('bid_type', models.CharField(default='e_type', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]