from django.shortcuts import render, get_object_or_404
from .models import NewsHeadline
from django.db.models.functions import ExtractYear
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
    def detectChangeOfYear(years, currentYearList):
        """
        Detect change of year and save the current year and 
        each year that has passed in a list
        """
        yearChanged = False
        for i in range(len(years)):
            j = i
            for j in range(i + 1, len(years) - 1):
                if years[i] == d.year:
                    currentYearList.append(years[i])
                    return yearChanged
                elif d.year == years[j]:
                    yearChanged = True
                    currentYearList.append(years[j])
                    i += 1
                    j += 1
                    return yearChanged    
    # Put all available years into a list
    allYears = []
    for aYear in range(2020, 2320):
        allYears.append(aYear)

    # Call the function 
    detectYear = detectChangeOfYear(allYears, yearsList)
        
    main_news_info = NewsHeadline.objects.all()
    currentYear = None
    if request.GET:
        if 'selectedNewsYear' in request.GET:
            selectedDate = request.GET['selectedNewsYear']
            theDate = int(selectedDate)
            currentYear = theDate
    else:
        currentYear = yearsList[-1]
    print(currentYear)

    context = {
        'main_news_info': main_news_info,
        'yearChanged': detectYear,
        'yearsList': yearsList,
        'currentYear': currentYear
    }
    # Get the year of when the news got published
    # yearOfPost = NewsHeadline.objects.annotate(year=ExtractYear('time_and_date_published')).filter(year=d.year)
    # yearOfPost = NewsHeadline.objects.all()
    # for postYear in yearOfPost:
    #     published = postYear
    #     # Return main news page content that is from the current year
    #     print(published)
    return render(request, 'news/news.html', context)


def article_content(request, article_id):
    """ Show individual news article content """
    
    article = get_object_or_404(NewsHeadline, pk=article_id)

    context = {
        'article': article
    }

    return render(request, 'news/article-content.html', context)