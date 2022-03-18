from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Patient(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('birth date', null=True)
    gender = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Case(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    begin_date = models.DateTimeField()
    close_date = models.DateTimeField(null=True)
    result = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.result


class Document(models.Model):
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True)
    header = models.CharField(max_length=200)
    doc_date = models.IntegerField(default=0)

    def __str__(self):
        return self.header


class DocumentBody(models.Model):
    doc = models.OneToOneField(Document, on_delete=models.CASCADE)
    doc_filling = models.JSONField(max_length=200)

    def __str__(self):
        return self.doc_filling


class RequestLog(models.Model):
    timestamp = models.DateTimeField()
    choice_text = models.JSONField(max_length=200)

    def __str__(self):
        return self.choice_text
