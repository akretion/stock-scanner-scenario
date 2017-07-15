# flake8: noqa
# Use <m> or <message> to retrieve the data transmitted by the scanner.
# Use <t> or <terminal> to retrieve the running terminal browse record.
# Put the returned action code in <act>, as a single character.
# Put the returned result or message in <res>, as a list of strings.
# Put the returned value in <val>, as an integer

from openerp.tools import float_is_zero

if tracer == 'already':
    if message:
        question = _('Inventory quantity to add:')
        already_option = 'add'
    else:
        question = _('New inventory quantity:')
        already_option = 'rewrite'
    product = env['product.product'].browse(int(terminal.tmp_val2))
    terminal.write({'tmp_val4': already_option})
else:
    product_code = message
    question = _('Inventory quantity:')
    product = model.search(['|', ('default_code', '=', product_code), ('ean13', '=', product_code)])[0]
    terminal.write({'tmp_val2': product.id})

res = [
    _('Product: %s') % (product.display_name),
    ]
if product.uom_id == env.ref('product.product_uom_unit'):
    qty_int = True
else:
    qty_int = False
    res.append(_('UNIT OF MEASURE: %s') % product.uom_id.name)
silo = env['stock.inventory.line']
if terminal.tmp_val3:
    inv_line = silo.browse(int(terminal.tmp_val3))
else:
    lines = silo.search(
        [('inventory_id', '=', int(terminal.tmp_val1)), ('product_id', '=', product.id)])
    inv_line = lines and lines[0] or False
    if inv_line:
        terminal.write({'tmp_val3': inv_line.id})

act = 'Q'
if inv_line:
    theoric_qty_display = qty_int and int(inv_line.theoretical_qty) or inv_line.theoretical_qty
    res.append(_('Theoric qty: %s') % theoric_qty_display)
    prec = env['decimal.precision'].precision_get('Product Unit of Measure')
    if not float_is_zero(inv_line.product_qty, precision_digits=prec):
        cur_qty_display = qty_int and int(inv_line.product_qty) or inv_line.product_qty
        res.append(_('QTY ALREADY INVENTORIED: %s') % cur_qty_display)
        if tracer != 'already':
            act = 'A'
            terminal.write({'tmp_val5': 'already'})
else:
    res.append(_('PRODUCT WAS NOT ON INVENTORY LINES!'))

res += ['', question]
