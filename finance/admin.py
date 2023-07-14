from django.contrib import admin
from .models import Sales, Branches, Employee
from import_export.admin import ExportActionMixin


# Branch Actions
@admin.action(description="Seçili şubeleri yayınla")
def make_branch_published(modeladmin, request, queryset):
    queryset.update(status='1')


@admin.action(description="Seçili şubeleri yayından kaldır")
def make_branch_draft(modeladmin, request, queryset):
    queryset.update(status='0')


UYARITEXT = 'Bütün para birimleri TL olarak yazılmalıdır'


# Sales Admin
class SalesAdmin(ExportActionMixin, admin.ModelAdmin):
    # fields ekranda görünmesini istediğimi form alanlarını grupluyarak göstermemizi sağlar.
    # fields = ('name', ('phone', 'email'), ('city', 'country'))

    fieldsets = (
        ('Şube', {
            'fields': ('branch',),
        }),
        ('Günlük Satış Rakamları', {
            'fields': ('date', ('credit', 'cash', 'expense', 'remain'), ('turnover',),),
            'description': '%s' % UYARITEXT,

        }),
        ('Personel Bilgileri', {
            'fields': ('author', ('status',)),
            'classes': ('collapse',),  # other options: extrapretty, wide
        }),
    )

    list_display = ('date', 'credit', 'cash', 'expense', 'remain', 'turnover',)
    list_filter = ('status', 'author',)
    list_display_links = ['date']
    ordering = ['id']
    search_fields = ['date', 'credit']
    # prepopulated_fields = {'name': ('name',)}
    # list_editable = ['status']
    list_per_page = 35

    # special actions
    actions = [make_branch_published, make_branch_draft]


admin.site.register(Sales, SalesAdmin)


# Branches Admin
class BranchesAdmin(admin.ModelAdmin):
    # fields ekranda görünmesini istediğimi form alanlarını grupluyarak göstermemizi sağlar.
    # fields = ('name', ('phone', 'email'), ('city', 'country'))

    fieldsets = (
        ('Adres Bilgileri', {
            'fields': ('country', 'city', 'district', 'postcode', 'address', 'addressDescription',),
        }),
        ('Şube Bilgileri', {
            'fields': ('name', 'photo',),
            # 'description': '%s' % UYARITEXT,

        }),
        ('İletişim Bilgileri', {
            'fields': ('manager', 'phone', 'email',),
            # 'classes': ('collapse',),  # other options: extrapretty, wide
        }),

        ('Çalışma Saatleri', {
            'fields': ('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun',),
        }),
        ('Diğer', {
            'fields': ('status', 'author',),
            'classes': ('collapse',),
        }),
    )
    #fields = ('author', 'createdOn', 'updatedOn', 'status')

    list_display = ('name', 'manager', 'phone', 'email', 'city', 'district',)
    list_filter = ('status', 'city',)
    list_display_links = ['name']
    ordering = ['id']
    search_fields = ['name', 'manager', 'country', 'city', 'district', 'postcode', 'address', 'description']
    # prepopulated_fields = {'name': ('name',)}
    # list_editable = ['status']
    list_per_page = 10
    # readonly_fields = ('country',)
    # special actions
    actions = [make_branch_published, make_branch_draft]


admin.site.register(Branches, BranchesAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'gender', 'dateOfBirth', 'dateOfJoin', 'dateOfQuit',)
    list_filter = ('gender',)
    list_display_links = ['firstName', 'lastName']
    ordering = ['id']
    search_fields = ['firstName', 'lastName']
    # prepopulated_fields = {'name': ('name',)}
    # list_editable = ['status']
    list_per_page = 25

    # special actions
    # actions = [make_branch_published, make_branch_draft]


admin.site.register(Employee, EmployeeAdmin)
