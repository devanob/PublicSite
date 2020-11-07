from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import  Project,ProjectCategory



class ProjectAdmin(ModelAdmin):
    model = Project
    menu_label = "Projects"  
    menu_icon = "pick" 
    menu_order = 200 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("project_name", 'Categories', 'show_case')
    def Categories(self, obj):
        return ", ".join([cat.name for cat in obj._categories.all()])

    def get_tags(self,obj):
        return "\n".join(["hello" for tags in obj.tags])

    list_filter = ("tags","_categories")
    search_fields = ("project_name",)

class ProjectCategoryAdmin(ModelAdmin):
    model = ProjectCategory
    menu_label = "Project Categories"  
    menu_icon = "pick" 
    menu_order = 200 
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ("name",)
    #list_filter = ("tags",)
    search_fields = ("name",)

#modeladmin_register(ProjectAdmin)

class ProjectsGroup(ModelAdminGroup):
    menu_label = 'Project Management'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (ProjectAdmin,ProjectCategoryAdmin)

modeladmin_register(ProjectsGroup)