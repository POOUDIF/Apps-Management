from django.contrib.auth.models import User, AbstractUser
from django.db import models, IntegrityError

from library.models.bbicore.submodels.base import BaseModel
from library.models.bbicore.submodels.apps import AppAccess, RptAccess

""" Model related to user's profile
#########################################
Returns:
    _type_: _description_
"""

class OrganizationLevel(models.Model):
    code            = models.CharField(max_length=20)
    name            = models.CharField(max_length=100)
    description     = models.TextField(blank=True, null=True)
    is_active		= models.BooleanField(default=True)

    class Meta:
        app_label           = 'bbicore'
        db_table            = 'organization_level'
        verbose_name        = 'Organization Level'
        verbose_name_plural = 'Organization Levels'
    def __str__(self):
        return '%s -- %s'%(self.name, self.code)


class Organization(models.Model):
    code              = models.CharField(max_length=20, blank=True, null=True)
    name              = models.CharField(max_length=100, blank=True, null=True)
    company           = models.CharField(max_length=20, blank=True, null=True)
    parent_unit       = models.CharField(max_length=200, blank=True, null=True)
    type_of_unit      = models.CharField(max_length=200, blank=True, null=True)
    alt_organization  = models.CharField(max_length=200, blank=True, null=True)
    area              = models.CharField(max_length=200, blank=True, null=True)
    sub_area          = models.CharField(max_length=200, blank=True, null=True)
    groupdept         = models.CharField(max_length=200, blank=True, null=True)
    subdept           = models.CharField(max_length=200, blank=True, null=True)
    subdept_name      = models.CharField(max_length=200, blank=True, null=True)
    dept              = models.CharField(max_length=200, blank=True, null=True)
    dept_name         = models.CharField(max_length=200, blank=True, null=True)
    div               = models.CharField(max_length=200, blank=True, null=True)
    div_name          = models.CharField(max_length=200, blank=True, null=True)
    dir               = models.CharField(max_length=200, blank=True, null=True)
    dir_name          = models.CharField(max_length=200, blank=True, null=True)


    class Meta:
        app_label           = 'bbicore'
        db_table            = 'organization'
        verbose_name        = 'Organization'
        verbose_name_plural = 'Organizations'
    def __str__(self):
        return '%s -- %s'%(self.name, self.code)


class Position(models.Model):
    company         = models.CharField(max_length=20, blank=True, null=True)
    position        = models.CharField(max_length=100, blank=True, null=True)
    position_name   = models.CharField(max_length=100, blank=True, null=True)
    pos_hie         = models.IntegerField()

    class Meta:
        app_label           = 'bbicore'
        db_table            = 'position'
        verbose_name        = 'User Position'
        verbose_name_plural = 'User Position'
    def __str__(self):
        return '%s -- %s'%(self.position_name, self.company)


