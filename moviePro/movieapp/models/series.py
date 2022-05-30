from django.db import models

class series(models.Model):
    name=models.CharField(verbose_name="Serinin Adı",max_length=80,blank=False,null=False)

    class Meta:
        verbose_name="series"
        verbose_name_plural="Seriler"
        db_table="tblserie"

    def __str__(self):
        return self.name