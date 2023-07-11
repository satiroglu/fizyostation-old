from django.contrib import admin
from .models import Branch, Page


# Branch Actions
@admin.action(description="Seçili şubeleri yayınla")
def make_branch_published(modeladmin, request, queryset):
    queryset.update(status='1')


@admin.action(description="Seçili şubeleri yayından kaldır")
def make_branch_draft(modeladmin, request, queryset):
    queryset.update(status='0')

UYARITEXT = 'Merhaba bu bir uyarıdır.'

# Branch Admin
class BranchAdmin(admin.ModelAdmin):
    # fields ekranda görünmesini istediğimi form alanlarını grupluyarak göstermemizi sağlar.
    # fields = ('name', ('phone', 'email'), ('city', 'country'))

    fieldsets = (
        ('Adres Bilgileri', {
            'fields': ('name', ('country', 'city'), ('phone', 'email'),),
            'description': '%s' % UYARITEXT,
            'classes': ('collapse',), # other options: extrapretty, wide
        }),
        ('Diğer Bilgiler', {
            'fields': ('description', ('postcode', 'district'), ('author', 'status')),
            'classes': ('extrapretty',),
        }),
    )

    list_display = ('name', 'phone', 'email', 'city', 'country', 'status')
    list_filter = ('status', 'author', 'city', 'country')
    list_display_links = ['name']
    ordering = ['id']
    search_fields = ['name', 'description']
    # prepopulated_fields = {'name': ('name',)}
    # list_editable = ['status']
    list_per_page = 10

    # special actions
    actions = [make_branch_published, make_branch_draft]

admin.site.register(Branch, BranchAdmin)


# Page Admin
class PageAdmin(admin.ModelAdmin):
    list_display = ('pageTitle', 'menuTitle', 'status')
    list_filter = ('status',)
    list_display_links = ['pageTitle']
    ordering = ['id']
    search_fields = ['pageTitle', 'menuTitle']
    # prepopulated_fields = {'slug': ('slug',)}
    # list_editable = ['status']
    list_per_page = 10

    # special actions
    actions = [make_branch_published, make_branch_draft]


admin.site.register(Page, PageAdmin)

