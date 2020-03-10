import string

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .SendSlack import send_file_to_slack
from .forms import PostForm
from .TypeOfTrends import TypeOfTrend, transfer_into_image, transfer_into_csv
import re


# Create your views here.

def index(request):
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'abc': 'abc'
    # }
    # return HttpResponse(template.render(context, request))
    context = {}
    context['form'] = PostForm()

    if request.GET:
        response = HttpResponse()
        trend = request.GET['GG_Trend_Type']
        kw = request.GET['Keyword_List']

        SEP = (',', ';')
        rsplit = re.compile("|".join(SEP)).split
        kw_list = [s.strip() for s in rsplit(kw)]

        type = TypeOfTrend()
        func_map = {'interest_by_region': type.interest_by_region,
                    'gg_today_searches': type.gg_today_searches,
                    'hot_trends': type.hot_trends,
                    'gg_keyword_suggestions': type.gg_keyword_suggestions,
                    'gg_top_charts': type.gg_top_charts,
                    'related_queries': type.related_queries,
                    'related_topics': type.related_topics,
                    }
        func_map[trend](kw_list)
        data = type.get_df()

        if (trend == 'related_queries') or (trend == 'related_topics'):
            response.write(type.print_value())
        else:
            response.write(type.print_head())

        if (data != string.empty):
            transfer_into_image(data)
            transfer_into_csv(data)
            send_file_to_slack('demo.png')

        return response

    return render(request, 'polls/index.html', context)

