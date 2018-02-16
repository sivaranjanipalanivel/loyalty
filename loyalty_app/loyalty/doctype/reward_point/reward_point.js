// Copyright (c) 2018, Loyalty and contributors
// For license information, please see license.txt

frappe.ui.form.on('Reward Point', {
	refresh: function(frm) {

	},
	onload: function(frm){
		console.log(frm.doc.customer)
		if(frm.doc.status === "Approved" || frm.doc.status === "Rejected"){
			cur_frm.disable_save();
		}
		else{
			cur_frm.enable_save();
		}
	}
	
});
