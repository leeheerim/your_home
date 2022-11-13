from django.db import models

# Create your models here.
class Table(models.Model):
    번호=models.FloatField()
    주택관리번호=models.FloatField()
    공고번호=models.FloatField()
    주택명=models.CharField(max_length=20)
    위도=models.FloatField()
    경도=models.FloatField()
    공급위치=models.CharField(max_length=30)

class maket(models.Model):
    번호=models.FloatField()
    시장명=models.CharField(max_length=30)
    시장유형=models.CharField(max_length=10)
    위도=models.FloatField()
    경도=models.FloatField()
    소재지도로명주소=models.CharField(max_length=30)
    시장개설주기=models.CharField(max_length=10)
    소재지지번주소=models.CharField(max_length=30)
    점포수=models.FloatField()
    사용가능상품권=models.CharField(max_length=20)
    공중화장실보유여부=models.CharField(max_length=5)
    주차장보유여부=models.CharField(max_length=5)
    개설년도=models.FloatField()

class school(models.Model):
    번호=models.FloatField()
    학교ID=models.FloatField()
    학교명=models.CharField(max_length=20)
    학교급구분=models.CharField(max_length=10)
    설립일자=models.CharField(max_length=30)
    설립형태=models.CharField(max_length=10)
    소재지지번주소=models.CharField(max_length=30)
    소재지도로명주소=models.CharField(max_length=30)
    위도=models.FloatField()
    경도=models.FloatField()