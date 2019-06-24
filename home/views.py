from django.shortcuts import render,redirect
from .forms import bookforms,searchform
from home.models import Book


# Create your views here.
#def home_view3(request):
   # return render(request,'home.html')

#def home_view(request):
   # return render(request,'signup.html')


#def home_view1(request):
    #return render(request,'login.html')


#def design(request):
    #return render(request,'home2.html')

def form_view(request):
    context=None
    msg=None
    form=None
    b= Book.objects.all()
    if request.method=='POST':
        form=bookforms(request.POST)
        if form.is_valid():
            #b=book.objects(book_name=form.cleaned_data('name'),
             #   author_name=form.cleaned_data('author'),
              #  date=form.cleaned_data('date'))
            b=Book.objects.Create(book_name=form.cleaned_data('name'),
                author_name=form.cleaned_data('author'),
                date=form.cleaned_data('date'))
            b.save()
            msg='Book added successfully!!!'
        else:
            msg=form.errors        
    else:
        form=bookforms()
    context={'msg':msg,'forms':form,'bk':b}
    return render(request,'forms.html',context)



def model_form(request):
    if request.method=='POST':
        form=modelbookforms(request.POST)
        if form.is_valid():
            form.save()
            msg='Book added successfully!!!'
        else:
            msg=form.errors        
    else:
        form=modelbookforms()
    context={'msg':msg,'forms':form,'bk':b}
    return render(request,'forms.html',context)


def html_form(request):
    value=''
    if request.method=='POST':
        value==request.POST.get('name')
        return render(request,'values.html',{'value':value})  
    else:
        value='wrong input'
        return render(request,'home.html')  



def booksearch(request):
    if request.method=='POST':
        form=modelbookforms(request.POST)
        q=form.cleaned_data.get('q')
        if form.is_valid():
            b=Book.objects.filter(book_name__contains=q)
            return render(request,'showtable.html',{'b':b})
    else:
        form=searchform()
        b= Book.objects.all() 
    return render(request,'showtable.html',{'b':b,'form':form})

def deletebook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    message.success(request,'Deleted#'+str(id)+'SUCCESSFULLY!!!!')
    return redirect('/')

