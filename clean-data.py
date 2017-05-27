# encoding: utf-8
import csv
import glob


def decode(row):
    return [s.decode('iso-8859-1') for s in row]


def encode(row):
    return [s.encode('utf-8') for s in row]


for f in glob.glob('data/btw05_kerg.csv'):
    print f
    f_out = f.replace('data/', 'data/cleaned/')
    out = csv.writer(open(f_out, 'w'), dialect='excel-tab')
    data = csv.reader(open(f), delimiter=';')

    i = 0
    row = data.next()
    while row[0] != 'Nr' and row[0] != 'Wahlkreis':
        row = data.next()

    # pull in next two rows
    header = []
    # fill right
    header_s = [row, data.next()]
    if f != 'data/btw94_kerg.csv':
        header_s.append(data.next())
    for row in header_s:
        row = decode(row)
        for c in range(len(row)):
            if c > 0 and row[c] == '' and row[c-1] != 'Name':
                row[c] = row[c-1]
        header.append(row)

    single_row_head = []
    for c in range(len(header[0])):
        k = []
        for h in header:
            if len(h) > c and h[c] != '' and h[c] != u'Endgültig':
                k.append(h[c])
        single_row_head.append('.'.join(k))

    single_row_head[0] = 'Nr'
    single_row_head[1] = 'Wahlkreis'
    single_row_head[2] = 'Land'
    nrow = []
    for h in single_row_head:
        if 'Vorperiode' not in h:
            nrow.append(h)
    print len(nrow)
    out.writerow(encode(nrow))

    for row in data:
        row = decode(row)
        if len(row) > 1 and row[0] != '' and int(row[0]) < 900:
            nrow = []
            for i in range(len(row)):
                if 'Vorperiode' not in single_row_head[i]:
                    nrow.append(row[i])
            out.writerow(encode(nrow))
