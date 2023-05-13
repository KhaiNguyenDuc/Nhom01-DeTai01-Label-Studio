"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""

from django import forms
from .models import Organization, OrganizationMember, InvitedPeople
from django.contrib.auth.models import Group


from django.forms import Textarea, ModelForm, TextInput, Form, FileField, Select, HiddenInput, CharField


class OrganizationForm(ModelForm):
    """
    """
    org_update = CharField(widget=HiddenInput(), required=False)
    
    class Meta:
        model = Organization
        fields = ('title',)


class OrganizationSignupForm(ModelForm):
    """
    """
    class Meta:
        model = Organization
        fields = ('title',)

EMAIL_MAX_LENGTH = 256
PASS_MAX_LENGTH = 64
PASS_MIN_LENGTH = 8
USERNAME_MAX_LENGTH = 30
DISPLAY_NAME_LENGTH = 100
USERNAME_LENGTH_ERR = 'Please enter a username 30 characters or fewer in length'
DISPLAY_NAME_LENGTH_ERR = 'Please enter a display name 100 characters or fewer in length'
PASS_LENGTH_ERR = 'Please enter a password 8-12 characters in length'
INVALID_USER_ERROR = 'The email and password you entered don\'t match.'
EXISTED_PERSON = 'This person has been invited to your organization'

class AddPeopleForm(forms.Form):
    """ For logging in to the app and all - session based
    """

    email = forms.EmailField(label="Email", error_messages={'required': 'Invalid email'})
    role = forms.ModelChoiceField(queryset=Group.objects.all()) 
    organization_id = forms.IntegerField()

    def clean_email(self, *args, **kwargs):
        cleaned = super(AddPeopleForm, self).clean()
        email = cleaned.get('email', '').lower()

        if len(email) >= EMAIL_MAX_LENGTH:
            raise forms.ValidationError('Email is too long')

        # advanced way for user auth
        member = InvitedPeople.objects.get(email=email)

        if member:
            raise forms.ValidationError(EXISTED_PERSON)
        else:
            return email

    def save(self):
        cleaned = self.cleaned_data
        email = cleaned['email'].lower()
        role= self.role
        member = InvitedPeople(email=email, role=role)
        return member


