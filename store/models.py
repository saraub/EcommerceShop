from django.db import models
from django.contrib.auth.models import User



class Item(models.Model):
    name= models.CharField(max_length=200, null=True)
    description= models.CharField(max_length=5000, null=True, blank=True)
    price= models.FloatField()
    category= models.CharField(max_length=200, null=True,default="uncategorized")
    
    image= models.ImageField(default='images/bear.png')
    image1= models.ImageField(default='images/bear.png')
    image2= models.ImageField(default='images/bear.png')
    image3= models.ImageField(default='images/bear.png')
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    user= models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    emial= models.CharField(max_length=200)
    image= models.ImageField()
    
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name= models.CharField(max_length=200, null=True)
    
    
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    ordereddate= models.DateTimeField(auto_now_add=True)
    trans_id = models.CharField(max_length=100, null=True)
    
    
    
    @property
    def get_total_price_cart(self):
        ordereditems = self.ordereditem_set.all()
        total_price_cart= sum([item.get_total_price for item in ordereditems])
        return total_price_cart
    
    @property
    def get_total_num_cart(self):
        ordereditems= self.ordereditem_set.all()
        total_num_cart= sum([item.quantity for item in ordereditems])
        return total_num_cart
        
        
 
         
    
class OrderedItem(models.Model):
    item= models.ForeignKey(Item,  on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    
    @property
    def get_total_price(self):
        total_price=self.item.price*self.quantity
        return total_price
        
        
    
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address