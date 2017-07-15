# flake8: noqa
# Use <m> or <message> to retrieve the data transmitted by the scanner.
# Use <t> or <terminal> to retrieve the running terminal browse record.
# Put the returned action code in <act>, as a single character.
# Put the returned result or message in <res>, as a list of strings.
# Put the returned value in <val>, as an integer

from openerp.tools import float_compare


# No current inventory, create a new one
silo = env['stock.inventory.line']
sio = env['stock.inventory']
ppo = env['product.product']
res = []
if tracer == 'inventory':
    # Write inventory ID in tmp_val1
    terminal.write({'tmp_val1': message})
elif tracer == 'product' and terminal.tmp_val2:
    inv = sio.browse(int(terminal.tmp_val1))
    product = ppo.browse(int(terminal.tmp_val2))
    quantity = float(message)
    res.append(_("Product: %s") % product.display_name)
    if product.uom_id == env.ref('product.product_uom_unit'):
        qty_int = True
    else:
        qty_int = False
        res.append(_('UNIT OF MEASURE: %s') % product.uom_id.name)
    if terminal.tmp_val3:
        inv_line = silo.browse(int(terminal.tmp_val3))
        if inv_line.product_id != product:
            res.append(_(
                "ERROR: Product on inventory line ID %d is not %s") % (inv_line.id, product.display_name))
        if inv_line.location_id != inv.location_id:
            res.append(_(
                "ERROR: Location on inventory line ID %s is not %s") % (inv_line.id, inv.location_id.display_name))
        inv_line.product_qty = quantity
        theoric_qty = inv_line.theoretical_qty
    else:
        silo.create({
            'inventory_id': inv.id,
            'product_id': product.id,
            'product_uom_id': product.uom_id.id,
            'product_qty': quantity,
            'location_id': inv.location_id.id,
        })
        theoric_qty = 0

    theoric_qty_display = qty_int and int(theoric_qty) or theoric_qty
    qty_display = qty_int and int(quantity) or quantity
    res += [
        _("Theoric qty: %s") % theoric_qty_display,
        _("Inventoried qty: %s") % qty_display,
        ]
    prec = env['decimal.precision'].precision_get('Product Unit of Measure')
    variation_float_compare = float_compare(
        quantity, theoric_qty, precision_digits=prec)
    if variation_float_compare:
        variation = quantity - theoric_qty
        variation_display = qty_int and int(variation) or variation
        variation_display = unicode(variation_display)
        if variation_float_compare > 0:
            variation_display = '+%s' % variation_display

        res.append(_("STOCK LEVEL VARIATION: %s") % variation_display)
    else:
        res.append(_('NO STOCK LEVEL VARIATION'))

    terminal.write({'tmp_val2': '', 'tmp_val3': ''})

act = 'T'
res += [
    '',
    _('Enter new product code:'),
]
