from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
plt.switch_backend('Agg')
csv_path = 'weathers/data/austin_weather.csv'

# Create your views here.

def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, "problem1.html", context) 

def problem2(request):
    df = pd.read_csv(csv_path)
    x = pd.to_datetime(df['Date'])
    y1 = df['TempHighF']
    y2 = df['TempAvgF']
    y3 = df['TempLowF']
    
    plt.figure(figsize=(10,6))
    
    # 다른 View 함수에서 plt 를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()
    
    plt.plot(x, y1, label='High Temperature')
    plt.plot(x, y2, label='Average Temperature')
    plt.plot(x, y3, label='Low Temperature')

    plt.title('Temperature Variation')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.xlabel('Date')

    # 범례 표시
    plt.legend(loc='lower center')

    # 격자 그리기
    plt.grid(True)
    
    plt.savefig('firstgraph.png')
    
    buffer = BytesIO()
    
    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    
    buffer.close()
    
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "problem2.html", context)

def problem3(request):
    df = pd.read_csv(csv_path,usecols=['Date', 'TempHighF', 'TempAvgF', 'TempLowF'])
    df['Date'] = pd.to_datetime(df['Date'])
    df_average = df.groupby(df['Date'].dt.strftime('%Y/%m')).mean()
    x = df_average['Date']
    y1 = df_average['TempHighF']
    y2 = df_average['TempAvgF']
    y3 = df_average['TempLowF']
    
    plt.figure(figsize=(10,6))
    
    # 다른 View 함수에서 plt 를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()
    
    plt.plot(x, y1, label='High Temperature')
    plt.plot(x, y2, label='Average Temperature')
    plt.plot(x, y3, label='Low Temperature')

    plt.title('Temperature Variation')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.xlabel('Date')

    # 범례 표시
    plt.legend(loc='lower center')

    # 격자 그리기
    plt.grid(True)
    
    plt.savefig('firstgraph.png')
    
    buffer = BytesIO()
    
    plt.savefig(buffer, format='png')
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    
    buffer.close()
    
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, "problem3.html", context)