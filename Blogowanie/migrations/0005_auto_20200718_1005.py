# Generated by Django 3.0.8 on 2020-07-18 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blogowanie', '0004_auto_20200714_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogowanie.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='id_blog',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='Blogowanie.Blog'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogowanie.User'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blogowanie.User'),
        ),
    ]
