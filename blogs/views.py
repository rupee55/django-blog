from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from requests import post
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Logic to fetch blogs by category_name
    
    # return render(request, 'blogs_by_category.html', context)
    posts = Blog.objects.filter(category__id=category_id, status='Published').order_by('created_at')
    # try:
    #     category = Category.objects.get(id=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, id=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    
    return render(request, 'posts_by_category.html', context)