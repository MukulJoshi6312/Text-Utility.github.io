# I have create this file - M u k u l
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request, "index.html")


def analyze(request):
    djtext = request.POST.get ('text', 'default')
    removepunc = request.POST.get ('removepunc', 'off')
    capitalize = request.POST.get ('capitalize', 'off')
    removenewline = request.POST.get ('removenewline', 'off')
    extraspaceremover = request.POST.get ('extraspaceremover', 'off')
    charcount = request.POST.get ('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations',
                  'analyze_text':analyzed}
        djtext = analyzed

    if  capitalize == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalization',
                  'analyze_text': analyzed}
        djtext = analyzed

    if  removenewline == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line',
                  'analyze_text': analyzed}
        djtext = analyzed

    if  extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate (djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra space remover'
            , 'analyze_text': analyzed}
        djtext = analyzed


    if  charcount == "on":
        analyzed = 0
        for i in range (0, len (djtext)):
            if djtext[i] != ' ':
                analyzed = analyzed + 1
        params = {'purpose': 'Counting the character in a string',
                  'analyze_text': "Total Character = "+str(analyzed)}
        djtext = analyzed

    if removepunc!= "on" and extraspaceremover != "on" and removenewline!= "on" and charcount!= "on" and capitalize!= "on":
        return HttpResponse ("Please select any option!")


    return  render(request,'analyez.html',params)



def about(request):
    return  render(request,"about.html")


def contact(request):
    return  render(request,"contact.html")
