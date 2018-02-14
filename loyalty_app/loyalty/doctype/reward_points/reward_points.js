// Copyright (c) 2018, Loyalty and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reward Points', {
	refresh: function(frm) {

	},
	onload: function(frm){
		console.log(frm.doc.customer)
			frappe.call({
				method: "frappe.client.get_list",
				args: {
					doctype: "Points Management",
					filters: [["customer", "=", frm.doc.customer]],
					fields: ["rewardtype","productid","qr_code","productname","points","status"]
				},
				callback: function(r) {
					console.log(r.message)
				   for(var e=0; e<r.message.length; e++){
						frappe.model.add_child(cur_frm.doc, "Reward List", "history");  
				        $.each(frm.doc.history || [], function(e, v) {
					        frappe.model.set_value(v.doctype, v.name, "rewardtype", r.message[e].rewardtype)
					        frappe.model.set_value(v.doctype, v.name, "productid", r.message[e].productid)
					        frappe.model.set_value(v.doctype, v.name, "qr_code", r.message[e].qr_code)
					        frappe.model.set_value(v.doctype, v.name, "productname", r.message[e].productname)
					        frappe.model.set_value(v.doctype, v.name, "points", r.message[e].points)
					        frappe.model.set_value(v.doctype, v.name, "status", r.message[e].status)
				        })
				        frm.refresh_field("history");			
					}
				}
			});
	},
});
