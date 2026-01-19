#  import frappe


# def get_columns():
#     return [
#         {"label": "Gender", "fieldname": "gender", "fieldtype": "Data", "width": 150},
#         {"label": "Total Employees", "fieldname": "total_employees", "fieldtype": "Int", "width": 150},
#         {"label": "No of Employees", "fieldname": "employee_count", "fieldtype": "Int", "width": 150},
#         {"label": "Employee Contribution (₹)", "fieldname": "employee_contribution", "fieldtype": "Currency", "width": 180},
#         {"label": "Employer Contribution (₹)", "fieldname": "employer_contribution", "fieldtype": "Currency", "width": 180},
#     ]


# def execute(filters=None):
#     columns = get_columns()
#     data = []

#     result = frappe.db.sql("""
#         SELECT  
#             e.gender, 
#             COUNT(ss.employee) AS employee_count,
#             SUM(ss.gross_pay) AS total_gross
#         FROM `tabSalary Slip` ss
#         INNER JOIN `tabEmployee` e 
#             ON ss.employee = e.name
#         WHERE ss.docstatus = 1
#           AND e.status = 'Active'
#           AND e.custom__is_lwf = 1
#         GROUP BY e.gender
#     """, as_dict=True)

#     total_employees = sum(row.employee_count for row in result)

#     for row in result:
#         employee_contribution = (row.total_gross or 0) * 8.33 / 100
#         employer_contribution = (row.total_gross or 0) * 3.76 / 100

#         data.append({
#             "gender": row.gender,
#             "total_employees": total_employees,
#             "employee_count": row.employee_count,
#             "employee_contribution": employee_contribution,
#             "employer_contribution": employer_contribution
#         })

#     return columns, data


import frappe
from frappe.utils import getdate


def get_columns():
    return [
        {"label": "Gender", "fieldname": "gender", "fieldtype": "Data", "width": 120},
        {"label": "Total Employees", "fieldname": "total_employees", "fieldtype": "Int", "width": 150},
        {"label": "No of Employees", "fieldname": "employee_count", "fieldtype": "Int", "width": 150},
        {"label": "Employee Contribution (₹)", "fieldname": "employee_contribution", "fieldtype": "Currency", "width": 180},
        {"label": "Employer Contribution (₹)", "fieldname": "employer_contribution", "fieldtype": "Currency", "width": 180},
        {"label": "Total Contribution (₹)", "fieldname": "total_contribution", "fieldtype": "Currency", "width": 180},
    ]


def execute(filters=None):
    columns = get_columns()
    data = []

    if not filters or not filters.get("from_date") or not filters.get("to_date"):
        return columns, data

    from_date = getdate(filters.get("from_date"))
    to_date = getdate(filters.get("to_date"))

    # Extract month from selected date range
    selected_month = from_date.month

    # Only allow June (6) or December (12)
    if selected_month not in (6, 12):
        # Return ZERO rows
        data.append({
            "gender": "All",
            "total_employees": 0,
            "employee_count": 0,
            "employee_contribution": 0,
            "employer_contribution": 0,
            "total_contribution": 0
        })
        return columns, data

    result = frappe.db.sql("""
        SELECT  
            e.gender,
            COUNT(DISTINCT ss.employee) AS employee_count
        FROM `tabSalary Slip` ss
        INNER JOIN `tabEmployee` e 
            ON ss.employee = e.name
        WHERE ss.docstatus = 1
          AND e.status = 'Active'
          AND e.custom__is_lwf = 1
          AND ss.posting_date BETWEEN %(from_date)s AND %(to_date)s
          AND MONTH(ss.posting_date) = %(month)s
        GROUP BY e.gender
    """, {
        "from_date": from_date,
        "to_date": to_date,
        "month": selected_month
    }, as_dict=True)

    total_employees = sum(row.employee_count for row in result)

    for row in result:
        employee_contribution = row.employee_count * 25
        employer_contribution = row.employee_count * 75

        data.append({
            "gender": row.gender,
            "total_employees": total_employees,
            "employee_count": row.employee_count,
            "employee_contribution": employee_contribution,
            "employer_contribution": employer_contribution,
            "total_contribution": employee_contribution + employer_contribution
        })

    return columns, data
