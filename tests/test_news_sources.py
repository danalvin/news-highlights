
import unittest
from app.models import News_sources

class News_sources_Test(unittest.Testcase):
    """
    Test Class to test the behaviour of the News_sources class
    """
    def setup(self):
        '''
        Set up method that will run before every Test
        '''
        self.news_sources = News_sources('the-new-york-times', 'The New York Times', 'Charles V. Bagli and Jesse Drucker', 'Vornado Realty Trust\u2019s chairman said it had agreed to sell its part of the financially troubled building to the Kushners.', 'www.nytimes.com/2018/04/06/nyregion/kushners-vornado-666-fifth-avenue.html')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, News_source))
    

if __name__ == '__main__':
    unittest.main()