from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NameForm
from .models import Post
from .models import Artist
from .models import Show
from .models import Sust   
from django.contrib import messages
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

##############################################################
################   Home Page           #######################
##############################################################

def home(request):
	
	context = {
		'artist': Artist.objects.all()
	}

	return render(request, 'blog/home.html', {'title': 'Home', 'artist': Artist.objects.all()})


##############################################################
################   Navbar Main Pages   #######################
##############################################################

def news(request):
	
	#posts =  Post.objects.filter().order_by('-date_posted')[0:5]
	posts = Post.objects.all().order_by('-date_posted')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 4)

	try:
		numbers = paginator.page(page)
	except PageNotAnInteger:
		numbers = paginator.page(1)
	except EmptyPage:
		numbers = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/news.html', {'title': 'News', 'numbers': numbers})
	#return render(request, 'blog/news.html', {'title': 'News',  'posts': posts})


def shows(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/shows.html', {'title': 'Shows', 'show': Show.objects.all()})


def sustainability(request):
	
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})


##############################################################
################   Navbar Secondary Pages   ##################
##############################################################

def contact(request):
	return render(request, 'blog/contact.html', {'title': 'Contact'})


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})



##############################################################
################     ARTIST PAGES    #########################
##############################################################

def artist1(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist1.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist2(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist2.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist3(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist3.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist4(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist4.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist5(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist5.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist6(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist6.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

def artist7(request):
	context = {
		'artist': Artist.objects.all()
	}
	return render(request, 'blog/artist1.html', {'title': 'Art Shop', 'artist': Artist.objects.all()})

##############################################################
################     Show PAGES      #########################
##############################################################

def show1(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show1.html', {'title': 'Shows', 'show': Show.objects.all()})

def show2(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show2.html', {'title': 'Shows', 'show': Show.objects.all()})

def show3(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show3.html', {'title': 'Shows', 'show': Show.objects.all()})

def show4(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show4.html', {'title': 'Shows', 'show': Show.objects.all()})

def show5(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show5.html', {'title': 'Shows', 'show': Show.objects.all()})

def show6(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show6.html', {'title': 'Shows', 'show': Show.objects.all()})

def show7(request):
	context = {
		'show': Show.objects.all()
	}
	return render(request, 'blog/show7.html', {'title': 'Shows', 'show': Show.objects.all()})


##############################################################
################     Sustain. Pages     ######################
##############################################################

def sustainability1(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability1.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability2(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability2.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability3(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability3.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability4(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability4.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability5(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability5.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability6(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability6.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})

def sustainability7(request):
	context = {
		'sust': Sust.objects.all()
	}

	return render(request, 'blog/sustainability7.html', {'title': 'Sustainability', 'sust': Sust.objects.all()})


##############################################################
################     Post PAGES      #########################
##############################################################

row = 1

def signup(request):
	if request.method == "POST":

		form = NameForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data.get('name')
			email = form.cleaned_data.get('email')
			messages.success(request, f"Thanks {name}, your Email has been successfully added. You'll hear from us soon!")

			scope =  ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
			creds = ServiceAccountCredentials.from_json_keyfile_name('django_thesocial/gcreds.json', scope)
			client = gspread.authorize(creds)
			sheet = client.open("testing-signup").sheet1

			global row

			def next_available_row(worksheet):
				str_list = list(filter(None, sheet.col_values(1)))
				return str(len(str_list)+1)
			
			next_row = next_available_row(sheet)

			sheet.update_cell(next_row, 1, name)
			sheet.update_cell(next_row, 2, email) 


			return redirect('social-home')

	else:

		form = NameForm()

	return render(request, 'blog/signup.html', {'form': form, 'title': 'Signup'})
