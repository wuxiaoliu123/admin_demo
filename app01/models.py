from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    age=models.IntegerField()
    #将admin中的表名替换成中文
    class Meta:
        verbose_name = "作者"
        verbose_name_plural =verbose_name

    # 与AuthorDetail建立一对一的关系
    authorDetail=models.OneToOneField(to="AuthorDetail",on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AuthorDetail(models.Model):

    nid = models.AutoField(primary_key=True)
    birthday=models.DateField()
    telephone=models.BigIntegerField()
    addr=models.CharField( max_length=64)

    #将admin中的表名替换成中文
    class Meta:
        verbose_name = "作者信息"
        verbose_name_plural =verbose_name

        # def __str__(self):
        #     return self.birthday

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name=models.CharField( max_length=32)
    city=models.CharField( max_length=32)
    email=models.EmailField()

    #将admin中的表名替换成中文
    class Meta:
        verbose_name = "出版社"
        verbose_name_plural =verbose_name


    def __str__(self):
        return self.name


class Book(models.Model):

    nid = models.AutoField(primary_key=True)
    title = models.CharField( max_length=32)
    publishDate=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2)

    # 与Publish建立一对多的关系,外键字段建立在多的一方
    publish=models.ForeignKey(to="Publish",to_field="nid",on_delete=models.CASCADE)
    # 与Author表建立多对多的关系,ManyToManyField可以建在两个模型中的任意一个，自动创建第三张表
    authors=models.ManyToManyField(to='Author',)

    #将admin中的表名替换成中文
    class Meta:
        verbose_name = "书籍"
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.title