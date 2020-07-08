from django.shortcuts import render
from .models import NewsHeadlines

# Create your views here.

def news_page(request):
    """ Return Main News Page """
    main_news_info = NewsHeadlines.objects.all()
    def prime_num(num):
        if num == 1:
            return "Small Picture"
        for i in range(2, num):
            if num % i == 0:
                return i
        return "Long Picture"

    for num in range(1, 100):
        print(num, prime_num(num))

    context = {
        'news_info': main_news_info
    }
        
    return render(request, 'news/news.html', context)
