#
# reviewboard/admin/urls.py -- URLs for the admin app
#
# Copyright (c) 2008-2009  Christian Hammond
# Copyright (c) 2009  David Trowbridge
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin

from reviewboard.admin import forms


NEWS_FEED = "http://www.review-board.org/news/feed/"

urlpatterns = patterns('reviewboard.admin.views',
    (r'^$', 'dashboard'),
    (r'^cache/$', 'cache_stats'),

    # Settings
    url(r'^settings/general/$', 'site_settings',
        {'form_class': forms.GeneralSettingsForm,
         'template_name': 'admin/general_settings.html'},
        name="settings-general"),
    url(r'^settings/email/$', 'site_settings',
        {'form_class': forms.EMailSettingsForm,
         'template_name': 'admin/settings.html'},
        name="settings-email"),
    url(r'^settings/diffs/$', 'site_settings',
        {'form_class': forms.DiffSettingsForm,
         'template_name': 'admin/settings.html'},
        name="settings-diffs"),
    url(r'^settings/logging/$', 'site_settings',
        {'form_class': forms.LoggingSettingsForm,
         'template_name': 'admin/settings.html'},
        name="settings-logging"),
    url(r'^settings/storage/$', 'site_settings',
        {'form_class': forms.StorageSettingsForm,
         'template_name': 'admin/storage_settings.html'},
        name="settings-storage"),
)

urlpatterns += patterns('',
    (r'^log/', include('djblets.log.urls')),

    ('^db/(.*)', admin.site.root),
    ('^feed/news/$', 'djblets.feedview.views.view_feed',
     {'template_name': 'admin/feed.html',
      'url': NEWS_FEED}),
    (r'^feed/news/rss/$', 'django.views.generic.simple.redirect_to',
     {'url': NEWS_FEED}),

    url(r'^settings/$', 'django.views.generic.simple.redirect_to',
        {'url': 'general/'},
        name="site-settings"),
)
