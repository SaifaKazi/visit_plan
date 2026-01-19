import frappe

def validate_item_accounts(doc, method):
    if not doc.is_stock_item and not doc.is_fixed_asset:
        for d in doc.item_defaults:
            if d.expense_account or d.income_account:
                return

        frappe.throw("Set Expense or Income Account")