class UserProfile(models.Model):
    OPT_BU          = (('BBI1', 'BBI Pulogadung'), ('AOI1', 'Apparel One Indonesia - 1'),
                       ('AOI2', 'Apparel One Indonesia - 2'), ('AOI3', 'Apparel One Indonesia - 3'), ('AOID', 'Development Center'))
    user     		= models.OneToOneField(User, on_delete=models.CASCADE)
    # name            = models.CharField(max_length=200)
    business_unit   = models.CharField(max_length=20, choices=OPT_BU, default='BBI1')
    nik             = models.CharField(max_length=20, default='00000', verbose_name='NIK')
    old_nik         = models.CharField(max_length=20, blank=True,  null= True, verbose_name='Old NIK')
    organization    = models.CharField(max_length=200, blank=True,  null= True,)
    app_role        = models.ManyToManyField(AppAccess,verbose_name=('Apps Access'))
    rpt_role        = models.ManyToManyField(RptAccess,verbose_name=('Report Access'))
    is_locked       = models.BooleanField(default=False)
    company         = models.CharField(max_length=200, blank=True,  null= True,)
    job             = models.CharField(max_length=200, blank=True,  null= True,)
    position        = models.CharField(max_length=200, blank=True,  null= True,)
    area            = models.CharField(max_length=200, blank=True,  null= True,)
    subarea         = models.CharField(max_length=200, blank=True,  null= True,)
    alt_dept        = models.CharField(max_length=200, blank=True,  null= True,)
    emp_group       = models.CharField(max_length=200, blank=True,  null= True,)
    gender          = models.CharField(max_length=200, blank=True,  null= True,)
    # birth_place     = models.CharField(max_length=200, blank=True,  null= True,)
    birth_date      = models.DateTimeField(null=True, blank=True,)
    marital_status  = models.CharField(max_length=200, blank=True,  null= True,)
    pmtelp          = models.CharField(max_length=500, blank=True,  null= True,)
    ptelp           = models.CharField(max_length=200, blank=True,  null= True,)
    term_eff        = models.DateTimeField(null=True, blank=True,)
    email           = models.CharField(max_length=100, blank=True,  null= True,)
    is_first_login  = models.BooleanField(default=True, editable=False)


    class Meta:
        # abstract    = True
        app_label   = 'bbicore'
        db_table    = 'user_profile'
        ordering    = ['nik']
        indexes = [
            models.Index(fields=['nik']),
        ]
        verbose_name        = 'User Profile'
        verbose_name_plural = 'User Profile'

    def __str__(self):
        return '(%s) %s -- %s'%(self.nik, self.position, self.organization)


class BbiSmgUser(User):
    class Meta:
        app_label   = 'bbicore'
        proxy = True

    def get_or_create(self, username, *args, **kwargs):
        try:
            new_user = User.objects.create_user(username=username, password='r@nD0m_P4s5', first_name=kwargs['name'], last_name= 'BBISemarang')
        except IntegrityError:
            return User.objects.get(username=username)

        return new_user


class AltDept(models.Model):
    name   = models.CharField(max_length=100)
    code   = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label           = 'bbicore'
        verbose_name        = 'Alternative Department'
        verbose_name_plural = 'Alternative Department'
        db_table            = 'alt_dept'


class Company(models.Model):
    name   = models.CharField(max_length=100)
    code   = models.CharField(max_length=50)
    hris_code  = models.CharField(max_length=50)
    description  = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        app_label   = 'bbicore'
        verbose_name        = 'Company'
        verbose_name_plural = 'Company'
        db_table    = 'company'


# class V_ActiveDepartment(models.Model):
#     rowno       = models.IntegerField(primary_key=True)
#     dept_id     = models.IntegerField()
#     dept_code   = models.CharField(max_length=20)
#     dept_name   = models.CharField(max_length=100)

#     class Meta:
#         app_label   = 'bbicore'
#         managed     =   False
#         db_table    = 'v_active_department'

class V_ActiveDivGroup(models.Model):
    id       = models.IntegerField(primary_key=True)
    # dept_id     = models.IntegerField()
    div_group   = models.CharField(max_length=20)
    dept_company   = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_active_div_group'

class V_Organization(models.Model):
    id       = models.IntegerField(primary_key=True)
    code   = models.CharField(max_length=20)
    name   = models.CharField(max_length=100)
    company   = models.CharField(max_length=100)
    parent_unit   = models.CharField(max_length=100)
    type_of_unit   = models.CharField(max_length=100)
    alt_organization   = models.CharField(max_length=100)
    area   = models.CharField(max_length=100)
    sub_area   = models.CharField(max_length=100)
    groupdept         = models.CharField(max_length=200, blank=True, null=True)
    subdept           = models.CharField(max_length=200, blank=True, null=True)
    subdept_name      = models.CharField(max_length=200, blank=True, null=True)
    dept              = models.CharField(max_length=200, blank=True, null=True)
    dept_name         = models.CharField(max_length=200, blank=True, null=True)
    div               = models.CharField(max_length=200, blank=True, null=True)
    div_name          = models.CharField(max_length=200, blank=True, null=True)
    dir               = models.CharField(max_length=200, blank=True, null=True)
    dir_name          = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_org'

