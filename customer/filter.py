class FilterQuerySet:
   def __init__(self,product,status,orders_qs):
      self.product = product
      self.status = status
      self.orders = orders_qs

   def querySearch(self):
      if self.product and self.status:
         return self.orders.filter(product=self.product, status=self.status)
      elif self.product:
         return self.orders.filter(product=self.product)
      elif self.status:
         return self.orders.filter(status=self.status)