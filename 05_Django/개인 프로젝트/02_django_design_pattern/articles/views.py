from django.shortcuts import render

# Create your views here.
# app 폴더 안에 view.py 안에서 특정 기능을 수행하는 함수 def를 만든다.

def index(request): 
    # index는 보통 메인페이지를 의미한다.
    return render(request, 'index.html')
