# Local URL handler for hostinfo
#
# Written by Dougal Scott <dougal.scott@gmail.com>
#
#    Copyright (C) 2014 Dougal Scott
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url
from .views import index, doHostlist, doHost, doKeylist, handlePost
from .edits import (
    doHostMerge, doHostMergeChoose, doHostRenameChoose, doHostEditChoose,
    doHostCreateChoose, doHostEdit, doHostCreate, doHostRename
)


urlpatterns = patterns(
    'host.views',
    url(r'^$', index, name='index'),
    url(r'^handlePost/$', handlePost, name='formhandler'),

    url(r'^hostedit/$', doHostEditChoose, name='hostEditChoose'),
    url(r'^hostedit/(?P<hostname>\S+)/$', doHostEdit, name='hostEdit'),

    url(r'^hostcreate/$', doHostCreateChoose, name='hostCreateChoose'),
    url(r'^hostcreate/(?P<hostname>\S+)/$', doHostCreate, name='hostCreate'),

    url(r'^hostmerge/$', doHostMergeChoose, name='hostMergeChoose'),
    url(r'^hostmerge/(?P<srchost>\S+)/(?P<dsthost>\S+)$', doHostMerge, name='hostMerge'),

    url(r'^hostrename/$', doHostRenameChoose, name='hostRenameChoose'),
    url(r'^hostrename/(?P<srchost>\S+)/(?P<dsthost>\S+)$', doHostRename, name='hostRename'),

    (r'^hostlist/(?P<criturl>.*)/(?P<options>opts=.*)?$', 'doHostlist'),
    url(r'^hostlist/$', doHostlist, name='hostlist'),
    (r'^hostcmp/(?P<criturl>.*)/(?P<options>opts=.*)?$', 'doHostcmp'),
    (r'^hostcmp/$', 'doHostcmp'),
    url(r'^host/(?P<hostname>\S+)/$', doHost, name='host'),
    url(r'^host/$', doHostlist),
    (r'^host_summary/(?P<hostname>.*)$', 'doHostSummary'),
    (r'^csv/$', 'doCsvreport'),
    (r'^csv/(?P<criturl>.*)/$', 'doCsvreport'),
    url(r'^keylist/(?P<key>\S+)/$', doKeylist, name='keylist'),
    (r'^rvlist/(?P<key>\S+)/$', 'doRestrValList'),
)

# EOF
