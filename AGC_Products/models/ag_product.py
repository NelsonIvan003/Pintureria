from odoo import models, fields

print("AGC_Products")


class AGCProducts(models.Model):
    _name = 'ag.product'
    _description = 'AG Productos'

    code = fields.Char(string='Código')
    barcode = fields.Char(string='Código de Barras')
    description = fields.Text(string='Descripción')
    supplier_number = fields.Char(string='N° Proveedor')
    category_id = fields.Many2one('product.category', string='ID Rubro')
    category_name = fields.Char(related='category_id.name', string='Rubro')
    unit = fields.Char(string='Unidad')
    tax = fields.Float(string='IVA (%)')
    price_1 = fields.Float(string='Precio L1')
    price_2 = fields.Float(string='Precio L2')
    price_3 = fields.Float(string='Precio L3')
    price_4 = fields.Float(string='Precio L4')

    def update_prices_from_excel(self):
        # Aquí se implementaría la lógica para procesar el archivo Excel y actualizar los precios de los productos
        # Puedes utilizar librerías como pandas o xlrd para leer el archivo Excel y obtener los datos
        # Luego, puedes comparar los precios con los existentes en la base de datos y actualizarlos según corresponda
        pass

