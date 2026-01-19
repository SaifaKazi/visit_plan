// Copyright (c) 2026, Sanpra Software and contributors
// For license information, please see license.txt

frappe.query_reports["Payment Entry Report"] = {
    "filters": [
        {
            "label": "From Date",
            "fieldname": "from_date",
            "fieldtype": "Date",
        },
        {
            "label": "To Date",
            "fieldname": "to_date",
            "fieldtype": "Date",
        },
        {
            "fieldname": "party",
            "label": "Customer",
            "fieldtype": "Link",
            "options": "Customer"
        }
    ]
};
