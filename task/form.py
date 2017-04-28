#coding:utf-8
from django import forms

class TaskForm(forms.Form):
    host = forms.CharField()
    salt_mod = forms.CharField()
    salt_parm = forms.CharField()

class CommandForm(forms.Form) :
    '''记录执行记录和结果'''
    salt_parm = forms.CharField()
    salt_reason = forms.CharField()#执行原因

