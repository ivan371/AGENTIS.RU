from django.contrib import admin
from .models import User_AGENTIS
from .models import orders_data
from .models import order
from .models import message
from .models import image

admin.site.register(User_AGENTIS)
admin.site.register(orders_data)
admin.site.register(order)
admin.site.register(message)
admin.site.register(image)
