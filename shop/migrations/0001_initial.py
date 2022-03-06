# Generated by Django 3.2 on 2022-03-06 06:24

from django.db import migrations, models
import django.db.models.deletion
import shop.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='著者')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='タイトル')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('author', models.ForeignKey(default=shop.models.set_default_author, on_delete=django.db.models.deletion.SET_DEFAULT, to='shop.author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
