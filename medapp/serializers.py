from rest_framework import serializers
from medapp.models import Patient, Case, Document, DocumentBody, RequestLog, LANGUAGE_CHOICES, STYLE_CHOICES


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'birth_date', 'gender']


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ['patient_id', 'begin_date', 'close_date', 'result']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['patient_id', 'case', 'header', 'doc_date']


class DocumentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentBody
        fields = ['doc', 'doc_filling']


class RequestLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLog
        fields = ['timestamp', 'choice_text']
