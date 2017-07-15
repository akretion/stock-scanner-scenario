# flake8: noqa
# Use <m> or <message> to retrieve the data transmitted by the scanner.
# Use <t> or <terminal> to retrieve the running terminal browse record.
# Put the returned action code in <act>, as a single character.
# Put the returned result or message in <res>, as a list of strings.
# Put the returned value in <val>, as an integer


# Select inventory
sio = env['stock.inventory']
inventories = sio.search([('state', '=', 'confirm')])
if not inventories:
     print "no inventory found"  # TODO
result = []
for inventory in inventories:
    result.append((inventory.id, inventory.name))

terminal.write({'tmp_val2': '', 'tmp_val3': ''})

act = 'L'
res = result
