import frappe

@frappe.whitelist()
def custom_get_print_format(doctype, name=None, print_format=None, meta=None):
    frappe.throw("Hii")
    doc = frappe.get_doc(doctype, name)

    if doc.custom_test_group == "vikas":
        return "Sales Invoice"

    if doc.custom_test_group == "sanpra":
        return "Point of Sale"

    return "Other Print Format"
 