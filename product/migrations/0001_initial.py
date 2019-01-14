# Generated by Django 2.1.2 on 2019-01-13 02:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '收藏',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('goods_price', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('description', models.TextField(max_length=300, verbose_name='商品描述')),
                ('goods_img1', models.CharField(max_length=100)),
                ('goods_img2', models.CharField(max_length=100, null=True)),
                ('goods_img3', models.CharField(max_length=100, null=True)),
                ('goods_img4', models.CharField(max_length=100, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'ordering': ['-c_time'],
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AddField(
            model_name='collection',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]
