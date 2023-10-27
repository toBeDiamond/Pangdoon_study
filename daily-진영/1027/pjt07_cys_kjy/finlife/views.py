from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

@api_view(['GET'])      # 정기예금 상품 목록과 옵션 목록을 DB에 저장
def save_deposit_products(request):
    # API KEY
    api_key = settings.API_KEY
    # 옵션
    responseType = 'json'
    bank = '020000'
    pageNum = 1
    serviceName = 'depositProductsSearch'
    # URL
    url = f'http://finlife.fss.or.kr//finlifeapi/{serviceName}.{responseType}?auth={api_key}&topFinGrpNo={bank}&pageNo={pageNum}'
    # 상품 목록 정보 받기 = response
    deposit_products_list = requests.get(url).json()
    products_list = deposit_products_list.get('result')
    for li in products_list.get('baseList'):
        if DepositProducts.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            continue

        save_data = {
            'fin_prdt_cd':li.get('fin_prdt_cd'),
            'kor_co_nm':li.get('kor_co_nm'),
            'fin_prdt_nm':li.get('fin_prdt_nm'), 
            'etc_note':li.get('etc_note'),
            'join_deny':li.get('join_deny'),
            'join_member':li.get('join_member'), 
            'join_way':li.get('join_way'),
            'spcl_cnd':li.get('spcl_cnd'),
        }
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

    for li in products_list.get('optionList'):
        dpl = DepositProducts.objects.get(fin_prdt_cd = li.get('fin_prdt_cd'))
        save_data = {
            'fin_prdt_cd' : li.get('fin_prdt_cd'),
            'intr_rate_type_nm' : li.get('intr_rate_type_nm') ,
            'intr_rate' : li.get('intr_rate') if li.get('intr_rate') else 0,
            'intr_rate2' : li.get('intr_rate2') if li.get('intr_rate') else 0,
            'save_trm' : li.get('save_trm'),	
        }
        serializer2 = DepositOptionsSerializer(data=save_data)
        if serializer2.is_valid(raise_exception=True):
            serializer2.save(product=dpl)
    return JsonResponse({'msg':'success'})
    


@api_view(['GET','POST'])       # GET : 전체정기예금상품 목록반환 , POST: 상품데이터 저장
def deposit_products(request):
    if request.method == 'GET':
        all_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(instance=all_products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        pass


@api_view(['GET'])          # 특정상품의 옵션리스트 반환
def deposit_product_options(request, fin_prdt_cd):
    pass



@api_view(['GET'])      # 금리가 가장높은 상품과 해당 옵션리스트를 반환
def top_rate(request):
    pass




