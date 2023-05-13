from django.db import transaction

from core.utils.common import temporary_disconnect_all_signals
from organizations.models import Organization, OrganizationMember
from projects.models import Project
from django.contrib.auth.models import Group


def create_organization(title, created_by):
    with transaction.atomic():
        org = Organization.objects.create(title=title, created_by=created_by)
        member=OrganizationMember.objects.create(user=created_by, organization=org, role_id=1)
        membergroup= Group.objects.get(id=1)
        membergroup.user_set.add(member.user)
        return org


def destroy_organization(org):
    with temporary_disconnect_all_signals():
        Project.objects.filter(organization=org).delete()
        if hasattr(org, 'saml'):
            org.saml.delete()
        org.delete()
