# Generated by Django 5.0.6 on 2024-06-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, verbose_name='заголовок')),
                ('author', models.CharField(max_length=200, verbose_name='автор')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='кол-во просмотров')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='позиция в списке')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
