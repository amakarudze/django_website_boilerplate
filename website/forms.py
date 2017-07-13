from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


from website.models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'subject', 'message',)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-Crispy_ContactForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('send', 'Send Email'))
        # Moving field labels into placeholders
        layout = self.helper.layout = Layout()
        for field_name, field in self.fields.items():
            layout.append(Field(field_name, placeholder=field.label))
        self.helper.form_show_labels = False
