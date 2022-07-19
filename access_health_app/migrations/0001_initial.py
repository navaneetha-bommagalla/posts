# Generated by Django 3.2.14 on 2022-07-19 15:33

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_description', models.TextField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_on', models.DateTimeField(auto_now_add=True)),
                ('liked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_by', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='access_health_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disliked_on', models.DateTimeField(auto_now_add=True)),
                ('disliked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='disliked_by', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dislikes', to='access_health_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('commented_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('commented_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commented_user', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_parent', to='access_health_app.comment')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='access_health_app.post')),
            ],
        ),
    ]
