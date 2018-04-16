#---------------------Web Scraping ---------------
from WebScraping import WebLog
from WebScraping import LeadingHere


WebLog.custom_info('html/error.log')

"""
try:
    raise Exception
except Exception as e:
    WebLog.report(e)
"""

atlassian = LeadingHere.AtlasLink(LeadingHere.url_atlassian, WebLog)

atlassian.rake_up_webpage()
atlassian.write_webpage_html_format()
atlassian.read_webpage_from_html()
atlassian.pare_simple_html()
