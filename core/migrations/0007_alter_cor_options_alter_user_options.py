# Generated by Django 5.0.2 on 2024-07-22 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_marca_nacionalidade"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cores", "verbose_name_plural": "Cores"},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Usuários"},
        ),
    ]
