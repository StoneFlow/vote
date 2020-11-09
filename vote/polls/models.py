# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Subject(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural = '学科'

SEX_OPTIONS = ((True, '男'),(False, '女'))


class Teachers(models.Model):
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    sex = models.BooleanField(choices=SEX_OPTIONS, default=True, verbose_name='性别')
    birth = models.DateField(verbose_name='出生日期')
    intro = models.CharField(max_length=1000, verbose_name='介绍')
    photo = models.CharField(max_length=255, verbose_name='照片')
    good_count = models.IntegerField(default=0, db_column='gcount', verbose_name='好评数')
    bad_count = models.IntegerField(default=0, db_column='bcount', verbose_name='差评数')
    subject = models.ForeignKey(to=Subject, on_delete=models.DO_NOTHING, db_column='sno', verbose_name='所属学科')

    class Meta:
        managed = False
        db_table = 'tb_teachers'
        verbose_name = '老师'
        verbose_name_plural = '老师'