class V_ActiveBU(models.Model):
    code    = models.CharField(max_length=20, primary_key=True)
    name    = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_active_business_unit'


class V_BBISmgAccess(models.Model):
    name        = models.CharField(max_length=100)
    factory     = models.CharField(max_length=100)
    is_active   = models.BooleanField()

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_bbismg_access'


class V_ActiveDepartment(models.Model):
    rowno       = models.IntegerField(primary_key=True)
    dept_id     = models.IntegerField()
    dept_code   = models.CharField(max_length=20)
    dept_name   = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_active_department'


class V_ActiveAltDept(models.Model):
    rowno       = models.IntegerField(primary_key=True)
    dept_id     = models.IntegerField()
    dept_code   = models.CharField(max_length=20)
    dept_name   = models.CharField(max_length=100)

    class Meta:
        app_label   = 'bbicore'
        managed     = False
        db_table    = 'v_active_alt_dept'

class V_BbiSmgDept(models.Model):
    rowno       = models.IntegerField(primary_key=True)
    factory     = models.CharField(max_length=20)
    dept_code   = models.CharField(max_length=200)
    dept_name   = models.CharField(max_length=200)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_bbismg_dept_filter'

class V_OrgPath(models.Model):
    code        = models.CharField(max_length=20)
    parent_unit = models.CharField(max_length=20)
    company     = models.CharField(max_length=20)
    path        = models.CharField(max_length=200)
    name        = models.CharField(max_length=200)
    type_of_unit= models.CharField(max_length=20)
    groupdept   = models.CharField(max_length=200)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_orgpath'

class V_OrgPathBBI(models.Model):
    code        = models.CharField(max_length=20)
    parent_unit = models.CharField(max_length=20)
    company     = models.CharField(max_length=20)
    path        = models.CharField(max_length=200)
    name        = models.CharField(max_length=200)
    groupdept   = models.CharField(max_length=200)


    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_orgpath_bbi'

class V_OrgPathAOI(models.Model):
    code        = models.CharField(max_length=20)
    parent_unit = models.CharField(max_length=20)
    company     = models.CharField(max_length=20)
    path        = models.CharField(max_length=200)
    name        = models.CharField(max_length=200)
    type_of_unit= models.CharField(max_length=20)
    groupdept   = models.CharField(max_length=200)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_orgpath_aoi'

class V_user(models.Model):
    nik = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="NO")
    organization_name = models.CharField(max_length=255)
    position = models.CharField(max_length=20)
    position_name = models.CharField(max_length=20)
    job = models.CharField(max_length=100)
    # date = models.DateTimeField()
    gender = models.CharField(max_length=2)
    area = models.CharField(max_length=50)
    subarea = models.CharField(max_length=50)
    business_unit = models.CharField(max_length=100)

    class Meta:
        app_label = 'bbicore'
        managed   = False
        db_table  = 'v_user_bbi'


class V_OrgGroup(models.Model):
    company         = models.CharField(max_length=200)
    groupdept       = models.CharField(max_length=200)

    class Meta:
        app_label   = 'bbicore'
        managed = False
        db_table = 'v_org_groupdept'

class MultiDepartment(models.Model):
    nik             = models.CharField(max_length=250,null=True)
    name            = models.CharField(max_length=250,null=True)
    bu              = models.CharField(max_length=250,null=True)
    dept            = models.CharField(max_length=250,null=True)
    is_active       = models.BooleanField()

    class Meta:
        app_label           = 'bbicore'
        verbose_name        = 'Multiple Department'
        verbose_name_plural = 'Multiple Department'
        db_table            = 'multi_department'
        indexes = [
            models.Index(fields=['nik']),
        ]