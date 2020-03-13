import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

class TypeOfTrend:
    def __init__(self):
        self.df = ""

    # Interest by Region
    def interest_by_region(self, kw_list):
        pytrend.build_payload(kw_list=kw_list)
        self.df = pytrend.interest_by_region()

    # Get Google Hot Trends data
    # pn: country name
    def hot_trends(self, pn):
        self.df = pytrend.trending_searches(pn=pn)

    # Get Google Keyword Suggestions
    def gg_keyword_suggestions(self, keyword):
        keywords = pytrend.suggestions(keyword=keyword)
        self.df = pd.DataFrame(keywords)

    # Get Google Hot Trends data
    def gg_today_searches(self, pn):
        self.df = pytrend.today_searches(pn=pn)

    # Get Google Top Charts
    def gg_top_charts(self):
        self.df = pytrend.top_charts(2019, hl='en-US', tz=300, geo='GLOBAL')

    def interest_over_time(self, kw_list):
        pytrend.build_payload(kw_list=kw_list)
        self.df = pytrend.interest_over_time()

    # Related Queries, returns a dictionary of dataframes
    def related_queries(self, kw_list):
        pytrend.build_payload(kw_list=kw_list)
        self.df = pytrend.related_queries()

    # Related Topics, returns a dictionary of dataframes
    def related_topics(self, kw_list):
        if (type(kw_list) is not list):
            kw_list = list(kw_list)
        pytrend.build_payload(kw_list=kw_list)
        self.df = pytrend.related_topics()

    def get_df(self):
        return self.df

    def print_head(self):
        print(self.df.head())

    def print_value(self):
        print(self.df.values())

def transfer_into_csv(data):
    data.to_csv('demo.csv', encoding='utf_8_sig')

def transfer_into_image(data):
    image = data.plot(title='Image')
    fig = image.get_figure()
    fig.savefig('demo.png')


# topic = TypeOfTrend()
# topic.related_topics('Corona')
# topic.print_value()
# type.related_queries(['apple', 'samsung'])
# type.print_value()
# type.transfer_into_csv()
# type.transfer_into_image()