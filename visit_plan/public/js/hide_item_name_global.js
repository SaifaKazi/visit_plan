// frappe.ui.form.on('Sales Order', {
//     refresh(frm) {
//         const can_see_item = frappe.user.has_role("Show Item Name");

//         // Toggle item column visibility
//         frm.fields_dict.items.grid.toggle_display(
//             "item_name",
//             can_see_item
//         );
//     },

//     onload_post_render(frm) {
//         const can_see_item = frappe.user.has_role("Show Item Name");

//         frm.fields_dict.items.grid.toggle_display(
//             "item_name",
//             can_see_item
//         );
//     }
// });


frappe.ui.form.on('*', {
    refresh(frm) {
        handle_item_name_visibility();
    },
    onload_post_render(frm) {
        handle_item_name_visibility();
    }
});

function handle_item_name_visibility() {
    if (frappe.user.has_role("Show Item Name")) return;

    // Delay to allow grids to render
    setTimeout(() => {
        // This targets item display text inside grid rows
        document.querySelectorAll('.grid-row .ellipsis').forEach(el => {
            let lines = el.innerText.split('\n');

            if (lines.length > 1) {
                el.innerText = lines[0]; // Keep item_code only
            }
        });
    }, 300);
}
