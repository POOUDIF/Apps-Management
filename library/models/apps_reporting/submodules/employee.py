from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver

from library.models.bbicore import BaseModel



class MasterEmployee(models.Model):
    empid       = models.CharField(max_length=100, null=True, blank=True)
    name        = models.CharField(max_length=500, null=True, blank=True)
    company     = models.CharField(max_length=20, null=True, blank=True)
    job         = models.CharField(max_length=20, null=True, blank=True)
    position    = models.CharField(max_length=20, null=True, blank=True)
    unit        = models.CharField(max_length=20, null=True, blank=True)
    area        = models.CharField(max_length=500, null=True, blank=True)
    subarea     = models.CharField(max_length=500, null=True, blank=True)
    emp_group   = models.CharField(max_length=20, null=True, blank=True)
    gender      = models.CharField(max_length=5, null=True, blank=True)
    birth_place = models.CharField(max_length=500, null=True, blank=True)
    birth_date  = models.DateField(null=True, blank=True)
    marital_status  = models.CharField(max_length=5, null=True, blank=True)
    pmtelp      = models.CharField(max_length=100, null=True, blank=True)
    ptelp       = models.CharField(max_length=100, null=True, blank=True)
    term_eff    = models.DateField(null=True, blank=True)
    termination = models.CharField(max_length=500, null=True, blank=True)
    education   = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        app_label   = 'hris_master'
        db_table    = 'm_employee'
        managed     = False


class V_EmpDemographSummary(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    total_gender_male   = models.IntegerField()
    total_gender_female = models.IntegerField()
    total_edu_sd        = models.IntegerField()
    total_edu_smp       = models.IntegerField()
    total_edu_smu       = models.IntegerField()
    total_edu_smk_d2    = models.IntegerField()
    total_edu_d3_d4     = models.IntegerField()
    total_edu_s1        = models.IntegerField()
    total_edu_s2        = models.IntegerField()
    total_edu_s3        = models.IntegerField()
        
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemographsummary'


class V_EmpDemographEdu(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    total_edu_sd        = models.IntegerField()
    total_edu_smp       = models.IntegerField()
    total_edu_smu       = models.IntegerField()
    total_edu_smk_d2    = models.IntegerField()
    total_edu_d3_d4     = models.IntegerField()
    total_edu_s1        = models.IntegerField()
    total_edu_s2        = models.IntegerField()
    total_edu_s3        = models.IntegerField()
    
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemograph_edu'

class V_EmpDemographGender(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    total_gender_male   = models.IntegerField()
    total_gender_female = models.IntegerField()
    
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemograph_gender'

class V_EmpDemographEmpGroup(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    empgroup_contract   = models.IntegerField()
    empgroup_probation  = models.IntegerField()
    empgroup_permanent  = models.IntegerField()
    empgroup_others     = models.IntegerField()
    
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemograph_empgroup'

class V_EmpDemographAgeGenderDist(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    agegroup_1_male     = models.IntegerField()
    agegroup_1_female   = models.IntegerField()
    agegroup_2_male     = models.IntegerField()
    agegroup_2_female   = models.IntegerField()
    agegroup_3_male     = models.IntegerField()
    agegroup_3_female   = models.IntegerField()
    agegroup_4_male     = models.IntegerField()
    agegroup_4_female   = models.IntegerField()
    agegroup_5_male     = models.IntegerField()
    agegroup_5_female   = models.IntegerField()
    agegroup_others_male    = models.IntegerField()
    agegroup_others_female  = models.IntegerField()
    
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemograph_agegender_dist'
        
class V_EmpDemographAgeTenureDist(models.Model):
    row_number          = models.IntegerField(primary_key=True)
    company             = models.CharField(max_length=100)
    agegroup_1_tenure_1 = models.IntegerField()
    agegroup_1_tenure_2 = models.IntegerField()
    agegroup_1_tenure_3 = models.IntegerField()
    agegroup_1_tenure_4 = models.IntegerField()
    agegroup_2_tenure_1 = models.IntegerField()
    agegroup_2_tenure_2 = models.IntegerField()
    agegroup_2_tenure_3 = models.IntegerField()
    agegroup_2_tenure_4 = models.IntegerField()
    agegroup_3_tenure_1 = models.IntegerField()
    agegroup_3_tenure_2 = models.IntegerField()
    agegroup_3_tenure_3 = models.IntegerField()
    agegroup_3_tenure_4 = models.IntegerField()
    agegroup_4_tenure_1 = models.IntegerField()
    agegroup_4_tenure_2 = models.IntegerField()
    agegroup_4_tenure_3 = models.IntegerField()
    agegroup_4_tenure_4 = models.IntegerField()
    agegroup_5_tenure_1 = models.IntegerField()
    agegroup_5_tenure_2 = models.IntegerField()
    agegroup_5_tenure_3 = models.IntegerField()
    agegroup_5_tenure_4 = models.IntegerField()
    agegroup_others_tenure_1 = models.IntegerField()
    agegroup_others_tenure_2 = models.IntegerField()
    agegroup_others_tenure_3 = models.IntegerField()
    agegroup_others_tenure_4 = models.IntegerField()
    
    class Meta:
        managed     = False
        app_label   = 'hris_master'
        db_table    = 'v_empdemograph_agetenure_dist'