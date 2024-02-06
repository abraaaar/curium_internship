from django.db import models
from django.contrib.postgres.fields import JSONField
from uuid import uuid4

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email_id = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    org_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    org_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    org_description = models.TextField()
    org_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Membership(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        SURGEON = 'SURGEON'
        TELERADIOLOGIST = 'TELERADIOLOGIST'

    membership_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=20, choices=Role.choices, default=Role.ADMIN)

class UserCredential(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

class VolumeRecord(models.Model):
    class Status(models.TextChoices):
        UPLOADED = 'UPLOADED'
        QUEUED = 'QUEUED'
        PROCESSING = 'PROCESSING'
        INTERMEDIATE_STATE = 'INTERMEDIATE_STATE'
        COMPLETED = 'COMPLETED'

    record_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Organization, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.UPLOADED)
    patient_id = models.CharField(max_length=255)
    study_id = models.CharField(max_length=255)
    volume_meta = JSONField()
    report_meta = JSONField()
    isAutomated = models.BooleanField(default=False)

class ReportStage(models.Model):
    record_id = models.OneToOneField(VolumeRecord, on_delete=models.CASCADE, primary_key=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    intermediate_result = JSONField()
