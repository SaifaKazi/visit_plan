# # your_app/api/file_preview.py

# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_file_for_webform(docname):
#     if not docname:
#         return None

#     doc = frappe.get_doc("Test Web Form", docname)

#     if not doc.attach_oygq:
#         return None

#     return {
#         "file_url": doc.attach_oygq,
#         "is_private": frappe.db.get_value(
#             "File",  
#             {"file_url": doc.attach_oygq},
#             "is_private"
#         )
#     }




# <div id="file-preview"></div>

# frappe.web_form.on('after_load', function () {
#     load_link_list();
# });

# // 🔹 Load clickable link list
# function load_link_list() {
#     frappe.call({
#         method: "visit_plan.api.file_preview.get_link_list",
#         callback: function (r) {

#             if (!r.message || r.message.length === 0) {
#                 $('#link-list').html('<p>No records found</p>');
#                 return;
#             }

#             let html = `<ul style="list-style:none;padding:0;">`;

#             r.message.forEach(row => {
#                 html += `
#                     <li style="margin-bottom:8px;">
#                         <a href="javascript:void(0)"
#                            onclick="preview_file('${row.name}')"
#                            style="color:#007bff;text-decoration:underline;">
#                            ${row.name}
#                         </a>
#                     </li>
#                 `;
#             });

#             html += `</ul>`;

#             // Inject into HTML field
#             frappe.web_form.set_value(
#                 'link_list_html',
#                 `<div id="link-list">${html}</div>`
#             );
#         }
#     });
# }


# // 🔹 Preview file on click
# function preview_file(docname) {

#     frappe.call({
#         method: "visit_plan.api.file_preview.get_file_for_webform",
#         args: { docname },
#         callback: function (r) {

#             if (!r.message || !r.message.file_url) {
#                 $('#file-preview').html('<p>No file uploaded</p>');
#                 return;
#             }

#             let file_url = r.message.file_url;
#             let full_url = window.location.origin + file_url;
#             let ext = file_url.split('.').pop().toLowerCase();
#             let html = '';

#             // 🖼 IMAGES
#             if (['jpg','jpeg','png','gif','webp','svg'].includes(ext)) {
#                 html = `<img src="${file_url}" style="max-width:100%;border:1px solid #ddd;">`;
#             }

#             // 📄 PDF
#             else if (ext === 'pdf') {
#                 html = `
#                     <iframe src="${file_url}" width="100%" height="600"></iframe>
#                 `;
#             }

#             // 📊 OFFICE FILES (PUBLIC)
#             else if (['xls','xlsx','doc','docx','ppt','pptx'].includes(ext)) {
#                 let office =
#                     `https://view.officeapps.live.com/op/embed.aspx?src=${encodeURIComponent(full_url)}`;
#                 html = `
#                     <iframe src="${office}" width="100%" height="600"></iframe>
#                 `;
#             }

#             // 📄 TEXT / CSV / JSON
#             else if (['txt','csv','log','json','xml'].includes(ext)) {
#                 html = `<iframe src="${file_url}" width="100%" height="400"></iframe>`;
#             }

#             // ⬇ FALLBACK
#             else {
#                 html = `
#                     <a href="${file_url}" target="_blank">Download File</a>
#                 `;
#             }

#             frappe.web_form.set_value(
#                 'file_preview',
#                 `<div id="file-preview">${html}</div>`
#             );
#         }
#     });
# }

import frappe

@frappe.whitelist(allow_guest=True)
def get_file_for_webform(docname):
    if not docname:
        return {}

    # ignore permissions intentionally
    doc = frappe.get_doc("Test Web Form", docname)

    if not doc.attach_oygq:
        return {}

    return {
        "file_url": doc.attach_oygq
    }



# import frappe

# @frappe.whitelist(allow_guest=True)
# def get_records():
#     # return last 10 records
#     return frappe.get_all(
#         "Test Web Form",
#         fields=["name"],
#         limit_page_length=10,
#         order_by="creation desc"
#     )

# @frappe.whitelist(allow_guest=True)
# def get_file(docname):
#     if not docname:
#         return {}

#     doc = frappe.get_doc("Test Web Form", docname)

#     if not doc.attach_oygq:
#         return {}

#     return {
#         "file_url": doc.attach_oygq
#     }
