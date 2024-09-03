from django.db import models
from pymysql import NULL

class Admin(models.Model):
    id = models.CharField(max_length=25, unique=True,primary_key=True)
    password = models.CharField(max_length=25)



class User(models.Model):
    id = models.CharField(max_length=55, unique=True,primary_key=True)
    password = models.CharField(max_length=25)
    name=models.CharField(max_length=80,default=id)
    gender=models.CharField(max_length=15,blank=True, null=True)
    age=models.CharField(max_length=20,blank=True, null=True)
    phonenumber=models.CharField(max_length=20,blank=True, null=True)
    education=models.CharField(max_length=80,blank=True, null=True)
    workout=models.CharField(max_length=20,blank=True, null=True)
    readnwrite=models.CharField(max_length=20,blank=True, null=True)
    sleeping=models.CharField(max_length=30,blank=True, null=True)
    smoking=models.CharField(max_length=6,blank=True, null=True)
    diet=models.CharField(max_length=6,blank=True, null=True)
    living=models.CharField(max_length=28,blank=True, null=True)
    working=models.CharField(max_length=28,blank=True, null=True)
    ADhistory=models.CharField(max_length=6,blank=True, null=True)
    disease=models.CharField(max_length=6,blank=True, null=True)
    TBI=models.CharField(max_length=6,blank=True, null=True)

class PicTest(models.Model):
    record_id = models.AutoField(primary_key=True)  # 新的自动生成的主键字段
    testId = models.CharField(max_length=55, unique=False)
    testDate = models.CharField(max_length=20, blank=True, null=True, default='0000-00-00')
    audio = models.BinaryField(blank=True, null=True)  # 用于存储二进制数据，如音频文件

class QuestionTest(models.Model):
    record_id = models.AutoField(primary_key=True)  # 新的自动生成的主键字段
    testId = models.CharField(max_length=55, unique=False)
    testDate = models.CharField(max_length=20, blank=True, null=True, default='0000-00-00')
    todayDate = models.IntegerField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    remember = models.IntegerField(blank=True, null=True)
    calculate = models.IntegerField(blank=True, null=True)
    memorize = models.IntegerField(blank=True, null=True)
    named = models.IntegerField(blank=True, null=True)
    repeating = models.IntegerField(blank=True, null=True)
    commandOperate = models.IntegerField(blank=True, null=True)
    wordOperate = models.IntegerField(blank=True, null=True)
    writing = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    notes = models.TextField(max_length=800, blank=True, null=True)
    audio = models.BinaryField(blank=True, null=True)  # 用于存储二进制数据，如音频文件