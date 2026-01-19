import frappe

def validate_cost_center_balance(doc, method):
    cc_total = {}

    for row in doc.accounts:
        if not row.cost_center:
            continue

        cc_total[row.cost_center] = cc_total.get(row.cost_center, 0) + \
            row.debit_in_account_currency - row.credit_in_account_currency

    for cc in cc_total:
        if round(cc_total[cc], 2) != 0:
            frappe.throw("Debit & Credit mismatch for " + cc)
