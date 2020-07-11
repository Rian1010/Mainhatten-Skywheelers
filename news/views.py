from django.shortcuts import render, get_object_or_404
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


def article_content(request, article_id):
    """ Show individual news article content """
    
    article = get_object_or_404(NewsHeadlines, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'news/article-content.html', context)