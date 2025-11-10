import frappe

# @frappe.whitelist()
# def set_cost_center(doc, method=None):
#     frappe.msgprint("Setting cost center for Sales Order")
#     if not doc.cost_center:
#         return
#     for item in doc.items:
#         item.cost_center = doc.cost_center
#     for tax in doc.taxes:
#         tax.cost_center = doc.cost_center

# @frappe.whitelist()
# def set_cost_center(doc, method=None):
#     if not doc.cost_center:
#         return
#     for item in doc.items:
#         if hasattr(item, "cost_center"):
#             item.cost_center = doc.cost_center
#             frappe.msgprint("hi")
#     for tax in doc.taxes:
#         if hasattr(tax, "cost_center"):
#             tax.cost_center = doc.cost_center

@frappe.whitelist()
def set_cost_center(doc, method=None):
    if not doc.cost_center:
        return

    if hasattr(doc, "items"):
        for item in doc.items:
            if hasattr(item, "cost_center"):
                item.cost_center = doc.cost_center
                frappe.msgprint("Cost Center set for Item")

    if hasattr(doc, "taxes"):
        for tax in doc.taxes:
            if hasattr(tax, "cost_center"):
                tax.cost_center = doc.cost_center
                frappe.msgprint("Cost Center set for Tax")
