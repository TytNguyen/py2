import string

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .SendSlack import send_file_to_slack, send_message_to_slack
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

        if (trend == 'hot_trends') or (trend == 'gg_today_searches') or (trend == 'gg_top_charts'):
            kw_list = kw
        else:
            SEP = (',', ';')
            rsplit = re.compile("|".join(SEP)).split
            kw_list = [s.strip() for s in rsplit(kw)]

        topic = TypeOfTrend()
        func_map = {'interest_by_region': topic.interest_by_region,
                    'gg_today_searches': topic.gg_today_searches,
                    'hot_trends': topic.hot_trends,
                    'gg_keyword_suggestions': topic.gg_keyword_suggestions,
                    'gg_top_charts': topic.gg_top_charts,
                    'related_queries': topic.related_queries,
                    'related_topics': topic.related_topics,
                    }
        func_map[trend](kw_list)
        data = topic.get_df()


        if (trend == 'related_queries') or (trend == 'related_topics'):
            response.write(topic.print_value())
        else:
            response.write(topic.print_head())

        if (trend == 'interest_by_region') or (trend == 'interest_over_time'):
            transfer_into_image(data)
            transfer_into_csv(data)
            send_file_to_slack('demo.png')
            send_file_to_slack('demo.csv')
        elif (trend == 'related_queries') or (trend == 'related_topics'):
            send_message_to_slack(topic.get_value())
        else:
            transfer_into_csv(data)
            send_file_to_slack('demo.csv')

        return response

    return render(request, 'polls/index.html', context)

