from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import NewsHeadline
from django.db.models.functions import ExtractYear
from django.db.models import Q
import datetime

def news_page(request):
    # def prime_num(num):
    #     if num == 1:
    #         return "Small Picture"
    #     for i in range(2, num):
    #         if num % i == 0:
    #             return i
    #     return "Long Picture"

    # for num in range(1, 100):
    #     print(num, prime_num(num))
    
    
    d = datetime.datetime.now()
    yearsList = []
    def detectChangeOfYear():
        """
        Detect change of year and save the current year and 
        each year that has passed into a list
        """
        for i in range(2020, 2120):
            previousYear = i
            yearsList.append(i)
            for j in range(2021, 2121):
                newYear = j
                if previousYear == d.year:
                    return yearsList
                elif d.year == newYear and previousYear == d.year - 1:
                    yearsList.append(newYear)
                    return yearsList    
    
    # Call the function 
    detectYear = detectChangeOfYear()
    currentYear = None
    if request.GET:
        if 'selectedNewsYear' in request.GET:
            selectedDate = request.GET['selectedNewsYear']
            theDate = int(selectedDate)
            currentYear = theDate
    else:
        currentYear = yearsList[-1]

    main_news_info = NewsHeadline.objects.all()
    
    # Search Query
    searched = False
    query = None
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "Es wurden keine Suchkriterien eingegeben!")
            return redirect(reverse('main_news_info'))

        queries = Q(heading__icontains=query) | Q(second_heading__icontains=query)
        searched = True
        main_news_info = NewsHeadline.objects.filter(queries)

    context = {
        'main_news_info': main_news_info,
        'search_term': query,
        'searched': searched,
        'yearChanged': detectYear,
        'yearsList': yearsList,
        'currentYear': currentYear
    }
 
    return render(request, 'news/news.html', context)

    # Get the year of when the news got published
    # yearOfPost = NewsHeadline.objects.annotate(year=ExtractYear('time_and_date_published')).filter(year=d.year)
    # yearOfPost = NewsHeadline.objects.all()
    # for postYear in yearOfPost:
    #     published = postYear
    #     # Return main news page content that is from the current year
    #     print(published)


def article_content(request, article_id):
    """ Show individual news article content """
    
    article = get_object_or_404(NewsHeadline, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'news/article-content.html', context)