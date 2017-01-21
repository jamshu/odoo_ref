raw_data=[[0,0,
              {'account_id': 478,
               'credit': 35.0,
               'debit': 0.0,
               'name': u'Bill of Entry Charges- 1010873428316',
               'partner_id': 11729,
               'product_id': 3962}],
             [0,
              0,
              {'account_id': 451,
               'credit': 227.0,
               'debit': 0.0,
               'name': u'Delivery Order Charges - 6254427',
               'partner_id': 6076,
               'product_id': 3964}],
             [0,
              0,
              {'account_id': 696,
               'debit': 35.0,
               'name': u'302101002 - Bill of Entry Charges- 1010873428316',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 251.13}],
             [0,
              0,
              {'account_id': 308,
               'debit': 32.044240035041604,
               'name': u'302101002 - Bill of Entry Charges- 1010873428316: 229.922 already out',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 229.92199999999997}],
             [0,
              0,
              {'account_id': 696,
               'credit': 32.044240035041604,
               'name': u'302101002 - Bill of Entry Charges- 1010873428316: 229.922 already out',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 229.92199999999997}],
             [0,
              0,
              {'account_id': 696,
               'debit': 227.0,
               'name': u'302101002 - Delivery Order Charges - 6254427',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 251.13}],
             [0,
              0,
              {'account_id': 308,
               'debit': 207.829785370127,
               'name': u'302101002 - Delivery Order Charges - 6254427: 229.922 already out',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 229.92199999999997}],
             [0,
              0,
              {'account_id': 696,
               'credit': 207.829785370127,
               'name': u'302101002 - Delivery Order Charges - 6254427: 229.922 already out',
               'partner_id': False,
               'product_id': 3745,
               'quantity': 229.92199999999997}]]

data = []
for _,_,line in raw_data:
    line.pop('name')
    data.append(line)
print(data)
import csv

with open('entry.csv', 'w') as csvfile:
    fieldnames = ['account_id', 'credit','debit','partner_id','product_id','quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
    writer.writeheader()
    for line in data:
        writer.writerow(line)
   
