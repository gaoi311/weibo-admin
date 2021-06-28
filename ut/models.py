# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'admin'


class Admire(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    blog = models.ForeignKey('Blog', models.DO_NOTHING)
    is_saw = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'admire'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Blog(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    topic = models.ForeignKey('Topic', models.DO_NOTHING)
    content = models.CharField(max_length=765)
    created_time = models.DateTimeField()
    likes = models.IntegerField()
    pictures = models.CharField(max_length=2303, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blog'


class Collection(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    is_saw = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'collection'


class Comment(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    blog = models.ForeignKey(Blog, models.DO_NOTHING)
    content = models.CharField(max_length=255)
    created_time = models.DateTimeField()
    is_saw = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'comment'


class Follow(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='u1')
    other = models.ForeignKey('User', models.DO_NOTHING, related_name='u2')
    is_saw = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'follow'


class Topic(models.Model):
    name = models.CharField(unique=True, max_length=255)
    created_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'topic'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    avatar = models.CharField(max_length=255)
    is_blocked = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'user'
