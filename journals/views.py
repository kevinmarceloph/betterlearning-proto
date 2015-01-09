from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .forms import JournalForm, EntryForm
from .models import Journal, Entry


@login_required
def view_home(request):
    return redirect(view_profile, username=request.user.username)


@login_required
def view_profile(request, username):
    context = {
        'user': get_object_or_404(User, username=username),
    }

    return render(request, 'view_profile.html', context)


@login_required
def view_journal(request, username, slug):
    context = {
        'journal': get_object_or_404(Journal, user__username=username, slug=slug),
    }

    return render(request, 'view_journal.html', context)


@login_required
def add_edit_journal(request, slug=None):
    journal = get_object_or_404(Journal, user=request.user, slug=slug) if slug else None

    if request.method == 'POST':
        form = JournalForm(request.POST, request.FILES, instance=journal)
        if form.is_valid():
            journal = form.save(user=request.user)

            return redirect(view_journal, username=request.user.username, slug=journal.slug)
    else:
        form = JournalForm(instance=journal)

    context = {
        'form': form,
        'journal': journal,
    }

    return render(request, 'add_edit_journal.html', context)


@login_required
def view_entry(request, username, slug, id):
    context = {
        'entry': get_object_or_404(Entry, journal__user__username=username, journal__slug=slug, id=id),
    }

    return render(request, 'view_entry.html', context)


@login_required
def add_edit_entry(request, slug, id=None):
    journal = get_object_or_404(Journal, user=request.user, slug=slug)
    entry = get_object_or_404(Entry, journal=journal, id=id) if id else None

    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES, instance=entry)
        if form.is_valid():
            entry = form.save(journal=journal)

            return redirect(view_entry, username=request.user.username, slug=journal.slug, id=entry.id)
    else:
        form = EntryForm(instance=entry)

    context = {
        'form': form,
        'entry': entry,
    }

    return render(request, 'add_edit_entry.html', context)
