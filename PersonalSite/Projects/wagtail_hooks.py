from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import  Project



class ProjectAdmin(ModelAdmin):
    model = Project
    menu_label = "Projects"  
    menu_icon = "pick" 
    menu_order = 200 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("project_name",'tags')
    list_filter = ("tags",)
    search_fields = ("project_name",)


modeladmin_register(ProjectAdmin)