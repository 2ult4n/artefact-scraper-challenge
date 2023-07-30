import configparser

class SpiderConfigProvider():

    _spider_config = configparser.ConfigParser()
    _spider_config.read('spider/providers/spider_configs.ini')
 
    xpath_article_url = _spider_config['xpaths_exp']['article_url']
    xpath_paginaition = _spider_config['xpaths_exp']['paginaition']
    xpath_headline = _spider_config['xpaths_exp']['headline']
    xpath_content = _spider_config['xpaths_exp']['content']
    xpath_author = _spider_config['xpaths_exp']['author']
    xpath_publish_date = _spider_config['xpaths_exp']['publish_date']