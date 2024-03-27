from django.contrib import admin
from django.utils.translation import gettext_lazy as _
# Register your models here.
from .models import *



@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    exclude = ('user',)  # Excluye el campo 'user' del formulario de administración
    list_display = ['local_name', 'type', 'active']
    search_fields = ['local_name', 'type']
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        # Filtra los locales por el usuario actual
        else: 
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
            
    def has_add_permission(self, request):
        # Obtiene todos los Locales asociados con el usuario actual
        existing_locals = Local.objects.filter(user=request.user)
        
        # Si el usuario ya tiene un Local, no permitimos agregar otro
        if existing_locals.exists():
            return False
        return super().has_add_permission(request)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'local']
    list_per_page = 10

    
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(local__user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "local":
            kwargs["queryset"] = Local.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def has_add_permission(self, request):
        # Obtiene todos los Locales asociados con el usuario actual
        categories = Category.objects.filter(local__user = request.user)
        if request.user.groups.filter(name='asequible').exists():
            if categories.__len__() >=3:
                return False
        if request.user.groups.filter(name='recomendado').exists():
            if categories.__len__() >=20:
                return False
        return super().has_add_permission(request)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'cost', 'active', 'discount','category']
    search_fields = ['product_name']
    list_per_page = 10
    
    
    def has_add_permission(self, request):
        # Obtiene todos los Locales asociados con el usuario actual
        products = Product.objects.filter(category__local__user = request.user)
        if request.user.groups.filter(name='asequible').exists():
            if products.__len__() >=15:
                return False
        if request.user.groups.filter(name='recomendado').exists():
            if products.__len__() >=60:
                return False
        return super().has_add_permission(request)
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(category__local__user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            if request.user.is_authenticated:
                kwargs["queryset"] = Category.objects.filter(local__user=request.user)
            else:
                kwargs["queryset"] = Category.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Aggregate)
class AggregateAdmin(admin.ModelAdmin):
    list_display = ['agregate_name', 'measurement_unit', 'measurement_unit_quantity','cost', 'product']
    list_per_page = 10
    search_fields = ['agregate_name']
    
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(product__category__local__user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category__local__user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['ingredient_name', 'product']
    search_fields = ['ingredient_name']
    list_per_page = 10
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(product__category__local__user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "product":
            kwargs["queryset"] = Product.objects.filter(category__local__user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_per_page = 10
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(local__user=request.user)
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "local":
            kwargs["queryset"] = Local.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
@admin.register(Favorite) 
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ['local', 'active','date','time']
    list_per_page = 10
    
    def has_add_permission(self, request, obj=None):
        # Check if there are 2 or more favorite locales
        favorites =Favorite.objects.filter(active=True)
        if len(favorites) >= 2:
            return False # Do not allow adding if condition is met
        return super().has_add_permission(request)


@admin.register(Reviews) 
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'active']
    exclude = ('local',)
    list_per_page = 10
    
    def get_queryset(self, request):
        # Obtén el queryset original
        qs = super().get_queryset(request)
        
        if request.user.is_superuser:
            return qs
        else: 
            return qs.filter(local__user=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Check if the user belongs to the "recommended" or "premium" group
        user_groups = request.user.groups.values_list('name', flat=True)
        if 'recommended' not in user_groups and 'premium' not in user_groups:
            # Disable all fields except 'active' if the user is not in the allowed groups
            for field in form.base_fields:
                if field != 'active':
                    form.base_fields[field].disabled = True
        return form