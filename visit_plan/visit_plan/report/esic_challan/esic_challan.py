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
            "label": "ESIC No",
            "fieldname": "esic_id",
            "fieldtype": "Data",
            "width": 100,
        },
        {
            "label": "Employee Name",
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 180,
        },
        {
            "label": "No of Days Worked",
            "fieldname": "payment_days",
            "fieldtype": "Float",
            "width": 120,
        },
        {
            "label": "Gross Salary",
            "fieldname": "gross_pay",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "label": "Employee Contribution (0.75%)",
            "fieldname": "employee_contribution",
            "fieldtype": "Currency",
            "width": 180,
        },
        {
            "label": "Employer Contribution (3.25%)",
            "fieldname": "employer_contribution",
            "fieldtype": "Currency",
            "width": 190,
        },
        {
            "label": "Total Contribution",
            "fieldname": "total_contribution",
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
            "gross_pay": ["<", 21000],
            "posting_date": ["between", [filters.get("from_date"), filters.get("to_date")]],
        },
        fields=[
            "employee",
            "employee_name",
            "gross_pay",
            "payment_days",
        ], 
        order_by="posting_date asc",
    )

    
    for slip in salary_slips:
        employee_contribution = round(slip.gross_pay * 0.0075, 2)
        employer_contribution = round(slip.gross_pay * 0.0325, 2)
        total_contribution = round(employee_contribution + employer_contribution, 2)

        esic_id = frappe.get_value("Employee", {"name": slip.employee}, "custom_esic_id")
        
        data.append({
            "employee": slip.employee,
            "employee_name": slip.employee_name,
            "payment_days": slip.payment_days,
            "gross_pay": slip.gross_pay,
            "employee_contribution": employee_contribution,
            "employer_contribution": employer_contribution,
            "total_contribution": total_contribution,
            "esic_id": esic_id,
        })

    return data
