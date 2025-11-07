import frappe

@frappe.whitelist()
def set_cost_center(doc, method=None):
    if not doc.cost_center:
        return
    for item in doc.items:
        item.cost_center = doc.cost_center
    for tax in doc.taxes:
        tax.cost_center = doc.cost_center