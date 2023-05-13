"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.urls import include, path

from organizations import api, views

app_name = 'organizations'

# TODO: there should be only one patterns list based on API (with api/ prefix removed)
# Page URLs
_urlpatterns = [
    # get organization page
    path('', views.organization_people_list, name='organization-index'),
]

# API URLs
_api_urlpattens = [
    # organization list viewset
    path('', api.OrganizationListAPI.as_view(), name='organization-list'),
    # organization detail viewset
    path('<int:pk>', api.OrganizationAPI.as_view(), name='organization-detail'),
    # organization memberships list viewset
    path('<int:pk>/memberships', api.OrganizationMemberListAPI.as_view(), name='organization-memberships-list'),

    # organization invited member viewset
    path('<int:pk>/invitedmembers', api.OrganizationInvitedMemberListAPI.as_view(), name='organization-memberships-list'),

    # role view set
    path('listrole', api.GetRoleAddPermission.as_view(), name='role-base add permission'),
    path('addperson', api.AddPeopleAPI.as_view(), name="add person to organization"),
    path('detectrole', api.DetectRole.as_view(), name="detect role of logged in person"),
]

# TODO: these urlpatterns should be moved in core/urls with include('organizations.urls')
urlpatterns = [
    path('organization/', views.simple_view, name='organization-simple'),
    path('organization/webhooks', views.simple_view, name='organization-simple-webhooks'),

    path('people/', include(_urlpatterns)),
    path('api/organizations/', include((_api_urlpattens, app_name), namespace='api')),

    # invite
    path('api/invite', api.OrganizationInviteAPI.as_view(), name='organization-invite'),
    path('api/invite/reset-token', api.OrganizationResetTokenAPI.as_view(), name='organization-reset-token'),
]
