from odoo import models, fields

class ResPartner(models.Model)
    _inherit = 'res.partner'

    nivel_cliente = fields.Selection(
        [
            ('bajo', 'Bajo'),
            ('medio', 'Medio'),
            ('alto', 'Alto')
        ],
        string='Nivel de cliente'
    )