#this file is created by me
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    #get the text
    dgtext=(request.POST.get("text","default"))
    removepunc=request.POST.get("removepunc","off")
    fullcaps=request.POST.get("fullcaps","off")
    new_line_remover=request.POST.get("new_line_remover","off")
    removespace=request.POST.get("removespace","off")
    print(removepunc)
    #analyze the text
    punctuations='''.?()<>""'''
    if removepunc=="on":
        analyzed=""
        for char in dgtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removes Punctuations', 'analyzed_text':analyzed}
        dgtext=analyzed
        #return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in dgtext:
            analyzed+=char.upper()
        params={'purpose':'change uppercase', 'analyzed_text':analyzed}
        dgtext=analyzed
        #return render(request,'analyze.html',params)
    if new_line_remover=="on":
        analyzed=""
        for char in dgtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'change uppercase', 'analyzed_text':analyzed}
        dgtext=analyzed
        #return render(request,'analyze.html',params)
    if removespace=="on":
        analyzed=""
        for index,char in enumerate(dgtext):
            if not(dgtext[index]==" " and dgtext[index+1]==" "):
                analyzed+=char
        params={'purpose':'remove space', 'analyzed_text':analyzed}   
    return render(request,'analyze.html',params)
def navigate(request):
    return HttpResponse('''<h3>hello harry</h3>
    <ol>
    <li><a href="https://erp.aktu.ac.in/"> aktu login</a>
    </li>
    <li><a href="https://www.youtube.com/" >youtube</a>
    </li>''')
    