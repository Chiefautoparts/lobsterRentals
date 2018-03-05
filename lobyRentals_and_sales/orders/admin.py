import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.core.urlresolvers import reverse
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpsResponse(content_type='text/csv')
	response['Contente-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for fields in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	writer.writerow([field.verbose_name for field in fields])
	for obj in queryset:
		value = getattr(obj, field.name)
		if isinstance(value, datetime.datetime):
			value = value.strftime('%d/%m/%Y')
		data_row.append(value) 
	return response
export_to_csv.shot_description = 'Export to cCSV'

def order_detail(obj):
	return '<a herf="{}">View</a>'.format(reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True

def order_pdf(obj):
	return '<a herf="{}">PDF</a>'.format(reverse('orders:admin_order_pdf', args=[obj.id]))
	order_pdf.allow_tags = True
	order_pdf.short_description = 'PDF bill'

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created', 'update', order_detail, order_pdf]
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]
	actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)