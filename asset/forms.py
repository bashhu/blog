# coding=utf-8
"""

__created__ = '5/26/16'
__author__ = 'deling.ma'
"""
from django import forms
#from admin.plugins.multiselect import SelectMultipleTransfer

from asset.models import ServiceGroup, Machine


class MachineForm(forms.ModelForm):
    s_group = forms.ModelMultipleChoiceField(
    queryset=ServiceGroup.objects.all(),
        #idget=SelectMultipleTransfer('s_group',is_stacked=False),
        required=False, label="业务服务组")

    def __init__(self, *args, **kwargs):
        super(MachineForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['s_group'].initial = self.instance.s_group.all()

    class Meta:
        model = Machine
        exclude = []

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, commit)

        def save_m2m():
            groups = [s for s in self.cleaned_data['s_group']]
            for t in instance.s_group.all():
                if t not in groups:
                    instance.s_group.remove(t)
                else:
                    pass
                    # users.remove(t)
            for group in groups:
                instance.s_group.add(group)
        self.save_m2m = save_m2m
        return instance
