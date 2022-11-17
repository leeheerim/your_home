from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def search(request):
    if request.method=='GET':
        config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
        client_id = config_secret_debug['NAVER']['CLIENT_ID']
        client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

        q = request.GET.get('q')
        encText = urllib.parse.quote("주택".format(q))
        url = "https://openapi.naver.com/v1/search/news?query=" + encText  # json 결과
        news_api_request = urllib.request.Request(url)
        news_api_request.add_header("X-Naver-Client-Id",client_id)
        news_api_request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(news_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')

            context = {
                'items': items
            }
        return render(request, 'home.html', context=context)