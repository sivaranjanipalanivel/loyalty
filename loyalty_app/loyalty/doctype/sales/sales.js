// Copyright (c) 2018, Loyalty and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sales', {
	refresh: function(frm) {

	}
});
frappe.ui.form.on("Sales_list", {

	amount: function(frm) {
		debugger;
		var total_amount = 0;
		var total_points=0;
		for(var i=0;i<frm.doc.products.length;i++) {
			total_amount += parseInt(frm.doc.products[i].amount) * parseInt(frm.doc.products[i].quantity);
		}
		frm.set_value("amount", total_amount);
	}
});

