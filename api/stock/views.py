from django.db.models import Q
from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from stock.models import StockPrice
from stock.serializers import StockPriceSerializer


class StockDataListCreate(generics.ListCreateAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer

    def post(self, request, format=None):
        serializer = StockPriceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        # Get query parameters for date filtering
        start_date_param = request.query_params.get('start_date')

        # Parse date parameters
        start_date = parse_date(start_date_param) if start_date_param else None

        # Build a query for date filtering
        date_filter = Q()
        if start_date:
            date_filter &= Q(cdate__gte=start_date)

        # Query the database with the date filter
        stock_data = StockPrice.objects.filter(date_filter)

        serializer = StockPriceSerializer(stock_data, many=True)
        return Response(serializer.data)


class StockDataReset(generics.CreateAPIView):

    def post(self, request, format=None):
        StockPrice.objects.all().delete()
        return Response(status=HTTP_200_OK, data={'message': "All records deleted"})
