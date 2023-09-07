from django.shortcuts import render
from rest_framework.decorators import api_view
import pandas as pd 
from .models import Excel
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExcelSerializer

@api_view(['POST'])
def upload_file(request):
    excel_file = request.FILES.get('file')

    if excel_file:
        try:
            df = pd.read_excel(excel_file, engine='openpyxl')
            
            required_columns = {'name', 'salary', 'percentage'}
            if not required_columns.issubset(df.columns):
                return Response({'error': 'Excel file must contain columns: name, salary, percentage'}, status=status.HTTP_400_BAD_REQUEST)

            for index, row in df.iterrows():
                Excel.objects.create(name=row['name'], salary=row['salary'], percentage=row['percentage'])

            return Response({'message': 'Excel data uploaded successfully!'})
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_names(request):
    names = Excel.objects.all()
    serializers =ExcelSerializer(names, many=True)
    return Response(serializers.data)