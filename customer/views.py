from django.shortcuts import render
from .forms import RegistrationForm, LoginForm,CustomerCheckoutForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy,reverse
from adminpannel.models import Products
from django.views.decorators.csrf import csrf_exempt
from .models import CustomerCart
from django.http import JsonResponse


# Create your views here.
def registercustomer(request):
	if request.method == 'POST':
		registerform=RegistrationForm(request.POST)
		if registerform.is_valid():
			username=registerform.cleaned_data['username']
			firstname=registerform.cleaned_data['firstname']
			lastname=registerform.cleaned_data['lastname']
			email=registerform.cleaned_data['emailid']
			password=registerform.cleaned_data['password']
			if User.objects.filter(username=username).exists():
				registerform=RegistrationForm(request.POST)
				context={'registerform':registerform,'error':'This user already exists, add new one'}
				return render(request, 'customer/registercustomer.html', context)
			else:
				user=User.objects.create_user(
					username=username,
					password=password,
					email=email,
					first_name=firstname,
					last_name=lastname
					)
				user.save()
				return HttpResponseRedirect(reverse('logincustomer'))
		else:
			registerform=RegistrationForm(request.POST)
			context={'registerform':registerform}
			return render(request, 'customer/registercustomer.html', context)
	else:
		registerform=RegistrationForm()
		return render(request, 'customer/registercustomer.html',{'registerform':registerform})

def logincustomer(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse(''))
	else:
		if request.method=='POST':
			login_form=LoginForm(request.POST)
			if login_form.is_valid():
				username=login_form.cleaned_data['username']
				password=login_form.cleaned_data['password']

				user=authenticate(
					username=username,
					password=password
					)
				if user is not None:
					if user.is_active:
						login(request,user)
						return HttpResponseRedirect(reverse('products'))
					else:
						login_form=LoginForm(request.POST)
						context={'form':login_form}
						return render(request,'customer/logincustomer.html', context)
				else:
					login_form=LoginForm(request.POST)
					context={'form':login_form}
					return render(request,'customer/logincustomer.html', context)
			else:
				login_form=LoginForm(request.POST)
				context={'form':login_form}
				return render(request,'customer/logincustomer.html', context)
		else:
			login_form=LoginForm()
			return render(request,'customer/logincustomer.html', {'form':login_form})

@login_required(login_url=reverse_lazy('logincustomer'))
def logoutcustomer(request):
	logout(request)
	return HttpResponseRedirect(reverse('products')) #products

def homepage(request):
	products = Products.objects.filter(is_active=1)
	usercart=[]
	if request.user.is_authenticated:
		usercart = CustomerCart.objects.filter(customer = request.user)
	context={'products':products, 'usercart':usercart}
	return render(request, 'customer/products.html',context)

@csrf_exempt
@login_required(login_url=reverse_lazy('logincustomer'))
def addproducttocart(request):
	if request.is_ajax():
		product_id = int(request.POST['product'])
		user = request.user
		cart_instance = CustomerCart(
			customer=user,
			product_id=product_id
			)
		# if CustomerCart.objects.filter(product_id=product_id).exists:
		# 	return JsonResponse({'result':'error'})
		cart_instance.save()
		return JsonResponse({'result':'success'})

@csrf_exempt
@login_required(login_url=reverse_lazy('logincustomer'))		
def removeproductfromcart(request):
	if request.is_ajax():
		product_id = int(request.POST['product'])
		user = request.user
		cart_instance = CustomerCart.objects.filter(
			product=product_id,
			customer=user
			)
		cart_instance.delete()
		return JsonResponse({'result':'success'})


@login_required(login_url=reverse_lazy('logincustomer'))
def viewcustomercart(request):
	usercart = CustomerCart.objects.filter(customer=request.user).select_related('product')
	print(usercart)
	totalprice=sum(item.product.price for item in usercart)
	checkoutForm = CustomerCheckoutForm()
	context={'totalprice':totalprice, 'usercart':usercart,'checkoutform':checkoutForm}
	return render(request, 'customer/customercart.html', context)

@login_required(login_url=reverse_lazy('logincustomer'))
def removeproductcartpage(request, cart_item_id):
	user=request.user
	cart_instance=CustomerCart.objects.filter(customer=user, id=cart_item_id)
	cart_instance.delete()
	return HttpResponseRedirect(reverse('viewcustomercart'))