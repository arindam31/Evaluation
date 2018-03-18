# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect

from . import forms
from .models import Interview, Question, Candidate, Answer

# Create your views here.
def index(request):
    return render(request, 'Evaluator/home.html')

@login_required
def profile(request):
    i = Interview()
    print 'We are inside the profile of ', request.user

    args = {'user': request.user, 'interview_today': i.all_interviews()}
    return render(request, 'profile.html', args)

def question_detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exists!")
    args = {'question': question}
    return render(request, 'question_details.html', args)


def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = forms.RegistrationForm()
        args = {'form': form}
        return render(request, 'register.html', args)

@login_required
def add_candidate(request):
    if request.method == 'POST':
        form = forms.AddCandidateForm(request.POST)
        if form.is_valid():
            print 'Form is valid'
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.contact_primary = form.cleaned_data['contact_primary']
            post.experience = form.cleaned_data['experience']
            post.position_applied = form.cleaned_data['position_applied']
            print 'Saving the form'
            post.save()
            return redirect('/profile')
    else:
        form = forms.AddCandidateForm()
        args = {'form': form}
        return render(request, 'add_candidate.html', args)

@login_required
def search_candidate(request):
    if request.method == 'GET':
        if 'keyword' in request.GET.keys():
            keyword = request.GET['keyword']
            candis = Candidate.objects.filter(name__icontains=keyword)
            if candis:
                return render(request, 'search_candidate.html', {'candidates': candis})
            else:
                return render(request, 'search_candidate.html', {'error_message': 'No candidates matching'})
        else:
            return render(request, 'search_candidate.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = forms.EditProfileForm(instance=request.user)
        args = {'form' : form}
        return render(request, 'edit_profile.html', args)

@login_required
def edit_candidate(request):
    if request.method == 'POST':
        #Do something
        pass


@login_required
def change_password(request):
    if request.method == 'POST':
        form = forms.PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/profile')
        else:
            return redirect('/profile/password')
    else:
        form = forms.PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'password_change.html', args)


def search_question(request):
    pass


class QuestionList(ListView):
    model = Question


def create_question(request):
    answer_forms = forms.AnswerInLineFormSet(
            queryset=Answer.objects.none()
            )
    form = forms.QuestionForm()
    if request.method == 'POST':
        print "Inside POST call of create question"
        form = forms.QuestionForm(request.POST)
        answer_forms = forms.AnswerInLineFormSet(
                request.POST,
                queryset=Answer.objects.none()
                )
        if form.is_valid() and answer_forms.is_valid():
            question = form.save()
            answers = answer_forms.save(commit=False)
            for answer in answers:
                answer.question = question
                answer.save()
            return HttpResponseRedirect(reverse('Evaluator:profile'))
    return render(request, 'create_question.html',
            {
                'form':form,
                'formset':answer_forms
            })
            
            

