import mysql.connector

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
        results.append(i[0])

    return results

if __name__ == '__main__':
    x = 'zinc'
    y = load_genes(x)
    for i in y:
        print(i)
