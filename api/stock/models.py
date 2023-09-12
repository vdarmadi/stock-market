from django.db import models


# Create your models here.
class StockPrice(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(blank=True, null=True)
    open = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=20)
    high = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=20)
    low = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=20)
    close = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=20)
    adj_close = models.DecimalField(blank=True, null=True, max_digits=25, decimal_places=20)
    volume = models.IntegerField(blank=True, null=True)
    cdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'stock_price'
