# flake8: noqa
# Use <m> or <message> to retrieve the data transmitted by the scanner.
# Use <t> or <terminal> to retrieve the running terminal browse record.
# Put the returned action code in <act>, as a single character.
# Put the returned result or message in <res>, as a list of strings.
# Put the returned value in <val>, as an integer


# Select inventory
terminal.write({'tmp_val2': '', 'tmp_val3': '', 'tmp_val4': ''})
inventories = env['stock.inventory'].search([('state', '=', 'confirm')])
if inventories:
    act = 'L'
    res = []
    for inventory in inventories:
        res.append((inventory.id, inventory.name))
else:
     act = 'A'
