import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

HEX_COLOR = re.compile(r'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$')


class LoginBranding(models.Model):
    """Singleton-style configuration for the branded login page.

    A single record holds all the content shown on the login screen. It is
    read (with sudo) by the public login templates, and edited from the
    backend form at Settings > Login Page Design.
    """
    _name = 'login.branding'
    _description = 'Login Page Branding'

    name = fields.Char(default='Login Page', readonly=True)

    # Branded (left) panel
    brand_title = fields.Char(
        string='Headline', required=True, default='Welcome',
        help='Large heading shown on the branded side of the login page.')
    brand_subtitle = fields.Text(
        string='Sub-heading',
        help='Short line of text shown under the headline. Leave empty to hide.')
    logo = fields.Binary(string='Logo', attachment=True)
    show_features = fields.Boolean(string='Show Feature List', default=True)
    feature_ids = fields.One2many(
        'login.branding.feature', 'config_id', string='Feature List')

    # Sign-in (right) panel
    form_heading = fields.Char(
        string='Form Heading',
        help='Optional heading shown above the sign-in form. Leave empty to hide.')

    # Colors (hex)
    gradient_start = fields.Char(string='Gradient Start', default='#0d1b3e')
    gradient_end = fields.Char(string='Gradient End', default='#00aeef')
    primary_color = fields.Char(string='Primary Color', default='#2563eb')

    @api.constrains('gradient_start', 'gradient_end', 'primary_color')
    def _check_colors(self):
        for rec in self:
            for value in (rec.gradient_start, rec.gradient_end, rec.primary_color):
                if value and not HEX_COLOR.match(value.strip()):
                    raise ValidationError(_(
                        'Colors must be valid hex codes such as #2563eb or #fff.'))

    @api.model
    def _get_config(self):
        """Return the singleton config record, creating it if missing."""
        rec = self.sudo().search([], limit=1)
        if not rec:
            rec = self.sudo().create({'brand_title': 'Welcome'})
        return rec

    @api.model
    def action_open_config(self):
        """Open the (single) config record in a form view — used by the menu."""
        rec = self._get_config()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Login Page Design'),
            'res_model': 'login.branding',
            'res_id': rec.id,
            'view_mode': 'form',
            'target': 'current',
        }


class LoginBrandingFeature(models.Model):
    _name = 'login.branding.feature'
    _description = 'Login Page Feature Bullet'
    _order = 'sequence, id'

    sequence = fields.Integer(default=10)
    name = fields.Char(string='Text', required=True)
    config_id = fields.Many2one(
        'login.branding', string='Login Page', required=True, ondelete='cascade')
