from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .gpt_utils import analyze_feedback
from .models import Feedback
from dotenv import load_dotenv

import openai
import os
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY


# Create your views here.



def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            
            # Analyze the feedback using GPT
            analysis = analyze_feedback(feedback.message)

            #detect "need attention" in gpt response
            needs_attention= "Needs Attention: Yes" in analysis

            # Save or display the analysis 
            feedback.gpt_review = analysis
            feedback.needs_attention = needs_attention
            feedback.save()
            print("GPT Analysis:", analysis)

            return render(request, 'feedback/thank_you.html', {'analysis': analysis})
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})




def all_feedback_view(request):
    feedback_list= Feedback.objects.all().order_by('-submitted_At')
    return render(request, 'feedback/all_feedback.html', {'feedback_list': feedback_list})