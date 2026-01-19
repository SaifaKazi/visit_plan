// // frappe.ui.form.on("Prospect", {
// //     refresh(frm) {
// //         setTimeout(() => {
// //             frm.page.wrapper
// //                 .find('a[data-label="Customer"]')
// //                 .off("click.prospect_check")
// //                 .on("click.prospect_check", function (e) {

// //                     e.preventDefault();
// //                     e.stopImmediatePropagation();

// //                     frappe.call({
// //                         method: "visit_plan.public.py.prospect.check_customer_from_prospect",
// //                         args: {
// //                             prospect_name: frm.doc.name
// //                         },
// //                         callback: function (r) {
// //                             if (r.message && r.message.exists) {
// //                                 frappe.msgprint({
// //                                     title: __("Not Allowed"),
// //                                     message: __("Customer is already created for this Prospect: ") 
// //                                              + "<b>" + r.message.customer + "</b>",
// //                                     indicator: "red"
// //                                 });
// //                             }
// //                             // if NOT exists → do nothing
// //                         }
// //                     });

// //                     return false;
// //                 });
// //         }, 300);
// //     }
// // });


// frappe.ui.form.on("Prospect", {
//     refresh(frm) {
//         setTimeout(() => {
//             const customer_btn = frm.page.wrapper.find(
//                 'a[data-label="Customer"]'
//             );

//             customer_btn.off("click").on("click", function (e) {
//                 e.preventDefault();
//                 e.stopImmediatePropagation();

//                 frappe.call({
//                     method: "visit_plan.public.py.prospect.check_customer_from_prospect",
//                     args: {
//                         prospect_name: frm.doc.name
//                     },
//                     callback(r) {
//                         if (r.message && r.message.exists) {
//                             // ❌ Customer exists → show message only
//                             frappe.msgprint({
//                                 title: __("Not Allowed"),
//                                 message: __("Customer is already created for this Prospect."),
//                                 indicator: "red"
//                             });
//                         } else {
//                             // ✅ Customer not exists → allow normal flow
//                             frappe.set_route(
//                                 "Form",
//                                 "Customer",
//                                 "new-customer",
//                                 {
//                                     from_prospect: frm.doc.name
//                                 }
//                             );
//                         }
//                     }
//                 });

//                 return false;
//             });
//         }, 300);
//     }
// });




// frappe.ui.form.on("Prospect", {
//     refresh(frm) {
//         if (!frm.doc.name) return;

//         frappe.db.exists("Customer", {
//             custom_from_prospect: frm.doc.name
//         }).then(exists => {
//             if (exists) {
//                 frm.remove_custom_button("Customer", "Create");
//             }
//         });
//     }
// });



frappe.ui.form.on("Prospect", {
    refresh(frm) {
        if (!frm.doc.name) return;

        frappe.call({
            method: "visit_plan.public.py.prospect.check_customer_exists",
            args: {
                prospect_name: frm.doc.name
            },
            callback: function(r) {
                if (r.message) {
                    // Customer exists → remove Create button
                    frm.remove_custom_button("Customer", "Create");

                    // Optional: add "View Customer" button
                    frm.add_custom_button("View Customer", () => {
                        frappe.set_route("Form", "Customer", r.message);
                    });
                }
            }
        });
    }
});
