import json
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import BlackOffer, tweets
from datetime import datetime
import nltk
from django.db import models
from django.db.models import Count  # Add this import

from nltk.sentiment import SentimentIntensityAnalyzer
# Create your views here.

def index(request):
    positive = tweets.objects.filter(sentiment='positive').count()
    negative = tweets.objects.filter(sentiment='negative').count()
    neutral = tweets.objects.filter(sentiment='neutral').count()
    all = tweets.objects.all().count()
    positive = round((positive/all)*10000)/100
    negative = round((negative/all)*10000)/100
    neutral = round((neutral/all)*10000)/100
    top_hashtags = tweets.objects.values('hastag').annotate(tweet_count=Count('hastag')).order_by('-tweet_count')[:10]
    top_username = tweets.objects.values('username').annotate(tweet_count=Count('username')).order_by('-tweet_count')[:10]
    print(top_hashtags)
    data = {'positive':positive, 'negative':negative, 'neutral':neutral, 'top_hashtags':top_hashtags, 'top_username':top_username}
    return render(request, 'index.html', data)

def docs(request):
    return render(request, 'docs.html')

def orders(request):
    data = tweets.objects.all().values()
    data = {"data": data}
    return render(request, 'orders.html', data)

def notifications(request):
    return render(request, 'notifications.html')

def account(request):
    return render(request, 'account.html')

def settings(request):
    return render(request, 'settings.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def reset_password(request):
    return render(request, 'reset-password.html')


def error(request):
    return render(request, '404.html')


def charts(request):
    return render(request, 'charts.html')


def help(request):
    return render(request, 'help.html')


def main(request):
    return render(request, 'upload.html')

class UploadJsonView(View):
    def post(self, request, *args, **kwargs):
        try:
            
            uploaded_file = request.FILES['json_file']
            data = json.load(uploaded_file)

            for item in data:
                
                    end_year= item['end_year']
                    if end_year =="":
                        end_year = None
                    intensity=item['intensity']
                    if intensity == "":
                        intensity = None
                    sector=item['sector']
                    topic=item['topic']
                    insight=item['insight']
                    url=item['url']
                    region=item['region']
                    start_year=item['start_year']
                    if start_year=="":
                        start_year = None
                    impact=item['impact']
                    if impact == "":
                        impact = None
                    added=item['added']
                    try:
                        parsed_date = datetime.strptime(added, "%B, %d %Y %H:%M:%S")
                        added = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        added = None
                    published=item['published']
                    try:
                        parsed_date = datetime.strptime(published, "%B, %d %Y %H:%M:%S")
                        published = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
                    except:
                        published = None
                    country=item['country']
                    relevance=item['relevance']
                    if relevance == "":
                        relevance = None
                    pestle=item['pestle']
                    source=item['source']
                    title=item['title']
                    likelihood=item['likelihood']
                    if likelihood == "":
                        likelihood = None

                    BlackOffer.objects.create( end_year=end_year, intensity=intensity,
                                              sector=sector, topic=topic, insight=insight,
                                              url=url, region=region, start_year=start_year,
                                              impact=impact, added=added, published=published,
                                              country=country, relevance=relevance, pestle=pestle,
                                              source=source, title=title, likelihood=likelihood
                )

            return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


class UploadTweet(View):
    def post(self, request, *args, **kwargs):
        try:
            if 'json_file' in request.FILES:
                uploaded_file = request.FILES['json_file']
                data = json.load(uploaded_file)

                for item in data.get('tweets', []):
                    date_str = item.get('date', None)
                    # date_str = item.get('date', None)
                    try:
                        parsed_date = datetime.fromisoformat(date_str)
                        date = parsed_date
                    except (ValueError, TypeError):
                        date = None

                    hashtag = item.get('hashtag', '')
                    username = item.get('username', '')
                    tweet_text = item.get('tweet', '')
                    sentiment = item.get('sentiment', '')

                    tweets.objects.create(
                        date=date,
                        hastag=hashtag,
                        username=username,
                        tweets=tweet_text,
                        sentiment=sentiment
                    )

                return JsonResponse({'message': 'Data uploaded successfully'}, status=200)

            else:
                return JsonResponse({'error': 'No file uploaded'}, status=400)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

def sentiment(request):
    if request.method == "POST":
        data = request.POST.get('text')
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = sid.polarity_scores(data)
        if sentiment_scores['compound'] >= 0.05:
            sentiment_label = 'Positive'
        elif sentiment_scores['compound'] <= -0.05:
            sentiment_label = 'Negative'
        else:
            sentiment_label = 'Neutral'
        
        return render(request, 'sentiment.html', {'sentiment_label':sentiment_label})
    return render(request, 'sentiment.html')