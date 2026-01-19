// Copyright (c) 2025, Sanpra Software and contributors
// For license information, please see license.txt

frappe.query_reports["PT Challan"] = {
	"filters": [
		{
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            reqd: 1
        }

	] 
};
 