"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.middleware import enforce_csrf_checks
from organizations.models import InvitedPeople
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response

@login_required
def organization_people_list(request):
    return render(request, 'organizations/people_list.html')

@login_required
def simple_view(request):
    return render(request, 'organizations/people_list.html')

