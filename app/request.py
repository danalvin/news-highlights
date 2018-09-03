import urllib.request, json
from .models import News_sources, News_articles

# Getting api key
api_key = '16fa6a565fc14afe8bef13b530dc2e47'
# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    # api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_News_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    # get_sources_url = base_url.format(sources, api_key)

    get_sources_url = 'https://newsapi.org/v2/top-headlines?{}=techcrunch&apiKey=16fa6a565fc14afe8bef13b530dc2e47'

    the_url = get_sources_url.format(sources)
    print(the_url)
    with urllib.request.urlopen(the_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        News_sources_results = None

        if get_sources_response['articles']:
            sources_results_list = get_sources_response['articles']
            News_sources_results = process_sources(sources_results_list)

    return News_sources_results


def process_sources(source_list):
    '''
    Function  that processes the News_sources_results and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain news sources details
    Returns :
        News_sources_results: A list of news sources objects
    '''
    News_sources_results = []
    for source_item in source_list:
        source_id = source_item.get('id')
        title = source_item.get('title')
        author = source_item.get('author')
        description = source_item.get('description')
        url = source_item.get('url')


        source_object = News_sources(source_id, title, author, description, url)
        News_sources_results.append(source_object)

    return News_sources_results

def get_News_articles(source):
    get_News_articles_details_url = base_url.format(
        "everything", api_key) + "&sources=" + source
    print(get_News_articles_details_url)
    with urllib.request.urlopen(get_News_articles_details_url) as url:
        News_articles_details_data = url.read()
        News_articles_details_response = json.loads(News_articles_details_data)

        News_articles_results = None

        if News_articles_details_response['articles']:
            News_articles_results_list = News_articles_details_response['articles']
            News_articles_results = process_articles(News_articles_results_list)

    return News_articles_results


def process_articles(News_articles_list):
    '''
    Function that process the News_articles_list and transforms them into a list of objects
    '''
    '''
    Args: News_articles_results_list: A list of dictionaries that contains news articles and links
    '''

    News_articles_results = []
    for article_item in News_articles_list:
        source_id = article_item.get('id')
        source_name = article_item.get('name')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        urlToImage = article_item.get('urlToImage')
        url = article_item.get('url')
        publishedAt = article_item.get('publishedAt')
        if urlToImage:
            article_object = News_articles(source_id, source_name, author, title, description, urlToImage, url, publishedAt)
            News_articles_results.append(article_object)

    return News_articles_results