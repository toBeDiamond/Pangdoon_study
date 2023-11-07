from django.shortcuts import render
import numpy as np
import pandas as pd
from django.http import JsonResponse


# 공한 데이터(data/test_data_has_null.CSV)를 Django 에서 읽어오도록 구현합니다
df = pd.read_csv('data/test_data_has_null.CSV', encoding='cp949')

def function_A(request):
    # 공한 데이터(data/test_data.CSV)를 Django 에서 읽어오도록 구현합니다
    df = pd.read_csv('data/test_data.CSV', encoding='cp949')

    # 메모리에 있는 것을 바로 전달할 수 없어서 -> json으로 바꿔서 보내줌
    # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션
    data = df.to_dict('records')

    # JSON 형태로 응답
    return JsonResponse({ 'dat' : data })


def function_B(request):
    # df['직업'].fillna('NULL', inplace=True)
    # df['이름'].fillna('NULL', inplace=True)
    # df['나이'].fillna('NULL', inplace=True)
    # df['성별'].fillna('NULL', inplace=True)
    # df['사는곳'].fillna('NULL', inplace=True)

    df.fillna('NULL', inplace=True)

    # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션
    data = df.to_dict('records')

    return JsonResponse({ 'dat' : data })
    


def function_C(request):
    # 나이 필드의 평균값을 average_age에 담아줌
    average_age = df['나이'].mean()

    abs_age = []

    for i in range(len(df)):
        abs_age.append(abs(df['나이'][i] - average_age))
    
    df['diff'] = abs_age


    # records: 리스트 원소를 각각 하나의 레코드로 만들기 위해 주는 옵션

    new_df = df.sort_values('diff')

    ten_df = new_df.head(10)
    
    data = ten_df.to_dict('records')

    return JsonResponse({ 'dat' : data })
    


