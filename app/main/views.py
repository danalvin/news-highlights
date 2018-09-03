from flask import render_template, request, redirect, url_for
from .import main
from ..request import get_News_sources,get_News_articles

@main.route('/')
def index():
    '''
    View root page function that returns index page and the various news sources
    '''

    title = 'Welcome to the most Realistic News source page'

    # Getting news sources
    news_sources = get_News_sources('sources')
    return render_template('index.html', title = title, news_sources = news_sources)


@main.route('/articles/<source_id>')
def source(source_id):
    '''
    View for top story articles
    '''
    source_and_articles = get_News_articles(source_id)
    #for source in source_and_articles:
    #     print(source.urlToImage)
    return render_template('articles.html',source_and_articles = source_and_articles)
