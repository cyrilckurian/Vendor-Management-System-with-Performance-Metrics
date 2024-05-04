from django.urls import path
from .views import VendorListCreate, VendorRetrieveUpdateDestroy, PurchaseOrderListCreate, PurchaseOrderRetrieveUpdateDestroy, VendorPerformance, AcknowledgePurchaseOrder

urlpatterns = [
    path('vendors/', VendorListCreate.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorRetrieveUpdateDestroy.as_view(), name='vendor-retrieve-update-destroy'),
	path('vendors/<int:pk>/performance/', VendorPerformance.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListCreate.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchase-order-retrieve-update-destroy'),
	path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge-purchase-order'),
]
