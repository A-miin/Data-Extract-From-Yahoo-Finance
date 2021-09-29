from django import http
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from bs4 import BeautifulSoup
import requests
from datetime import datetime

from yahoo_scraping.serializers import DataSerializer
from yahoo_scraping.models import Data



class APIDataView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, *args, **kwargs):
        company = request.GET['company']
        try:
            items = get_data(company)
        except Exception as e:
            Response({'message': e}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DataSerializer(data=items, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


def get_data(company):
    result = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://finance.yahoo.com/quote/LCID/history?p={company}'
    html = requests.get(url, headers=headers)

    if html.status_code != 200:
        raise http.HttpResponseBadRequest

    soup = BeautifulSoup(html.text, 'html.parser')
    table = soup.find('table', {"data-test": "historical-prices"})
    tbody = table.find('tbody')
    try:
        for row in tbody.children:
            if len(row.findAll('td')) < 7:
                print('incorrect row', row)
                continue

            str_date = row.findAll('td')[0].text
            datetime_obj = datetime.strptime(str_date, '%b %d, %Y')

            volume = int(''.join(row.findAll('td')[6].text.split(',')))

            item = {
                "company": company,
                "date": datetime_obj.date(),
                "open": float(row.findAll('td')[1].text),
                "high": float(row.findAll('td')[2].text),
                "low": float(row.findAll('td')[3].text),
                "close": float(row.findAll('td')[4].text),
                "adj_close": float(row.findAll('td')[5].text),
                "volume": volume
            }
            result.append(item)
    except ValueError:
        raise ValueError('Some values are incorrect')

    return result
