from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect


def homepage(request):
    context = {

    }
    return render(request, 'homepage.html', context)

def clients(request):
    context = {

    }
    return render(request, 'clients.html', context)

def vendors(request):
    context = {

    }
    return render(request, 'vendors.html', context)

def aboutus(request):
    context = {

    }
    return render(request, 'about.html', context)

def contactus(request):
    context = {

    }
    return render(request, 'contact.html', context)
