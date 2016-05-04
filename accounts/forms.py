#!/usr/bin/env python
#-*-coding:utf-8-*-
#
#File Name: ".expand("%"))
#Copyright(c) 2015-2024 Beijing Carryon.top Corp.
#
#Author LiuBin on:" Wed Apr 27 22:57:04 CST 2016
#
#@desc:
#
#@history
#

from django import forms
from django.utils.translation import ugettext_lazy as _
from accounts.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField( 
        label=_('username'),
        required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    quantity = forms.DecimalField(
        label=_('quantity'), 
        min_value=0, 
        required=True, 
        widget=forms.NumberInput(attrs = {'size':2, 'class':'form-control','step':0.01, 'maxlength':5,'placeholder':_('quantity')}), 
        error_messages={'invalid':_('Please enter a valid quantity.')}
    )
    price = forms.DecimalField(
        label=_('price'), 
        min_value=0, 
        required=False, 
        widget=forms.NumberInput(attrs = {'size':2, 'class':'form-control','step':0.01, 'maxlength':5, 'placeholder':_('price')}), 
        error_messages={'invalid':_('Please enter a valid price.')}
    )
    sum_price = forms.DecimalField(
        label=_('sum_price'), 
        min_value=0, 
        required=True, 
        widget=forms.NumberInput(attrs = {'size':2, 'class':'form-control','step':0.01, 'maxlength':9,'placeholder': '小计'}), 
        error_messages={'invalid':_('Please enter a valid price')}
    )
    description = forms.CharField(
        label=_('description'), 
        label_suffix=':', 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('description')}), 
        help_text=_('help text')
    )
    class Meta:
        model = User
        fields = ['username', 'password',]
        exclude = ['data_joined',]

    #override the default __init__ so we can set the request
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(UserForm, self).__init__(*args, **kwargs)

    # custom validation to check for cookies
    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError(_('Cookies must be enabled.'))
        super(UserForm, self).clear()
        return self.cleaned_data


