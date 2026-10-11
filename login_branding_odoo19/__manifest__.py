{
    'name': 'Login Page Branding',
    'version': '19.0.1.1.0',
    'category': 'Website',
    'summary': 'Customizable split-screen login page, edited from the Odoo backend',
    'description': """
Login Page Branding
===================

Replaces the standard Odoo login screen with a modern split-screen design:
a branded panel on the left, the sign-in form on the right.

Everything on the branded panel — headline, sub-heading, feature bullets,
logo and colors — is stored in a record and edited from a backend form
(Settings > Login Page Design). No code editing required.

Self-contained: depends only on `web`, so it can be dropped into any Odoo 19
database and installed as-is.
""",
    'author': 'Mohamed Medhat',
    'license': 'LGPL-3',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'data/login_branding_data.xml',
        'views/login_branding_views.xml',
        'views/login_templates.xml',
        'views/favicon_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'login_branding/static/src/css/login.css',
            'login_branding/static/src/js/login.js',
        ],
    },
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
