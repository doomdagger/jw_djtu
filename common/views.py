from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models.query import exceptions
from django.template import loader, RequestContext

from common.models import Announcement, Setting
import json

# Create your views here.
def common_service_browse_announcement(request):
    announcements = []

    try:
        week = request.GET['school_week']
    except KeyError:
        week = int(Setting.objects.get(key="school_week").value)

    try:
        raw_announcements = Announcement.objects.filter(start_week__lte=week, end_week__gte=week)

        for raw_announcement in raw_announcements:
            temp_map = {
                "title": raw_announcement.title,
                "content": raw_announcement.content
            }
            announcements.append(temp_map)

    except exceptions.ObjectDoesNotExist:
        pass

    return {
        'announcements': announcements,
        'week': week
    }


def common_api_browse_announcement(request):
    return HttpResponse(json.dumps(common_service_browse_announcement(request)), content_type="application/json")


def common_browse_announcement(request):

    template = loader.get_template('common/browse_announcement.html')
    context = RequestContext(request, common_service_browse_announcement(request))
    return HttpResponse(template.render(context))


def common_query_room(request):
    return render_to_response('common/query_room.html')