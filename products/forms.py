from django import forms
from products.models import Order,Product,Tag

class UpdateOrderForm(forms.ModelForm):
   STATUS = (
      (None,'----------'),
      ('Pending', 'Pending'),
      ('Out for Delivery', 'Out for Delivery'),
      ('Delivered', 'Delivered')
   )
   status = forms.ChoiceField(required=False,choices=STATUS,widget=forms.Select(attrs={'class':'form-select '}))

   class Meta:
      model = Order
      exclude = ['customer','product']

class SearchOrderForm(forms.ModelForm):
   STATUS = (
      (None,'----------'),
      ('Pending', 'Pending'),
      ('Out for Delivery', 'Out for Delivery'),
      ('Delivered', 'Delivered')
   )
   product = forms.ModelChoiceField(required=False, queryset=Product.objects.all(),widget=forms.Select(attrs={'class':'form-select'}))
   status = forms.ChoiceField(required=False,choices=STATUS,widget=forms.Select(attrs={'class':'form-select '}))

   class Meta:
      model = Order
      exclude = ['customer']

class ProductAddForm(forms.ModelForm):
   CHOICE = (
      ('Indoor','Indoor'),
      ('Outdoor','Outdoor')
   )
   name = forms.CharField(label='Product', widget=forms.TextInput(attrs={'class':'form-control form-control-sm mb-2'}))
   price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-sm mb-2'}))
   category = forms.ChoiceField(choices=CHOICE,widget=forms.Select(attrs={'class':'form-select '}))
   tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.SelectMultiple(attrs={'class':'form-select'}))
   
   class Meta:
      model    = Product
      fields   = '__all__'