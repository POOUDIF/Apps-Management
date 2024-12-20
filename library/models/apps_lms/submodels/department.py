from django.db import models

class Department(models.Model):
    dept_name       = models.CharField(max_length=300)
    dept_code       = models.CharField(max_length=50,null=True)
    dept_bu         = models.CharField(max_length=300,null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'department'


# DMS LEGAL Department Mapping

class LegalDepartmentMapping(models.Model):
    business_unit   = models.CharField(max_length=20, blank=True, null=True)
    department      = models.CharField(max_length=50, blank=True, null=True)
    created_by      = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    update_by       = models.CharField(max_length=100, blank=True, null=True)
    update_at       = models.DateTimeField(blank=True, null=True)
    is_active       = models.BooleanField(blank=True, null=True)
    group_id        = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'legal_department_mapping'

class V_LegalDepartmentMapping(models.Model):
    business_unit   = models.CharField(max_length=20, blank=True, null=True)
    department      = models.CharField(max_length=50, blank=True, null=True)
    created_by      = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    update_by       = models.CharField(max_length=100, blank=True, null=True)
    update_at       = models.DateTimeField(blank=True, null=True)
    is_active       = models.BooleanField(blank=True, null=True)
    group_id        = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        app_label   = 'apps_lms'
        db_table = 'v_legal_department_mapping'

class LegalDepartmentPIC(models.Model):
    nik             = models.CharField(max_length=20, blank=True, null=True)
    cc              = models.BooleanField(blank=True, null=True)
    mapping         = models.ForeignKey(LegalDepartmentMapping, on_delete=models.CASCADE, blank=True, null=True)
    email           = models.CharField(max_length=150, blank=True, null=True)
    jabatan         = models.CharField(max_length=100, blank=True, null=True)
    jabatan_detail  = models.CharField(max_length=100, blank=True, null=True)
    created_by      = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    update_by       = models.CharField(max_length=100, blank=True, null=True)
    update_at       = models.DateTimeField(blank=True, null=True)
    is_active       = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'legal_department_pic'

class V_LegalDepartmentPIC(models.Model):
    nik                 = models.CharField(max_length=20, blank=True, null=True)
    cc                  = models.BooleanField(blank=True, null=True)
    mapping             = models.ForeignKey(LegalDepartmentMapping, on_delete=models.CASCADE, blank=True, null=True)
    email               = models.CharField(max_length=150, blank=True, null=True)
    jabatan         = models.CharField(max_length=100, blank=True, null=True)
    jabatan_detail  = models.CharField(max_length=100, blank=True, null=True)
    created_by          = models.CharField(max_length=100, blank=True, null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    update_by           = models.CharField(max_length=100, blank=True, null=True)
    update_at           = models.DateTimeField(blank=True, null=True)
    is_active           = models.BooleanField(blank=True, null=True)
    department          = models.CharField(max_length=100, blank=True, null=True)
    business_unit       = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        app_label   = 'apps_lms'
        db_table    = 'v_legal_department_pic'

class DepartmentGroup(models.Model):
    group_name = models.CharField(max_length=100)
    created_by  = models.CharField(max_length=50)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=50,null=True,default=None)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    deleted_by  = models.CharField(max_length=50,null=True,default=None)
    deleted_at  = models.DateTimeField(null=True,default=None)
    is_active           = models.BooleanField(blank=True, null=True)
    direksi_id          = models.CharField(max_length=150,null=True,default=None)
    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'department_group'

class LegalDepartmentGroupPIC(models.Model):
    nik             = models.CharField(max_length=20, blank=True, null=True)
    cc              = models.BooleanField(blank=True, null=True)
    group_id        = models.IntegerField(blank=True, null=True)
    email           = models.CharField(max_length=150, blank=True, null=True)
    jabatan         = models.CharField(max_length=100, blank=True, null=True)
    jabatan_detail  = models.CharField(max_length=100, blank=True, null=True)
    created_by      = models.CharField(max_length=100, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_by       = models.CharField(max_length=100, blank=True, null=True)
    updated_at       = models.DateTimeField(blank=True, null=True)
    deleted_by       = models.CharField(max_length=100, blank=True, null=True)
    deleted_at       = models.DateTimeField(blank=True, null=True)
    is_active       = models.BooleanField(blank=True, null=True)

    class Meta:
        app_label   = 'apps_lms'
        db_table    = 'legal_department_group_pic'