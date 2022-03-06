from django import forms
from orders.models import Orders, SourceDestination
from django_currentuser.middleware import get_current_authenticated_user



class OrderForm(forms.ModelForm):
    
    class Meta:
       
        model = Orders
        exclude = ['booker', 'order_status', 'payed', 'rider', 'price']
        # pick_up_time = forms.TimeInput(attrs={'type': 'time'})
        fields = '__all__'

        widgets = {
            'pick_up_date': forms.DateInput(attrs={'type': 'date'}),
            'pick_up_time': forms.TimeInput(attrs={'type': 'time'},format='%H:%M'),
            'address': forms.Textarea(attrs={'rows':'3','style': 'resize:none'})
        }
    
    def save(self, commit=True): 
        
        user = super().save(commit=False)
    
        source = self.cleaned_data["source"]
        destination = self.cleaned_data["destination"]
        set_price = SourceDestination.objects.get(source = source, destination=destination)
        user.price = set_price.price
        user.booker = get_current_authenticated_user()
        if commit:
            user.save()
        return user