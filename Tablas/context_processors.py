from .models import Carrito

def carrito_count(request):
    if request.user.is_authenticated:
        count = Carrito.objects.filter(cliente=request.user).count()
    else:
        count = 0
    return {'carrito_count': count}


