from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])

session = cluster.connect('enterprise_data')

rows = session.execute("SELECT * FROM customers")

for row in rows:

    print(row)
