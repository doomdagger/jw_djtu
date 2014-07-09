from django.shortcuts import render
from django.shortcuts import render_to_response
from common.models import Announcement


# Create your views here.
def common_browse_announcement(request):
    return render_to_response('common/browse_announcement.html')