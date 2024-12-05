from django.shortcuts import render
from .forms import ContactForm  # Import your form class

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form (e.g., save to database, send email)
            form.save()  # Example if your form is a ModelForm
    else:
        form = ContactForm()  # Instantiate an empty form

    # Pass the form instance to the template
    return render(request, 'contact.html', {'contact_form': form})
