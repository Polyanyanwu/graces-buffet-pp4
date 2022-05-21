""" System Admin Tables Maintenance View """

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from .forms import SystemPreferenceForm
from .models import SystemPreference


class SystemPreferenceView(View):

    def get(self, request, *args, **kwargs):
        """Display all system preference records and an update form"""
        syspref = SystemPreference.objects.all()
        selected_item = syspref[0].code
        form = SystemPreferenceForm(instance=syspref[0])
        return render(
            request,
            "general_tables/sys_pref/system_pref.html",
            {
                "form": form,
                "syspref": syspref,
                "pref_code": selected_item
            }
        )

    def post(self, request, *args, **kwargs):
        """ Update selected system preference record """
        if 'save_system_preference' in request.POST:
            selected_item = request.POST.get('pref_code')
            pref_form = get_object_or_404(SystemPreference, code=selected_item)
            data = int(request.POST.get('data'))
            pref_form.data = data
            pref_form.save()
            messages.add_message(request, messages.INFO,
                                 'Data updated successfully')
            syspref = SystemPreference.objects.all()
            form = SystemPreferenceForm(instance=syspref[0])
            selected_item = syspref[0].code
        else:
            selected_item = request.POST.get('pref_code')
            syspref = SystemPreference.objects.all()
            curr = None
            try:
                curr = SystemPreference.objects.get(code=selected_item)
            except SystemPreference.DoesNotExist as exception:
                print(exception)
            if curr:
                form = SystemPreferenceForm(instance=curr)
            else:
                form = SystemPreferenceForm(instance=syspref[0])

        return render(
            request,
            "general_tables/sys_pref/system_pref.html",
            {
                "form": form,
                "syspref": syspref,
                "pref_code": selected_item
            }
        )
