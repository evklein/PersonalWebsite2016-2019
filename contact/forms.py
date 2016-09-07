from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_subject = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your Name"
        self.fields['contact_email'].label = "Your Email Address:"
        self.fields['contact_subject'].label = "Subject"
        self.fields['content'].label = "What can I do for you?"
