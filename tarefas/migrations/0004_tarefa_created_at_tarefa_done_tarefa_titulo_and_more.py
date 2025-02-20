# Generated by Django 5.1.3 on 2024-11-21 20:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_alter_tarefa_tarefas'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='done',
            field=models.CharField(choices=[(1, 'doing'), (2, 'done')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='titulo',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarefa',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='tarefas',
            field=models.TextField(),
        ),
    ]
