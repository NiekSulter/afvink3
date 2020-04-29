import mysql.connector
from flask import Markup


def load_genes(var, lim):
    if lim == '':
        lim = 30

    conn = mysql.connector.connect(host="ensembldb.ensembl.org",
                                   user='anonymous',
                                   password='',
                                   db='homo_sapiens_core_98_38')

    cursor = conn.cursor()
    cursor.execute('select description from gene where description like \'%{}%\' limit {}'.format(var, lim))

    results = []
    for i in cursor:
        x = i[0]
        if var in x:
           x = x.replace(var, Markup('<b>' + var + '</b>'))
        results.append(x)

    return results
