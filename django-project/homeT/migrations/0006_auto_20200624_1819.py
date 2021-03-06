# Generated by Django 3.0.7 on 2020-06-24 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeT', '0005_auto_20200624_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='video',
            name='tag_set',
        ),
        migrations.RemoveField(
            model_name='video',
            name='tagcontent',
        ),
        migrations.AddField(
            model_name='video',
            name='tag',
            field=models.CharField(default=django.utils.timezone.now, help_text='카테고리가 될 태그를 입력해주세요', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='tags',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeT.Video'),
        ),
    ]
