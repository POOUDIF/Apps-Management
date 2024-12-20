from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class BaseModelQuerySet(QuerySet):
    def delete(self):
        return super(BaseModelQuerySet, self).update(deactivated_at=timezone.now(), is_active=False)

    def hard_delete(self):
        return super(BaseModelQuerySet, self).delete()

    def alive(self):
        return self.filter(is_active=False)

    def dead(self):
        return self.exclude(is_active=False)



class BaseModelManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(BaseModelManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return BaseModelQuerySet(self.model).filter(is_active=True)
        return BaseModelQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()

    def get_by_natural_key(self, id):
        return self.get(id=id)



class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'
    name            = models.CharField(max_length=100)
    description     = models.TextField(blank=True, null=True)
    is_active		= models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True, editable=False)
    created_by      = models.CharField(max_length=30, default='Admin', editable=False)
    modified        = models.DateTimeField(editable=False)
    modified_by     = models.CharField(max_length=30, default='Admin', editable=False)
    deactivated_at  = models.DateTimeField(blank=True, null=True, editable=False)

    objects = BaseModelManager()
    all_objects = BaseModelManager(alive_only=False)

    class Meta:
        abstract=True # Set this model as Abstract
        ordering = ['name']

    def __str__(self):
        return '%s'%(self.name)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

    def delete(self):
        self.is_active      = False
        self.deactivated_at = timezone.now()
        self.save()

    def hard_delete(self):
        super(BaseModel, self).delete()


class BaseModelApps(models.Model):  # base class should subclass 'django.db.models.Model'
    created          = models.DateTimeField(auto_now_add=True, editable=False)
    created_by       = models.CharField(max_length=30, default='00000', editable=False)
    created_by_name  = models.CharField(max_length=100, default='Admin', editable=False)
    updated          = models.DateTimeField(auto_now_add=True, editable=True)
    updated_by       = models.CharField(max_length=30, default='00000')
    updated_by_name = models.CharField(max_length=100, default='Admin')

    class Meta:
        abstract=True # Set this model as Abstract

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class BaseModelBBIApps(models.Model):  # base class should subclass 'django.db.models.Model'
    created_at          = models.DateTimeField(auto_now_add=True, editable=False)
    created_by          = models.CharField(max_length=30, default='00000', editable=False)
    created_by_name     = models.CharField(max_length=100, default='Admin', editable=False)
    updated_at          = models.DateTimeField(auto_now_add=True, editable=True)
    updated_by          = models.CharField(max_length=30, default='00000')
    updated_by_name     = models.CharField(max_length=100, default='Admin')
    is_active           = models.BooleanField(default=True)

    class Meta:
        abstract=True # Set this model as Abstract

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
