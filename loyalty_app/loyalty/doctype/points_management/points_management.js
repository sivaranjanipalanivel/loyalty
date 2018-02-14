// Copyright (c) 2018, Loyalty and contributors
// For license information, please see license.txt

frappe.ui.form.on('Points Management', {
	refresh: function(frm) {

	}
	// after_save: function() {
	// 	if (!cur_frm.doc.__islocal) {
	// 		if(cur_frm.doc.status == "Approved"){
	// 		  $.ajax({
	// 		  url : window.location.origin+"/api/resource/Reward Points",
	// 		  dataType: 'text',
	// 		  type: 'POST',
	// 		  contentType: 'application/json',
	// 		  data : JSON.stringify( {
	// 		  "customer" : cur_frm.doc.customer,
	// 		  "customername" : cur_frm.doc.customername,

	// 		  }
	// 		  ),
	// 		  beforeSend: function(xhr){
	// 		  xhr.setRequestHeader(
	// 		  'X-Frappe-CSRF-Token', frappe.csrf_token
	// 		  );
	// 		  },success: function(data){
	// 		  console.log(data); 
	// 		  }, error: function(error){
	// 		  console.log(error);
	// 		  }
	// 		  });
	// 		}
	// 	}
	// 	else
	// 	{
	// 		frappe.throw(__("Save the Document first"));
	// 	}
	// }
});
