##############################################################################
#
#    Copyright (C) 2023  CODIGONYN  (https://www.codigonyn.com.ar)
#    All Rights Reserved.
#
#
##############################################################################
{
    'name': 'AGconstrucciones',
    'version': "1.0.0",
    'category': 'Custom',
    'summary': 'Carga y actualizaciones de Productos creado por Nelson',
    'description': '''
        Este módulo permite la carga de productos nuevos con sus correspondientes descripciones como: 'default_code' (Código), 'barecode' (Código de barras), 'name' (Descripción, nombre del producto), 'list_price_1&2&3&4' (lista de precio 1 , 2, 3, 4), 'supplier_no' (N° Proveedor), 'item' (Rubro), 'vat'(IVA (%)).
        También permite actualizar los productos. Si el producto no existe se crea automáticamente. Si el producto existe, automáticamente actualiza los cambios si los hubiera, generalmente los cambios se realizan en las listas de precios.
        Si el documento tiene una lista de precio que no existe en la base de datos, esta lista no se creará automáticamente. 
        Para realizar cualquier cambio sobre éste módulo o nuevas funcionalidades, deberá ponerse en contacto con el desarrollador (Nelson Ivan Tontarelli, cel: 3462310254, email: nelsonivan003@gmail.com).
        
        --------------------------------
        This module allows the loading of new products with their corresponding descriptions such as: 'default_code' (Code), 'barecode' (Barcode), 'name' (Description, product name), 'list_price_1&2&3&4' (price list 1, 2, 3, 4), 'supplier_no' (Supplier No.), 'item' (Item), 'vat'(VAT (%)).
        It also allows you to update the products. If the product does not exist, it is created automatically. If the product exists, it automatically updates the changes if any, usually the changes are made in the price lists.
        If the document has a price list that does not exist in the database, this list will not be created automatically.
        To make any changes to this module or new features, you must contact the developer (Nelson Ivan Tontarelli, cel: 3462310254, email: nelsonivan003@gmail.com).

    ''',
    'author': 'CODIGONYN',
    'license': 'AGPL-3',
    'website': 'www.agconstrucciones.com.ar',
    'images': [],
    'depends': ['base','product',],
    'data': [
        'views/ag_products_view.xml',
        #'views/menu_items.xml',
        #'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
