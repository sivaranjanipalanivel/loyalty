from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
	{
			"label": _("Promotions"),
			"items": [
                {
					"type": "doctype",
					"name": "Advertisement"
				},
				  {
					"type": "doctype",
					"name": "Affiliates"
				},
				  {
					"type": "doctype",
					"name": "Reward Point"
				},
			]
		},
		
		{
			"label": _("Products"),
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
					"name": "Sales"
				},
				{
					"type": "doctype",
					"name": "Coupons"
				}

			]
		},
		
		# {
		# 	"label": _("Reward/Redeem Points"),
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Reward Point"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Bonus Points"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Scholarship Range"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Scholarship"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Student Scholarship"
		# 		}
  #       	]
		# },
		# {
		# 	"label": _("Sales/Orders"),
		# 	"items": [
		# 	{
		# 			"type": "doctype",
		# 			"name": "Sales"
		# 		},
		# 		# {
		# 		# 	"type": "doctype",
		# 		# 	"name": "Redeem Orders"
		# 		# }
		# 	]
		# },
		{
			"label": _("Scholarship"),
			"items": [
			  {
					"type": "doctype",
					"name": "Scholarship Range"
				},
				{
					"type": "doctype",
					"name": "Scholarship"
				},
				{
					"type": "doctype",
					"name": "Exam"
				},
				{
					"type": "doctype",
					"name": "Questions"
				},		
			]
		},
		# {
		# 	"label": _("Support"),
		# 	"items": [
		# 		{
		# 			"type": "doctype",
		# 			"name": "Knowledge centre"
		# 		},
		# 		{
		# 			"type": "doctype",
		# 			"name": "Ticket Management"
		# 		}

		# 	]
		# }
		{
			"label": _("History"),
			"items": [
				{
					"type": "doctype",
					"name": "Reward Points History"
				},
				# {
				# 	"type": "doctype",
				# 	"name": "Bonus Points History"
				# },
				# {
				# 	"type": "doctype",
				# 	"name": "Customer Enquiry"
				# }

			]
		},
		{
			"label": _("Promotors"),
			"items": [
				{
					"type": "doctype",
					"name": "Agents"
				},
				{
					"type": "doctype",
					"name": "Staff"
				},
				{
					"type": "doctype",
					"name": "Student"
				}

			]
		},
	]