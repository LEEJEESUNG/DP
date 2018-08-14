from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from web.models import Node

import urllib
import json

## トップページ

def index(request):

    ## Rest APIへのリクエスト
    opener = urllib.request.build_opener()
    urlreq = urllib.request.Request('http://127.0.0.1:8080/api/nodes')

    ## リクエストに対するレスポンス (jsonで返ってくる)
    data = opener.open(urlreq).read()

    ## jsonデータ構造の読み込み
    json_data = json.loads(data)

    ## 画面表示
    return render(request, 'web/node_list.html', {"nodes" : json_data})


def testa(request):
    res = Node.objects.all()
    return HttpResponse(res)

