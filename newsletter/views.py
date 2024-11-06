from django.shortcuts import render
from django.core.mail import send_mass_mail
from django.views import View
from django.contrib import messages
from . models import Subscriber, Newletter

# Create your views here.
# Subscription page

class SubcriptionPage(View):
    template_name = 'subscribe.html'
    model = Subscriber
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        email = request.POST.get('email')

        if Subscriber.objects.filter(email=email).exists():
            messages.error(request,"Sorry, this Email already registered")
            
        elif email:
            sub = Subscriber(email=email)
            sub.save()
            messages.success(request,'Thank you for registering to our Newsletter')

        else:
            messages.error(request, 'Please provide a valid email')
        return render(request, self.template_name)

# to create a Newsletter
class CreateNewsletter(View):
    template_name = 'newsletter.html'
    model = Newletter

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        title = request.POST.get('title')
        body = request.POST.get('body')

        # check if title already exists
        if Newletter.objects.filter(title=title).exists():
            messages.error(request, 'This Newsletter already exist')

        elif title and body:
            news = Newletter(title=title, body=body)
            news.save()
            messages.success(request, 'saved')


            # mail componenet
            subject = news.title
            message = news.body
            from_email = 'demzyukonta@gmail.com'
            recipients = Subscriber.objects.values_list('email', flat=True)
            
            # sending mass mail
            if recipients:
                email_message = [
                    (subject, message, from_email, [email])
                    for email in recipients
                ]
                send_mass_mail(email_message)
                messages.success(request, "Newsletter SENt to all Subscribers.")

            else:
                messages.info(request, 'No subscribers to send to')
        else:
            messages.error(request, 'please provide both a title and body')
        return render(request, self.template_name)
    


        

