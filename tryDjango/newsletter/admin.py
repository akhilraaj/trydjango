from django.contrib import admin

# Register your models here.
from .forms import SignupForm
from .models import Signup

class SignupAdmin(admin.ModelAdmin):
    list_display = ["__str__","full_name"]
    form = SignupForm
    # class Meta:
    #     model=Signup
admin.site.register(Signup,SignupAdmin)
