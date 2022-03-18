from medapp.models import Patient, Case, Document, DocumentBody, RequestLog
from medapp.serializers import PatientSerializer, CaseSerializer, DocumentSerializer, DocumentBodySerializer, \
    RequestLogSerializer
from rest_framework import generics


class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    class Meta:
        ordering = ['created']


class CaseList(generics.ListCreateAPIView):
    # queryset = Case.objects.all()
    serializer_class = CaseSerializer

    def get_queryset(self):
        if self.kwargs.get("patient_id"):
            return Case.objects.filter(patient_id=self.kwargs.get("patient_id"))
        return Case.objects.all()


class CaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

    # class Meta:
    #     ordering = ['patient_id']



class DocumentList(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DocumentBodyList(generics.ListCreateAPIView):
    queryset = DocumentBody.objects.all()
    serializer_class = DocumentBodySerializer


class DocumentBodyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentBody.objects.all()
    serializer_class = DocumentBodySerializer


class RequestLogList(generics.ListCreateAPIView):
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer


class RequestLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequestLog.objects.all()
    serializer_class = RequestLogSerializer
