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
            "label": "Supplier",
            "fieldname": "supplier",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Purchase Invoice Date",
            "fieldname": "purchase_invoice_date",
            "fieldtype": "Date",
            "width": 150
        },
        {
            "label": "Purchase Invoice",
            "fieldname": "purchase_invoice",
            "fieldtype": "Link",
            "options": "Purchase Invoice",
            "width": 150
        },
        {
            "label": "Purchase Invoice Total Amt",
            "fieldname": "pi_total",
            "fieldtype": "Currency",
            "width": 200
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
            "label": "Outstanding Amount",
            "fieldname": "outstanding_amount",
            "fieldtype": "Currency",
            "width": 150
        }
    ]


def get_data(filters=None):
    rows = []
    filters = filters or {}
    invoice_filters = {"docstatus": 1}

    # Date filter
    if filters.get("from_date") and filters.get("to_date"):
        invoice_filters["posting_date"] = [
            "between",
            [filters.get("from_date"), filters.get("to_date")]
        ]

    # Supplier filter
    if filters.get("party"):
        invoice_filters["supplier"] = filters.get("party")

    # Fetch Purchase Invoices
    purchase_invoices = frappe.get_all(
        "Purchase Invoice",
        filters=invoice_filters,
        fields=["name", "supplier", "posting_date", "rounded_total"],
        order_by="posting_date asc"
    )

    for pi in purchase_invoices:
        payment_refs = frappe.get_all(
            "Payment Entry Reference",
            filters={
                "reference_doctype": "Purchase Invoice",
                "reference_name": pi.name
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
                "supplier": pi.supplier if is_first else "",
                "purchase_invoice_date": pi.posting_date if is_first else "",
                "purchase_invoice": pi.name if is_first else "",
                "payment_entry": pe.name,
                "posting_date": pe.posting_date,
                "paid_amount": ref.allocated_amount if ref else 0,
                "outstanding_amount": ref.outstanding_amount if ref else 0,
                "pi_total": pi.rounded_total if is_first else 0,
            })

    return rows
