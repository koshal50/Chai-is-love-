from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ChaiVarietyForm,Store,ContactForm, ChaiReviewForm
from .models import chaiVariety, CHaiReview
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import SignUpForm
from performer.models import about_description, CHaiReview
from django.db.models import Count

def all_chai(request):
    chais = chaiVariety.objects.all() # retrieves all chai variety models from the database 
    return render(request,'performer/all_chai.html', {'chais': chais})  # passes the retrieved chai varieties to the template for rendering on frontend

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import chaiVariety, CHaiReview
from .forms import ChaiReviewForm

def chai_details(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    reviews = CHaiReview.objects.filter(chai=chai).order_by('-date')
    
    # Check if user already reviewed this chai
    user_review = None
    if request.user.is_authenticated:
        user_review = CHaiReview.objects.filter(chai=chai, user=request.user).first()
    
    if request.method == 'POST' and request.user.is_authenticated:
        # If user already has a review, update it; otherwise create new
        form = ChaiReviewForm(request.POST, instance=user_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.chai = chai
            review.user = request.user
            review.save()
            
            if user_review:
                messages.success(request, 'Review updated successfully! ✅')
            else:
                messages.success(request, 'Review submitted successfully! ✅')
            
            return redirect('chai_details', chai_id=chai_id)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ChaiReviewForm(instance=user_review)
    
    return render(request, 'performer/chai_details.html', {
        'chai': chai,
        'reviews': reviews,
        'form': form,
        'user_review': user_review
    })

def chai_store(request):
    stores = None  # placeholder for future implementation
    if request.method == 'POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chaiVariety = form.cleaned_data['chaiVariety']
            stores = Store.objects.filter(chai_varieties=chaiVariety)
    else:
        form = ChaiVarietyForm()
    return render(request,'performer/chai_store.html',{'stores': stores,'form': form})



def contact(request):
    if(request.method=='POST'):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'contact.html',{'form':ContactForm(),'success':True}   )
    else:
        form=ContactForm()
    return render(request, 'contact.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def about(request): #created a request to later on call the about function 
    blogs = about_description.objects.all().order_by('-id')
    featured = blogs.first() if blogs else None
    other_blogs = blogs[1:7] if blogs.count() > 1 else []
    
    return render(request, "about.html", {
        "featured": featured,
        "blogs": other_blogs
    })

def about_detail(request, pk):
    blog = about_description.objects.get(pk=pk)
    return render(request, "about_detail.html", {"blog": blog})

# # Find duplicate reviews (same chai + user)
# duplicates = (CHaiReview.objects
#     .values('chai', 'user')
#     .annotate(count=Count('id'))
#     .filter(count__gt=1))

# # For each duplicate group, keep the latest and delete older ones
# for dup in duplicates:
#     reviews = CHaiReview.objects.filter(
#         chai_id=dup['chai'], 
#         user_id=dup['user']
#     ).order_by('-date')
    
#     # Keep first (newest), delete rest
#     reviews_to_delete = reviews[1:]
#     for review in reviews_to_delete:
#         review.delete()
    
#     print(f"Cleaned duplicates for chai={dup['chai']}, user={dup['user']}")

# exit()
