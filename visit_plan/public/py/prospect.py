# import frappe

# @frappe.whitelist()
# def check_customer_from_prospect(prospect_name):
#     customer = frappe.db.get_value(
#         "Customer",
#         {"custom_from_prospect": prospect_name},
#         "name"
#     )

#     if customer:
#         return {
#             "exists": True,
#             "customer": customer
#         }

#     return {
#         "exists": False
#     }



import frappe
from frappe import _

@frappe.whitelist()
def check_customer_exists(prospect_name):
    """Check if a Customer already exists for this Prospect"""
    customer = frappe.db.get_value("Customer", {"custom_from_prospect": prospect_name}, "name")
    return customer or ""
