# Generated by Django 4.2.10 on 2024-04-10 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to='events', verbose_name='Аватар')),
                ('title', models.TextField(unique=True, verbose_name='Мероприятие')),
                ('description', models.TextField(verbose_name='Описание')),
                ('used_skills', models.TextField(blank=True, null=True, verbose_name='Испольщующиеся навыки')),
                ('detailed', models.TextField(blank=True, null=True, verbose_name='Подробнее')),
                ('number_of_participants', models.PositiveIntegerField(default=0, verbose_name='Количестов участников')),
                ('date', models.DateTimeField(verbose_name='Дата и время начала события')),
                ('duration', models.DurationField(verbose_name='Длительность события')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='EventResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField(default=0, verbose_name='Баллы')),
            ],
            options={
                'verbose_name': 'Результат события',
                'verbose_name_plural': 'Результаты события',
            },
        ),
        migrations.CreateModel(
            name='EventStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='Статус события')),
            ],
            options={
                'verbose_name': 'Статус события',
                'verbose_name_plural': 'Статусы события',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='programming_languages', verbose_name='Иконка')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Языки программирования',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField(verbose_name='Результат')),
                ('is_right', models.BooleanField(default=False, verbose_name='Правильность')),
            ],
            options={
                'verbose_name': 'Результат',
                'verbose_name_plural': 'Результаты',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True, verbose_name='Заголовок')),
                ('condition', models.TextField(verbose_name='Условие')),
                ('note', models.TextField(blank=True, verbose_name='Примечание')),
                ('answer_structure', models.TextField(blank=True, default='#Введите ваш код здесь', verbose_name='Структура ответа')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Комментарий')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')),
                ('like', models.PositiveIntegerField(default=0, verbose_name='Количество лайков')),
            ],
            options={
                'verbose_name': 'Комментарий к заданию',
                'verbose_name_plural': 'Комментарии к заданям',
            },
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_data', models.TextField(verbose_name='Входные данные')),
                ('output_data', models.TextField(verbose_name='Выходные данные')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.task', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Тестовые данные',
                'verbose_name_plural': 'Тестовые данные',
            },
        ),
        migrations.CreateModel(
            name='TaskReward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp', models.PositiveIntegerField(verbose_name='Опыт')),
                ('points', models.PositiveIntegerField(verbose_name='Поинты')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Event.task', verbose_name='Задание')),
            ],
            options={
                'verbose_name': 'Награда за задание',
                'verbose_name_plural': 'Награды за задания',
            },
        ),
    ]
