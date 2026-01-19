import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    if not filters.get("from_date") or not filters.get("to_date"):
        frappe.throw("Please select From Date and To Date")

    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"label": "Employee ID", "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 120},
        {"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 180},
        {"label": "Provident Fund Account", "fieldname": "provident_fund_account", "fieldtype": "Data", "width": 200},
        {"label": "PF Wages", "fieldname": "pf_wages", "fieldtype": "Currency", "width": 120},
        {"label": "Employee EPF 12%", "fieldname": "employee_epf", "fieldtype": "Currency", "width": 140},
        {"label": "Employer EPF 3.67%", "fieldname": "employer_epf", "fieldtype": "Currency", "width": 160},
        {"label": "Employer EPS 8.33%", "fieldname": "employer_eps", "fieldtype": "Currency", "width": 160},
        {"label": "EDLI 0.5%", "fieldname": "edli", "fieldtype": "Currency", "width": 100},
        {"label": "Total", "fieldname": "total", "fieldtype": "Currency", "width": 100},
    ]


def get_data(filters):
    salary_slips = frappe.db.sql("""
        SELECT
            ss.name AS salary_slip,
            ss.employee,
            ss.employee_name,
            ss.gross_pay,
            emp.provident_fund_account
        FROM `tabSalary Slip` ss
        LEFT JOIN `tabEmployee` emp ON emp.name = ss.employee
        WHERE ss.docstatus = 1
        AND ss.start_date >= %(from_date)s
        AND ss.end_date <= %(to_date)s
        AND ss.gross_pay > 15000
    """, filters, as_dict=True)

    data = []

    for ss in salary_slips:
        earnings = frappe.db.sql("""
            SELECT salary_component, amount 
            FROM `tabSalary Detail`
            WHERE parent = %s
            AND parenttype = 'Salary Slip'
            AND parentfield = 'earnings'
        """, ss.salary_slip, as_dict=True)

        basic = hra = da = 0

        for e in earnings:
            if e.salary_component == "Basic":
                basic += e.amount
            elif e.salary_component == "HRA":
                hra += e.amount
            elif e.salary_component == "DA":
                da += e.amount
 
        pf_wages = basic + hra + da

        employee_epf = round(pf_wages * 0.12, 2)
        employer_epf = round(pf_wages * 0.0367, 2)
        employer_eps = round(pf_wages * 0.0833, 2)
        edli_cal = round(pf_wages * 0.005, 2)

        data.append({
            "employee": ss.employee,
            "employee_name": ss.employee_name,
            "provident_fund_account": ss.provident_fund_account,
            "pf_wages": pf_wages,
            "employee_epf": employee_epf,
            "employer_epf": employer_epf,
            "employer_eps": employer_eps,
            "edli": edli_cal,
            "total": employee_epf + employer_epf + employer_eps + edli_cal
        })

    return data
