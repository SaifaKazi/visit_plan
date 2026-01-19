app_name = "visit_plan"
app_title = "Visit Plan"
app_publisher = "Sanpra Software"
app_description = "Book Visit Plan"
app_email = "contact@sanpra.co.in"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "visit_plan",
# 		"logo": "/assets/visit_plan/logo.png",
# 		"title": "Visit Plan",
# 		"route": "/visit_plan",
# 		"has_permission": "visit_plan.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/visit_plan/css/visit_plan.css"
# app_include_js = "/assets/visit_plan/js/visit_plan.js"

# include js, css files in header of web template
# web_include_css = "/assets/visit_plan/css/visit_plan.css"
# web_include_js = "/assets/visit_plan/js/visit_plan.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "visit_plan/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "visit_plan/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "visit_plan.utils.jinja_methods",
# 	"filters": "visit_plan.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "visit_plan.install.before_install"
# after_install = "visit_plan.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "visit_plan.uninstall.before_uninstall"
# after_uninstall = "visit_plan.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "visit_plan.utils.before_app_install"
# after_app_install = "visit_plan.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "visit_plan.utils.before_app_uninstall"
# after_app_uninstall = "visit_plan.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "visit_plan.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {  
   "Sales Invoice": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Sales Order": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Delivery Note": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Purchase Order": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Purchase Receipt": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Purchase Invoice": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    },
    "Payment Entry": {
        "before_save": "visit_plan.public.py.cost_center.set_cost_center"
    }
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"visit_plan.tasks.all"
# 	],
# 	"daily": [
# 		"visit_plan.tasks.daily"
# 	],
# 	"hourly": [
# 		"visit_plan.tasks.hourly"
# 	],
# 	"weekly": [
# 		"visit_plan.tasks.weekly"
# 	],
# 	"monthly": [
# 		"visit_plan.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "visit_plan.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "visit_plan.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "visit_plan.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["visit_plan.utils.before_request"]
# after_request = ["visit_plan.utils.after_request"]

# Job Events
# ----------
# before_job = ["visit_plan.utils.before_job"]
# after_job = ["visit_plan.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"visit_plan.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

