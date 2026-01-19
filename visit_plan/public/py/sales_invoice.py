import frappe
from frappe.utils.pdf import get_pdf
from frappe.core.doctype.communication.email import make

def send_invoice_email(doc, method):
    pass

    # # 1️⃣ Generate Sales Invoice PDF
    # html = frappe.get_print("Sales Invoice", doc.name, print_format="Sales Invoice")
    # sales_invoice_pdf = get_pdf(html)

    # attachments = [
    #     {
    #         "fname": f"{doc.name}.pdf",
    #         "fcontent": sales_invoice_pdf
    #     }
    # ]

    # # 2️⃣ Attach Item-wise custom PDF
    # for row in doc.items: 
    #     if row.item_code:
    #         custom_file = frappe.db.get_value("Item", row.item_code, "custom_attch")

    #         if custom_file:
    #             try:
    #                 file_doc = frappe.get_doc("File", {"file_url": custom_file})
    #                 file_content = file_doc.get_content()

    #                 attachments.append({
    #                     "fname": file_doc.file_name,
    #                     "fcontent": file_content
    #                 })

    #             except Exception as e:
    #                 frappe.log_error(f"Could not attach file for item {row.item_code}: {e}")

    # # 3️⃣ Recipient Email
    # recipient_email = doc.contact_email or doc.customer_email_id or None
    # if not recipient_email:
    #     frappe.log_error("Sales Invoice Email Failed: No Email in Customer or Contact")
    #     return

    # # 4️⃣ Build Custom HTML Body (Replace variables)
    # customer_person = doc.contact_person or doc.customer or "Customer"

    # email_html = f"""
    # <!DOCTYPE html>
    # <html>
    # <head>
    #     <title>New Sales Invoice Raised</title>
    # </head>
    # <body>
    #     <p>Dear {customer_person},</p>
    #     <p>Your Sales Invoice has been created. 
    #     Please check the attached PDF for full details.</p>
    
    #     <p>Thank you.</p>
    # </body>
    # </html>
    # """

    # # 5️⃣ Send Email
    # make(
    #     recipients=[recipient_email],
    #     subject=f"Sales Invoice {doc.name}",
    #     content=email_html,
    #     attachments=attachments,
    #     send_email=True,
    #     is_html=True
    # )
