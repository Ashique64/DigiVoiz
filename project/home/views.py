from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        subject = f"New Inquiry from {name}"

        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        Message: {message}
        """

        html_message = f"""
        <html>
            <body>
                <h2>New Inquiry Details</h2>
                <table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; font-family: Arial, sans-serif;">
                    <tr><th align="left">Name</th><td>{name}</td></tr>
                    <tr><th align="left">Email</th><td>{email}</td></tr>
                    <tr><th align="left">Phone</th><td>{phone}</td></tr>
                    <tr><th align="left">Subject</th><td>{subject}</td></tr>
                    <tr><th align="left">Message</th><td>{message}</td></tr>
                </table>
            </body>
        </html>
        """

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['ashique9496@gmail.com'],
                fail_silently=False,
                html_message=html_message
            )
            messages.success(
                request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")
        return redirect('contact')

    return render(request, 'index.html')
