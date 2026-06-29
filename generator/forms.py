from django import forms

class PasswordForm(forms.Form):
    platform = forms.CharField(max_length=100, label="Platform/Service (e.g., Google)", required=False)
    
    # NEW FIELD
    username = forms.CharField(max_length=100, label="Username (optional)", required=False)

    min_length = forms.IntegerField(label="Minimum Password Length", required=False)
    max_length = forms.IntegerField(label="Maximum Password Length", required=False)
    actual_length = forms.IntegerField(label="Exact Password Length", required=False)
    specific_chars = forms.CharField(max_length=50, label="Specific Characters/Block (e.g., 'abc')", required=False)
    
    char_types = forms.MultipleChoiceField(
        choices=[('upper', 'Uppercase Letters'), ('lower', 'Lowercase Letters'),
                 ('digit', 'Numbers'), ('symbol', 'Symbols')],
        widget=forms.CheckboxSelectMultiple,
        label="Character Types",
        required=False
    )
    owner_name = forms.CharField(max_length=100, label="Password Owner's Name", required=False)
    dob = forms.CharField(max_length=10, label="Date of Birth (e.g., 1990)", required=False)
    others = forms.CharField(widget=forms.Textarea, label="Other Details (e.g., favorite pet)", required=False)