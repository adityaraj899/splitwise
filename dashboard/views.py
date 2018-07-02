from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Category,Friend,Bill
from django.utils import timezone
from django.shortcuts import redirect
from .forms import BillForm
from django.views.decorators.csrf import csrf_protect
import time

BILLS_PER_PAGE = 5

'''
@login_required
def index(request):
    category_list = Category.objects.order_by('-name')
    friend_list = Friend.objects.order_by('-name')
    context_dict = {'categories': category_list,'friends':friend_list}
    return render(request, 'dashboard/index.html',context_dict)
'''
@login_required
def index(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = BillForm()
    category_list = Category.objects.order_by('-name')
    friend_list = Friend.objects.order_by('-name')
    context_dict = {'categories': category_list,'friends':friend_list}
    return render(request, 'dashboard/index.html', {'form': form})

'''
def bill_list(request):
    bills = Bill.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'dashboard/bill_list.html', {'bills': bills})


def edit_bill(request):
    category_list = Category.objects.order_by('-name')
    friend_list = Friend.objects.order_by('-name')
    context_dict = {'categories': category_list,'friends':friend_list}
    return render(request, 'dashboard/edit_bill.html', context_dict)
'''


@login_required
@csrf_protect
def edit_bill(request):
    category_list = Category.objects.order_by('-name')
    friend_list = Friend.objects.order_by('-name')
    dict = {'categories': category_list,'friends':friend_list,'status': False}

    #dict = { 'status': False }

    if request.method == 'POST':
        dict['status'] = True
        dict['title'] = request.POST['title']
        dict['amount'] = request.POST['amount']
        bill = Bill(title = dict['title'], published_date = time.strftime("%Y-%m-%d %H:%M:%S"), amount = dict['amount'])
        bill.save()
    return render(request,'dashboard/edit_bill.html', dict)

@csrf_protect
def bill_record(request):
	bills = Bill.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0 : BILLS_PER_PAGE]
	dict = {'bills': bills, 'page': 1}
	if len(bills) == BILLS_PER_PAGE:
		dict['next_page'] = True
	return render(request, 'dashboard/bill_list.html', dict)
###
def bill_page(request, page):
	bills = Bill.objects.all().filter(published_date__lte=timezone.now()).order_by('-published_date')[BILLS_PER_PAGE * (int(page) - 1) : BILLS_PER_PAGE * int(page)]
	dict = {'bills': bills, 'page': page}
	if len(bills) == BILLS_PER_PAGE:
		dict['next_page'] = True
	if int(page) > 1:
		dict['pre_page'] = True
	return render(request,'dashboard/bill_list.html', dict)













'''
@login_required
def bill_new(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            post.author = request.user
            post.save()
            post = get_object_or_404(Bill, pk=post.pk)

            return redirect('bill_detail', pk=post.pk)
    else:
        form = BillForm()
    return render(request, 'dashboard/bill_edit.html', {'form': form})
'''
