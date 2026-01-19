import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {
            "label": "Employee ID",
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 120,
        },
        {
            "label": "Employee Name",
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": "Gross Salary",
            "fieldname": "gross_pay",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": "PT Slab",
            "fieldname": "pt_slab",
            "fieldtype": "Currency",
            "width": 150,
        },
        {
            "label": "Professional Tax Amount",
            "fieldname": "pt_amount",
            "fieldtype": "Currency",
            "width": 160, 
        },
    ]


def get_data(filters):
    data = []

    if not filters.get("from_date") or not filters.get("to_date"):
        frappe.throw("Please select From Date and To Date")

    salary_slips = frappe.get_all(
        "Salary Slip",
        filters={
            "docstatus": 1,
            "gross_pay": [">", 7501],
            "posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
        },
        fields=[
            "name",
            "employee",
            "employee_name",
            "gross_pay",
        ],
        order_by="posting_date asc",
    )

    for slip in salary_slips:
        pt_deduction = frappe.get_all(
            "Salary Detail",
            filters={
                "parent": slip.name,
                "parenttype": "Salary Slip",
                "salary_component": "Professional Tax",
            },
            fields=["salary_component", "amount"],
            limit=1,
        )

        if pt_deduction:
            data.append({
                "employee": slip.employee,
                "employee_name": slip.employee_name,
                "gross_pay": slip.gross_pay,
                "pt_slab": pt_deduction[0].amount,   # keeping as you requested
                "pt_amount": pt_deduction[0].amount,
            })

    return data
