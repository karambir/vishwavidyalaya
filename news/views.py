from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView

from news.models import News

class NewsListView(ListView):
    context_object_name = 'news_list'
    template_name = 'news_list.html'
    model = News

class NewsDetailView(DetailView):
    context_object_name = 'news'
    model = News
    template_name = 'news_detail.html'
