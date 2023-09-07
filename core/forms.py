from django import forms


class ExcelUploadFile(forms.Form):
    excel_file = forms.FileField()