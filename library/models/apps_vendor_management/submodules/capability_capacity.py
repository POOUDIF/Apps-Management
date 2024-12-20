# from django.db import models

# class VendorCapabilityCapacity(models.Model):
#     vendor_code = models.CharField(max_length=300, null=True)
#     business_category = models.CharField(max_length=300, null=True)
#     vendor_code_sap = models.CharField(max_length=300, null=True)
#     vendor_name = models.CharField(max_length=300, null=True)
#     category_product = models.CharField(max_length=300, null=True)
#     service_type = models.CharField(max_length=300, null=True)
#     vendor_capacity = models.BigIntegerField(default=0, null=True)
#     status      = models.BooleanField(default=True)
#     created_by = models.CharField(max_length=50, null=True)
#     created_at = models.DateTimeField(default=None, null=True, blank=True)
#     updated_by = models.CharField(max_length=50, null=True, default=None)
#     updated_at = models.DateTimeField(auto_now_add=True, blank=True)
#     deleted_by = models.CharField(max_length=50, null=True, default=None)
#     deleted_at = models.DateTimeField(null=True, default=None)

#     class Meta:
#         app_label   = 'apps_vendor_management'
#         db_table    = 'vendor_capability_capacity'

# # class V_VendorCapabilityCapacity(models.Model):
# #     vendor_code = models.CharField(max_length=300, null=True)
# #     business_category = models.CharField(max_length=300, null=True)
# #     vendor_code_sap = models.CharField(max_length=300, null=True)
# #     vendor_name = models.CharField(max_length=300, null=True)
# #     category_product = models.CharField(max_length=300, null=True)
# #     service_type = models.CharField(max_length=300, null=True)
# #     vendor_capacity = models.BigIntegerField(default=0, null=True)
# #     status      = models.BooleanField(default=True)
# #     created_by = models.CharField(max_length=50, null=True)
# #     created_at = models.DateTimeField(default=None, null=True, blank=True)
# #     updated_by = models.CharField(max_length=50, null=True, default=None)
# #     updated_at = models.DateTimeField(auto_now_add=True, blank=True)
# #     deleted_by = models.CharField(max_length=50, null=True, default=None)
# #     deleted_at = models.DateTimeField(null=True, default=None)

# #     class Meta:
# #         app_label   = 'apps_vendor_management'
# #         db_table    = 'v_vendor_capability_capacity'
# #         managed     = False