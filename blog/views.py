from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms import inlineformset_factory, modelformset_factory
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail, BadHeaderError
import datetime


from .models import Image, Album
from .forms import *
from .filters import ImageFilter
from next_prev import next_in_order, prev_in_order
# Create your views here.

def home(request):
    images = Image.objects.filter(id__in = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    image1 = Image.objects.first()
    image2 = next_in_order(image1, qs=images)
    image3 = next_in_order(image2, qs=images)
    image4 = next_in_order(image3, qs=images)
    image5 = next_in_order(image4, qs=images)
    image6 = next_in_order(image5, qs=images)
    image7 = next_in_order(image6, qs=images)
    image8 = next_in_order(image7, qs=images)
    image9 = next_in_order(image8, qs=images)
    image10 = next_in_order(image9, qs=images)

    context = {'image1':image1, 'image2':image2, 'image3':image3,
               'image4': image4, 'image5': image5, 'image6': image6,
               'image7': image7, 'image8': image8, 'image9':image9,
               'image10':image10,
               }

    return render(request, 'blog/index.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print('logged in!')
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is Incorrect.')

    context={}
    return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def image_upload_view(request):
    user = request.user
    image_count = int(Image.objects.all().count() + 1)
    print(image_count)
    albums = Album.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, user=user)
        if form.is_valid():
            form.user = user
            form.save(commit=True)
            img_obj = form.instance
            messages.success(request, 'Successfully uploaded.')
            return render(request, 'blog/upload-image.html', {'form': form, 'img_obj': img_obj, 'image_count':image_count, 'albums':albums})
        else:
            messages.info(request, 'Something went wrong. Double check and try again.')
    else:
        form = ImageForm(user=user)
    return render(request, 'blog/upload-image.html', {'form': form, 'image_count':image_count})

@login_required(login_url='login')
def edit_image(request, pk):
    image = Image.objects.get(id=pk)
    img_obj = image.image
    form = EditImageForm(request.POST, request.FILES, instance=image)
    if request.method == 'POST':
        form = EditImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image.created_at = datetime.datetime.now()
            form.save()
            messages.success(request, 'Successfully updated.')
        else:
            messages.info(request, 'Something went wrong. Double check correct ID and info then try again.')
    else:
        form = EditImageForm(instance=image)
    context = {'form':form, 'img_obj':img_obj, 'image':image}
    return render(request, 'blog/edit.html', context)

@login_required(login_url='login')
def delete_image(request, pk):
    image = Image.objects.get(id=pk)
    essential = range(1, 11)
    if request.method == "POST" and pk not in essential:
        image.delete()
        return redirect('/')
    else:
        messages.info(request, 'Something went wrong. Pictures with ID 1 to 10 can only be edited, not deleted.')
    context = {'image':image, 'essential':essential}
    return render(request, 'blog/delete.html', context)

@login_required(login_url='login')
def image_view(request, pk):
    image = Image.objects.get(id=pk)
    img_obj = image.image
    context = {'image':image, 'img_obj':img_obj}
    return render(request, 'blog/view.html', context)

def about_us(request):
    context = {}
    return render(request, 'blog/about.html', context)

def view_all(request):
    images = Image.objects.all()
    myFilter = ImageFilter(request.GET, queryset=images)
    images = myFilter.qs

    context = {
        'images': images,
        'filter': myFilter,
    }
    return render(request, 'blog/grid.html', context)

def view_big(request):
    images = Image.objects.all()
    myFilter = ImageFilter(request.GET, queryset=images)
    images = myFilter.qs

    context = {
        'images': images,
        'filter': myFilter,
    }
    return render(request, 'blog/big-view.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Inquiry Message from MarenPhoto"
            body = {
                'name': 'From: ' + form.cleaned_data['name'] + "\n",
                'email': 'Sender email: ' + form.cleaned_data['email'] + "\n",
                'message': 'Message: ' + "\n"+ form.cleaned_data['message'] + "\n" + "\n"
                           + '---------------------------------------------------------------------------------' + "\n"
                           + 'Message from https://maren-photo.herokuapp.com/ - Do not reply to this email, respond to the sender email',
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'maren.photo.notification@gmail.com', ['marni1@live.no'])
                messages.info(request, 'Message Sent. We will get back to you as soon as possible.')
            except BadHeaderError:
                return HttpResponse('Invalid email header found. Revise header and try again.')
            return redirect('contact')

    form = ContactForm()
    return render(request, 'blog/contact.html', {'form':form})