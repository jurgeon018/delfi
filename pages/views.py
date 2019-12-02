from pages.models import *
from django.shortcuts import render 




def index(request):
  bus_comments = BusComment.objects.all()
  page = Index.objects.first()
  return render(request, 'index.html', locals())


def park(request):
  buses = Bus.objects.all()
  page = Park.objects.first()
  return render(request, 'park.html', locals())


def about_us(request):
  page = About.objects.first()
  return render(request, 'about_us.html', locals())


def contact_us(request):
  page = Contact.objects.first()
  return render(request, 'contact_us.html', locals())


def blog(request):
  posts = Post.objects.all()
  page = Blog.objects.first()
  return render(request, 'blog.html', locals())


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'post_detail.html', locals())


def thank_you(request):
  return render(request, 'thank_you.html', locals())
