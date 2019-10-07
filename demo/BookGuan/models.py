from django.db import models
class Goods(models.Model):
    goods_number = models.CharField(max_length=11, verbose_name="书籍编号")
    goods_name = models.CharField(max_length=32, verbose_name="书籍名称")
    goods_status = models.IntegerField(verbose_name="书籍状态",default=1)
    goods_pro_time = models.DateField(auto_now=True, verbose_name="出版日期")
    goods_author_name=models.CharField(max_length=32,verbose_name='作者名字')
    type_name = models.CharField(max_length=32, verbose_name='类型名字')
    goods_title = models.CharField(max_length=32, verbose_name='文章')
    goods_content = models.TextField(verbose_name='内容')
    goods_description = models.TextField(verbose_name='描述')
    picture = models.ImageField(upload_to='images')

# class Goods(models.Model):
#     goods_number=models.CharField(max_length=11,verbose_name="书籍编号")
#     goods_name = models.CharField(max_length=32, verbose_name="书籍名称")
#     goods_price = models.FloatField(verbose_name="书籍价格")
#     goods_count = models.IntegerField(verbose_name="书籍数量")
#     goods_status = models.IntegerField(verbose_name="书籍状态")
#     goods_pro_time= models.DateField(auto_now=True, verbose_name="出版日期")
#     picture = models.ImageField(upload_to="images")
#     goods_type=models.ForeignKey(to=GoodsType,on_delete=models.CASCADE,default=1)
#     goods_store=models.ForeignKey(to=LoginUser,on_delete=models.CASCADE,default=1)
#     goods_description=models.TextField(default="欢迎")
#     photo = models.ImageField(upload_to="images", null=True, blank=True)
#     class Meta:
#         db_table='goods'
#
# class Type(models.Model):
#     name=models.CharField(max_length=32,verbose_name='类型名字')
#     description=models.TextField(verbose_name='类型描述')
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table='type'
#         verbose_name_plural='类型'


# from django.db import models
# from ckeditor.fields import RichTextField
# # Create your models here.
# GENDER_LIST=(
#     (1,'男'),
#     (2,'女')
# )
#
# class Author(models.Model):
#     name=models.CharField(max_length=32,verbose_name='作者名字')
#     age=models.IntegerField(verbose_name='年龄')
#     # gender=models.CharField(max_length=8,verbose_name='性别')
#     gender=models.IntegerField(choices=GENDER_LIST,verbose_name='性别')
#     email=models.CharField(max_length=32,verbose_name='邮箱')
#     def __str__(self):
#         return self.name
#     class Meta:
#         db_table='auther'
#         verbose_name_plural='作者'

# class Article(models.Model):
#     title=models.CharField(max_length=32,verbose_name='文章')
#     date=models.DateField(auto_now=True,verbose_name='日期')
#     # content=models.TextField(verbose_name='内容')
#     content =RichTextField()
#     # description=models.TextField(verbose_name='描述')
#     description = RichTextField()
#     #图片类型
#     picture=models.ImageField(upload_to='images')

#
#
#     def __str__(self):
#         return self.title
#     class Meta:
#         db_table='article'
#         verbose_name_plural='文章'
#
# class User(models.Model):
#     name = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#
#     class Meta:
#         db_table='user'
