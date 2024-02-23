# views.py
from django.shortcuts import render, redirect
from .models import FancyPhoneNumber
from .forms import FancyPhoneNumberForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import AdminLoginForm
from django.urls import reverse_lazy

class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    authentication_form = AdminLoginForm

    def form_valid(self, form):
        # Perform additional validation checks here if needed
        # For example, you can check if the user is an admin
        if form.user_cache.is_superuser:
            return super().form_valid(form)
        else:
            # If user is not an admin, redirect them to a different page
            return redirect('non_admin_page')

    def get_success_url(self):
        return reverse_lazy('fancy_phone_number_list')


def add_fancy_phone_number(request):
    if request.method == 'POST':
        form = FancyPhoneNumberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fancy_phone_number_list')
    else:
        form = FancyPhoneNumberForm()
    return render(request, 'add_fancy_phone_number.html', {'form': form})


def delete_fancy_phone_number(request, number_id):
    number = FancyPhoneNumber.objects.get(pk=number_id)
    number.delete()
    return redirect('fancy_phone_number_list')

def fancy_phone_number_list(request):
    fancy_phone_numbers = FancyPhoneNumber.objects.all()
    context = {
        "fancy_phone_numbers":fancy_phone_numbers,
    }
    return render(request, 'fancy_phone_number_list.html',context)