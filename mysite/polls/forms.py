from django import forms
from .models import TrendType

TREND_TYPE = (
    ("interest_by_region", "Interest by Region"),
    ("hot_trends", "Google Hot Trends data"),
    ("gg_keyword_suggestions", "Google Keyword Suggestions"),
    ("gg_today_searches", "Google Hot Trends today search"),
    ("gg_top_charts", "Google Top Charts"),
    ("related_queries", "Related Queries"),
    ("related_topics", "Related Topics"),
    ("interest_over_time", "Interest over Time"),
)


class PostForm(forms.Form):
   GG_Trend_Type = forms.ChoiceField(choices=TREND_TYPE)
   Keyword_List = forms.CharField(max_length=100)
   Keyword = forms.CharField(max_length=100)