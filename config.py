import os

class Config:
    """docstring for .
    """
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=16fa6a565fc14afe8bef13b530dc2e47'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    """
    docstring for .
    """
    pass
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg

class DevConfig(Config):
    """docstring for .
    """

    DEBUG = True
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}