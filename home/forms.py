from django import forms
from home.models import Book,Author,Genre

class bookforms(forms.Form):
    name=forms.CharField(label='book name',
        widget=forms.TextInput(attrs={
            'maxlength':'30','placeholder':'book name'
        }))
    
    author=forms.ModelChoiceField(
                        queryset=Author.objects.all(),
                        empty_label='Author',widget=forms.Select(attrs={'placeholder':'Author',
                        'name':Author,
                        'id':'author','class':'custom-select'}))

   # genre=forms.ModelMultipleChoiceField(queryset=genre.objects.all(),
    #empty_label='',widget=forms.CheckboxSelectMultiple)

    pur_date=forms.DateField(label='',widget=forms.DateInput(attrs={'placeholder':'pur-date','name':'pur_date',
    'id':'pur_date','class':'form-control'}))
    #summary=forms.CharField(label='summary',
    #                        widget=forms.TextInput(attrs={'placeholder':'summary',
    #                        'name':'summary',
    #                        'id':'summary','class':'form-control'}))

    #isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'isbn',
    #                        'name':'isbn',
    #                        'id':'isbn','class':'form-control'}))

    genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                                        widget=forms.CheckboxSelectMultiple)                                                               
    #multiplechoicefield gives the options with a checkbox
    #checkboxmultiple creates check box
class modelbookforms(forms.ModelForm):
    name=forms.CharField(label='book name',
        widget=forms.TextInput(attrs={
            'maxlength':'30','placeholder':'book name'
        }))
    
    author=forms.ModelChoiceField(
                        queryset=Author.objects.all(),
                        empty_label='Author',widget=forms.Select(attrs={'placeholder':'Author',
                        'name':Author,
                        'id':'author'}))


    summary=forms.CharField(label='summary',
                            widget=forms.TextInput(attrs={'placeholder':'summary',
                            'name':'summary',
                            'id':'summary','class':'form-control'}))

    isbn=forms.CharField(label='ISBN Number',widget=forms.TextInput(attrs={'placeholder':'isbn',
                            'name':'isbn',
                            'id':'isbn','class':'form-control'}))

    genre=forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),
                                        widget=forms.CheckboxSelectMultiple)                                                               



    class Meta:

        model=Book#dependency injection 
        fields='__all__'
        
class searchform(forms.Form):
    q=forms.CharField(label='',
        widget=forms.TextInput(attrs={
            'maxlength':'30','placeholder':'search','class':'form-control','minlength':'2'
        }))






"""class CustomForms(forms.Form):

    username=forms.CharField(
        label='username',

        widget=forms.TextInput(
            attrs={'placeholder':'your username','class':'form-control','max':'20'})
    )

    email=forms.EmailField(label='your email',widget=forms.EmailInput(attrs={'placeholder':'hb@hmail.com',
    'class':'formcontrol'}))"""




















    