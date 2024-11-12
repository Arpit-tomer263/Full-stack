
from django.shortcuts import render
import math
import random
import string
from bot.models import Contact,UserCredential
from threading import Thread, Event
from django.core.mail import send_mail
from django.conf import settings


# Global variables
Keys = []
user_data = {}

def Making_key():
    characters = string.ascii_uppercase + string.digits
    key = ''.join(random.choices(characters, k=13))
    Keys.append(key)
    return key

def entery(request):
    return render(request, "index.html")

def money_management(request):
    if request.method == 'POST':
        initial_amount = request.POST.get('initial_amount')
        try:
            initial_amount = int(initial_amount)
            results = calculate_money_management(initial_amount)
            context = {'results': results}
        except ValueError:
            context = {'error': 'Please enter a valid integer for your account balance.'}
    else:
        context = {}

    return render(request, 'moneymanegment.html', context)

def calculate_money_management(initial_amount):
    num_days = 30
    results = []

    def calculate_trades_needed(profit, trade_amount):
        num_trades = profit / trade_amount
        return math.ceil(num_trades)

    def rounded_stp(trade_amount):
        stp_lss = trade_amount * 3
        return math.ceil(stp_lss)

    for day in range(num_days):
        trade_amount = initial_amount * 3.5 / 100
        profit = trade_amount * 5 / 100 * 80
        total_amount = initial_amount + profit
        MTG = trade_amount + initial_amount * 1.5 / 100
        num_trades = calculate_trades_needed(profit, trade_amount)
        stp_lss = rounded_stp(trade_amount)

        results.append((initial_amount, profit, total_amount, trade_amount, MTG, num_trades, stp_lss))
        initial_amount = total_amount

    return results

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        problem = Contact(name=name, email=email, description=description)
        problem.save()
    return render(request, 'contact.html')

def Generate_key(request):
    if request.method == "POST":
        # Fetch the username from the form
        username = request.POST.get('username')
        Email = request.POST.get('Email') 

        # Check if there's a validated UTR in the session
        if 'validated_utr' in request.session:
            # Generate the key only if the UTR is validated
            generated_key = Making_key()
            subject = 'Your Generated Key'
            message = f'Thank you for registering. Your generated key is: {generated_key} with this username {username}. Use it wisely!'
            
            email_from = settings.DEFAULT_FROM_EMAIL  # Make sure this is set in your settings.py
            recipient_list = [Email]  # Email must be in a list
            
            send_mail(subject, message, email_from, recipient_list)
            # Save the username and key to the database
            UserCredential.objects.update_or_create(username=username, defaults={'key': generated_key})

            # Remove the validated UTR from the session after successful key generation
            del request.session['validated_utr']

            return render(request, 'Generate.html', {'key': generated_key, 'Flag': True})
        
        # If no validated UTR, don't generate the key
        return render(request, 'Generate.html', {'error': 'UTR not validated!'})

    return render(request, 'Generate.html')

def Check_key(request):
    global message,mtg,result
    context = {'error': False}  # Initialize context with 'error' set to False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('Key')
        
        try:
            # Retrieve the user credential based on the provided username
            user = UserCredential.objects.get(username=username)
            
            # Check if the provided key matches the key stored in the database for that username
            if user.key == password:
                return render(request, 'home.html', context)  # Pass the context to 'home.html'
            else:
                context['error'] = True  # Set 'error' to True if the key is incorrect
        except UserCredential.DoesNotExist:
            # Handle the case where the username does not exist in the database
            context['error'] = True  # Set 'error' to True if the username does not exist

    return render(request, 'index.html', context)

def  fetch_utr():
    global utr
    utr = []
    #logic goes here
    testutr = 7592301521
    utr.append(testutr)
    return utr

def Check_utr(request):
    utrs = fetch_utr()
    if request.method == 'POST':
        try:
            user_utr = int(request.POST.get('utr'))  # Convert user UTR to an integer
        except ValueError:
            # Handle the case where the UTR is not a valid integer
            return render(request, 'Generate.html', {'Flag': False, 'error': 'Invalid UTR'})

        if user_utr in utrs:
            # Store the validated UTR in session
            request.session['validated_utr'] = user_utr
            return render(request, 'Generate.html', {'Flag': True})
    
    return render(request, 'Generate.html')



def check_admin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        if username == 'Arpit_tomer7599' and password == '7592301521APPI':
            return render(request,'dashboard.html')
        else:
            return render(request,'admin.html')
    return render(request,'admin.html')