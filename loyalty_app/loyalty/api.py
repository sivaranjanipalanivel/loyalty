# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, cstr
from frappe.email.doctype.email_group.email_group import add_subscribers

@frappe.whitelist()
def get_offers(academic_year):
	"""Returns Fee Components.

	:param fee_structure: Fee Structure.
	"""
	if academic_year:
		fs = frappe.get_list("Offers", fields=["from_mark", "to_mark","scholarship"] , filters={"parent": academic_year}, order_by= "idx")
		return fs
