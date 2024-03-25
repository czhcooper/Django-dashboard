from django.db import models
from django.conf import settings
# Create your models here.

#测试
class City(models.Model):
    """ 城市 """
    name = models.CharField(verbose_name="名称", max_length=32)
    count = models.IntegerField(verbose_name="人口")

    # 本质上数据库也是CharField，自动保存数据。
    img = models.FileField(verbose_name="Logo", max_length=128, upload_to='city/')


#上传rna-seq数据
class rnaseq(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    user_name = models.CharField(max_length=128, verbose_name="用户名",default="")
    file_path = models.CharField(max_length=128, verbose_name="文件路径",default="")
    #file_path = models.FileField(upload_to='rnaseq/', max_length=128, verbose_name="文件路径")

    def __str__(self):
        return self.file_path