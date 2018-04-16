from urllib.request import urlopen
from bs4 import BeautifulSoup


url_atlassian = 'https://www.atlassian.com/'
url_devops = 'https://devops.com/'
url_nginx = 'https://www.nginx.com/'
file_path = 'html/atlassian.html'


class AtlasLink:
    __url = ''
    __data = ''
    __web_log = None
    __soup = None


    def __init__(self, url, web_log):
        self.__url = url
        self.__web_log = web_log


    def rake_up_webpage(self):
        try:
            html = urlopen(self.__url)
        except Exception as e:
            self.__web_log.report(e)
        else:
            self.__data = html.read()
            if len(self.__data) > 0:
                print("Raked Up Successful")


    def write_webpage_html_format(self, filepath=file_path, data=''):
        try:
            with open(filepath, 'wb') as file_object:
                if data:
                    file_object.write(self.__data)
        except Exception as e:
            self.__web_log.report(str(e))


    def read_webpage_from_html(self, filepath=file_path, data=''):
        try:
            with open(filepath) as file_object:
                self.__data = file_object.read()
        except Exception as e:
            self.__web_log.report(str(e))


    def data_convert_to_bs4(self):
        self.__soup = BeautifulSoup(self.__data, 'html.parser')


    def pare_simple_html(self):
        info_lists = self.__soup.find_all(['h1', 'h2', 'h3', 'h4'])

        htmltext = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>News Link Scrapper</title>
        </head>
        <body>
        {NEWS_LINKS}
        </body>
        </html>
        '''

        links_info = '<ol>'

        for tag in info_lists:
            if tag.parent.get('href'):
                link = self.__url + tag.parent.get('href')
                title = tag.string
                links_info += "<li><a href='{}' target='_blank'>{}</li>\n".format(link, title)
        links_info += '</ol>'

        htmltext = htmltext.format(NEWS_LINKS=links_info)
        self.write_webpage_html_format(filepath='html/sample.html', data=htmltext.encode())



    