from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Donation
from .forms import DonationForm

def donation_list(request):
    donations = Donation.objects.all()
    print(donations)
    context = {'pagina': 'Doações', 'page_title': 'Doações', 'donations': donations}
    return render(request, 'donation/donation_list.html', context)


def donation_detail(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    context = {'pagina': 'Doações', 'page_title': 'Doações', 'donation': donation}
    return render(request, 'donation/donation_detail.html', context)

def donation_new(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.created_at = timezone.now()
            donation.status = "A"
            donation.save()
            return redirect('donation_detail', pk=donation.pk)
    else:
        form = DonationForm()
        context = {'pagina': 'Doações', 'page_title': 'Despesas', 'form': form}
    return render(request, 'donation/donation_edit.html', context)

def donation_edit(request, pk):
    donation = Donation.objects.get(pk=pk)
    if request.method == "POST":
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.updated_at = timezone.now()
            donation.save()
            return redirect('donation_detail', pk=donation.pk)
    else:
        form = DonationForm(instance=donation)
        context = {'pagina': 'Doações', 'page_title': 'Doações', 'form': form}
    return render(request, 'donation/donation_edit.html', context)

def donation_delete(request, pk):
    donation = Donation.objects.get(pk=pk)
    context = {'pagina': 'Doações', 'page_title': 'Doações'}
    Donation.objects.filter(pk=pk).delete()
    return redirect('donation_list')
