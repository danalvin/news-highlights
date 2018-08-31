class News_sources:
    """
    News_sources class to define News_sources Objects
    """
    def __init__(self, source_id, source_name, author, description, url):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.description = description
        self.url = url

class News_articles:
    """
    News_articles class to define News_articles Objects
    """
    def __init__(self, source_id, source_name, author, title, description, urlToImage, url, publishedAt):
        self.source_id = source_id
        self.source_name = source_name
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt