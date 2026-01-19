# Copyright (c) 2026, Sanpra Software and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": "Customer",
            "fieldname" : "customer",
            "fieldtype" : "Data",
            "width" :150
        },
        {
            "label": "Sales Invoice Date",
            "fieldname": "sales_invoice_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": "Sales Invoice",
            "fieldname": "sales_invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 150
        },
        {
            "label": "Sales Invoice Total Amt",
            "fieldname": "total",
            "fieldtype": "Currency",
            "width": 180
        },
        {
            "label": "Payment Date",
            "fieldname": "posting_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": "Payment Entry",
            "fieldname": "payment_entry",
            "fieldtype": "Link",
            "options": "Payment Entry",
            "width": 150
        },
        {
            "label": "Paid Amount",
            "fieldname": "paid_amount",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label" : "Outstanding Amount",
            "fieldname" : "outstanding_amount",
            "fieldtype" : "Currency",
            "width" : 150
        }
    ]

def get_data(filters=None):
    rows = []
    filters = filters or {}
    invoice_filters = {"docstatus": 1}

    # 🔹 Posting Date filter (From Date – To Date)
    if filters.get("from_date") and filters.get("to_date"):
        invoice_filters["posting_date"] = [
            "between",
            [filters.get("from_date"), filters.get("to_date")]
        ]
    # 🔹 Customer filter
    if filters.get("party"):
        invoice_filters["customer"] = filters.get("party")
    # 🔹 Fetch Sales Invoices (posting_date wise)
    sales_invoices = frappe.get_all(
        "Sales Invoice",
        filters=invoice_filters,
        fields=["name", "customer", "posting_date","total"],
        order_by="posting_date asc"
    )
    for si in sales_invoices:
        payment_refs = frappe.get_all(
            "Payment Entry Reference",
            filters={
                "reference_doctype": "Sales Invoice",
                "reference_name": si.name
            },
            fields=["parent", "allocated_amount", "outstanding_amount"]
        )
        if not payment_refs:
            continue
        payment_entries = frappe.get_all(
            "Payment Entry",
            filters={
                "name": ["in", [ref.parent for ref in payment_refs]],
                "docstatus": 1
            },
            fields=["name", "posting_date"],
            order_by="posting_date asc"
        )
        ref_map = {ref.parent: ref for ref in payment_refs}

        for i, pe in enumerate(payment_entries):
            is_first = (i == 0)
            ref = ref_map.get(pe.name)

            rows.append({
                "customer": si.customer if is_first else "",
                "sales_invoice_date": si.posting_date if is_first else "",
                "sales_invoice": si.name if is_first else "",
                "payment_entry": pe.name,
                "posting_date": pe.posting_date,
                "paid_amount": ref.allocated_amount if ref else 0,
                "outstanding_amount": ref.outstanding_amount if ref else 0,
                "total": si.total if is_first else 0,  

            })
    return rows
