from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jw_djtu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'students.views.student_index'),
    url(r'^signin/', 'students.views.student_signin'),
    url(r'^dosignin/', 'students.views.student_dosignin'),
    url(r'^signout/', 'students.views.student_signout'),
    url(r'^changepass/', 'students.views.student_change_password'),

    url(r'^announcement/', 'common.views.common_browse_announcement'),
    url(r'^api/announcement/', 'common.views.common_api_browse_announcement'),
    url(r'^queryroom/', 'common.views.common_query_room'),
    url(r'^querycourse/', 'students.views.student_query_course'),
    url(r'^queryscore/', 'students.views.student_query_score')

)
