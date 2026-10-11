# Login Page Branding

A modern split-screen login page for **Odoo 18**, fully editable from the backend — no code changes needed to rebrand it.

- **Left panel:** logo, headline, sub-heading and a feature list on a gradient background.
- **Right panel:** the sign-in form, with a show/hide password toggle.
- **Everything is configurable** at *Settings > Login Page Design*: texts, logo, feature bullets and three colors.
- **Self-contained:** depends only on `web`. Drop it into any Odoo 18 database and install.
- **Safe by design:** colors are validated as hex codes, and the page reads its content through a single sudo-ed config record, so the public login screen never needs broader access.
- **Compatible with `website`:** the layout view is registered at a priority that always wins over the one `website` ships, so the design survives whether or not `website` is installed.

## Installation

1. Copy the `login_branding` folder into your Odoo addons path.
2. Restart Odoo and update the apps list (Apps > Update Apps List).
3. Install **Login Page Branding**.
4. Open *Settings > Login Page Design* (administrators only) and make it yours.

## Customizing

| Setting | What it does |
| --- | --- |
| Logo | Shown on both panels. Falls back to the bundled placeholder if empty. |
| Headline / Sub-heading | Text on the branded panel. Leave the sub-heading empty to hide it. |
| Feature list | Bullet points with a check icon. Drag to reorder, or switch the list off entirely. |
| Form heading | Optional title above the sign-in form. |
| Gradient start / end | Background gradient of the branded panel. |
| Primary color | Buttons, focus ring, links and bullet icons. |

The bundled logo and icon are neutral placeholders; replace `static/src/img/logo.png` and `static/description/icon.png`, or simply upload your own logo from the settings form.

The module also uses its logo as the browser-tab icon on all pages (`views/favicon_templates.xml`). Delete that file from the manifest's `data` list if you don't want that behavior.

## Compatibility

Odoo 18.0 (Community and Enterprise).

## License

LGPL-3
