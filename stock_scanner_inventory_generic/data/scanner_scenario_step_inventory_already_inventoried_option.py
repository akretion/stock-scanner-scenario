# flake8: noqa
# Use <m> or <message> to retrieve the data transmitted by the scanner.
# Use <t> or <terminal> to retrieve the running terminal browse record.
# Put the returned action code in <act>, as a single character.
# Put the returned result or message in <res>, as a list of strings.
# Put the returned value in <val>, as an integer

terminal.write({'tmp_val5': ''})
product = env['product.product'].browse(int(terminal.tmp_val2))
inv_line = env['stock.inventory.line'].browse(int(terminal.tmp_val3))

res = [
    _('Product: %s') % (product.display_name),
    ]
if product.uom_id == env.ref('product.product_uom_unit'):
    qty_int = True
else:
    qty_int = False
    res.append(_('UNIT OF MEASURE: %s') % product.uom_id.name)
theoric_qty_display = qty_int and int(inv_line.theoretical_qty) or inv_line.theoretical_qty
res.append(_('Theoric qty: %s') % theoric_qty_display)
cur_qty_display = qty_int and int(inv_line.product_qty) or inv_line.product_qty
res.append(_('QTY ALREADY INVENTORIED: %s') % cur_qty_display)

#act = 'C'
#res += [
#    '',
#    (_('Do you want to ADD to the already inventoried qty?')),
#    '',
#    (_('If you answer no, you will enter a new inventory qty.')),
#    ]
act = 'L'
res = [
    ('add', 'Add to already inventoried qty'),
    ('rewrite', 'Enter new inventoried qty'),
    ]
