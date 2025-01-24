from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import OrderItem,Order,Items,Deliverer,DelivererProfile,Restaurant

@receiver(post_save, sender=OrderItem)
def update_ratings(sender,instance,created,**kwargs):
    all_items = OrderItem.objects.all().filter(items_id = instance.items_id, rating__isnull=False)
    og = Items.objects.get(id = instance.items_id)
    if all_items:
        rate_list = [float(i.rating) for i in all_items]
        print("i = ", rate_list)
        og.rating = sum(rate_list)/len(rate_list)
        og.save()
    else:
        og.rating = instance.rating
        og.save()
    print("Triggered update item rating")


@receiver(post_save,sender = Order)
def update_deliverer_ratings(sender,instance,created,**kwargs):
    # print(instance.__dir__())
    d = Order.objects.all().filter(id = instance.deliverer_id, rating__isnull = False)
    if instance.deliverer_id:
        og = DelivererProfile.objects.get(user_id = instance.deliverer_id)
        
        if d and og:

            # print(d)
            # print('lst=',[i for i in d])
            rate_list = [float(i.rating) for i in d]
            print("d=",rate_list)
            og.rating = sum(rate_list)/len(rate_list)
            og.save()
        else:
            og.rating = instance.rating
            og.save()
        print("Triggered update deliverer rating")

@receiver(post_save,sender = Items)
def update_restaurant_ratings(sender,instance,created,**kwargs):
    rest = Items.objects.get(id = instance.pk).restaurant
    items = Items.objects.all().filter(restaurant_id = rest.id, rating__isnull =False)
    rate_list = [float(i.rating) for i in items]
    print("r=",rate_list)
    rest.rating = sum(rate_list)/len(rate_list)
    rest.save()
    print("Triggered update restaurant rating")
