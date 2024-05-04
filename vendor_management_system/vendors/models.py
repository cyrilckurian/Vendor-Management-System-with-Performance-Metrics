from audioop import avg
from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def calculate_performance_metrics(self):
        # On-Time Delivery Rate
        completed_orders = PurchaseOrder.objects.filter(vendor=self.vendor, status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=timezone.now())
        self.vendor.on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0

        # Quality Rating Average
        completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
        self.vendor.quality_rating_avg = completed_orders_with_rating.aggregate(avg_quality=avg('quality_rating'))['avg_quality'] if completed_orders_with_rating.exists() else 0

        # Average Response Time
        acknowledged_orders = completed_orders.exclude(acknowledgment_date__isnull=True)
        self.vendor.average_response_time = acknowledged_orders.aggregate(avg_response=avg(F('acknowledgment_date') - F('issue_date')))['avg_response'].total_seconds() / acknowledged_orders.count() if acknowledged_orders.exists() else 0

        # Fulfillment Rate
        successful_orders = completed_orders.exclude(status='canceled')
        self.vendor.fulfillment_rate = (successful_orders.count() / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0

        self.vendor.save()

    def acknowledge_order(self):
        self.acknowledgment_date = timezone.now()
        self.save()
        self.calculate_performance_metrics()

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
