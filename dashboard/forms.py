from django import forms
from .models import Bill

'''
class BillForm(forms.ModelForm):
    tag = forms.CharField(required=False)
    class Meta:
        model = Bill
        fields = ('title', 'text',)
'''
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class FriendForm(forms.ModelForm):
    name = forms.CharField(max_length=128)

    def __str__(self):
        return self.name



CATEGORY_CHOICES = [
    ('food','Food'),
    ('rent','Rent'),
    ('fee','Fee'),
]

FRIEND_CHOICES = [
    ('Ambuj','Ambuj'),
    ('Aditya','Aditya'),
    ('Aashish','Aashish'),
    ('Raju','Raju'),
]

class BillForm(forms.Form):
    #category = forms.ForeignKey(Category, on_delete=models.CASCADE)
    category = forms.CharField(label='Where you have invested ?',widget=forms.Select(choices=CATEGORY_CHOICES))
    title = forms.CharField(max_length=128)
    amount = forms.IntegerField()
    #paidby = forms.ForeignKey(Friend, on_delete=models.CASCADE)
    paidby = forms.CharField(label='Who paid it ?',widget=forms.Select(choices=FRIEND_CHOICES))
    #published_date = forms.DateTimeField()

    def clean(self):
        cleaned_data = super(BillForm, self).clean()
        title = cleaned_data.get('title')
        amount = cleaned_data.get('amount')
        paidby = cleaned_data.get('paidby')
        if not title and not amount and not paidby:
            raise forms.ValidationError('You have to write something!')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    '''
    def __str__(self):
        return self.title
    '''
