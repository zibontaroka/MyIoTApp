from django.shortcuts import render # type: ignore
import time


def home(request):
    # List of slide images
    slides = [
        {"url": "images/slide1.jpg"},
        {"url": "images/slide2.jpg"},
        {"url": "images/slide3.jpg"},
    ]

    # Calculate the current active slide based on the time
    current_time = int(time.time() / 3)
    current_slide_index = current_time % len(slides)


    # Pass the current slide index to the template
    return render(request, "home/index.html", {
        "slides": slides,
        "current_slide_index": current_slide_index,
    })

def about(request):
    return render(request, 'home/about.html')

def contacts_us(request):
    return render(request, 'home/contacts_us.html')

def services(request):
    return render(request, 'home/services.html')

def base(request):
    return render(request, 'home/base.html')


