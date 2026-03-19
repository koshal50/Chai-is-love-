from django.contrib import admin
from .models import chaiVariety,CHaiReview,Store,Certificate,ContactMessage,about_description
# Register your models here.
class ChaiReviewInline(admin.TabularInline):  #- Purpose: This defines an inline form for the CHaiReview model inside the Django admin.

  model = CHaiReview
  extra = 1  # displays extra empty column



#- Purpose: Customizes how the ChaiVariety model appears in the Django admin.
class ChaiVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline] #- Embeds the ChaiReviewInline inside the ChaiVariety admin page.




#this is an admin class from this an new section is created with a reference of store model

class StoreAdmin(admin.ModelAdmin):
  list_display=('name', 'location',)
  filter_horizontal=('chai_varieties',)# needed for mamy to many fields ensures arrows for exchange



class CertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number','issued_date','valid')
  
admin.site.register(chaiVariety,ChaiVarietyAdmin) # registering the model so that it appears in the admin panel
admin.site.register(Store,StoreAdmin)
admin.site.register(Certificate,CertificateAdmin)
admin.site.register(ContactMessage)
admin.site.register(about_description)
