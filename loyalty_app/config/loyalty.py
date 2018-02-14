from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Product"),
			"items": [
				{
					"type": "doctype",
					"name": "Category"
				},
				{
					"type": "doctype",
					"name": "Products"
				},
				{
					"type": "doctype",
					"name": "Coupons"
				}

			]
		},
		{
			"label": _("Customers"),
			"items": [
				{
					"type": "doctype",
					"name": "Customers"
				},
				{
					"type": "doctype",
					"name": "Reward Points"
				}

			]
		},
		{
			"label": _("Orders"),
			"items": [
				{
					"type": "doctype",
					"name": "Points Management"
				},
				{
					"type": "doctype",
					"name": "Orders"
				}

			]
		},
		{
			"label": _("Promotions"),
			"items": [
				{
					"type": "doctype",
					"name": "Sliders"
				}

			]
		},
		{
			"label": _("Quiz"),
			"items": [
				{
					"type": "doctype",
					"name": "Question"
				},
				{
					"type": "doctype",
					"name": "Quiz"
				}

			]
		},
		{
			"label": _("Support"),
			"items": [
				{
					"type": "doctype",
					"name": "Knowledge centre"
				},
				{
					"type": "doctype",
					"name": "Ticket Management"
				}

			]
		}
	]