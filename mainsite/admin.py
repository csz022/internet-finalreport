from django.contrib import admin
from .models import Member, MemberMessage

# Register your models here.
admin.site.register(Member)
admin.site.register(MemberMessage)
