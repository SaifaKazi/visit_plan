# import frappe

# @frappe.whitelist()
# def set_cost_center(doc, method=None):
#     if not doc.cost_center:
#         return

#     if hasattr(doc, "items"):
#         for item in doc.items:
#             if hasattr(item, "cost_center"):
#                 item.cost_center = doc.cost_center

#     if hasattr(doc, "taxes"):
#         for tax in doc.taxes:
#             if hasattr(tax, "cost_center"):
#                 tax.cost_center = doc.cost_center
import frappe

@frappe.whitelist()
def set_cost_center(doc, method=None):

    if hasattr(doc, "items"):
        for item in doc.items:
            if hasattr(item, "cost_center"):
                item.cost_center = doc.cost_center or None

    if hasattr(doc, "taxes"):
        for tax in doc.taxes:
            if hasattr(tax, "cost_center"):
                tax.cost_center = doc.cost_center or None
