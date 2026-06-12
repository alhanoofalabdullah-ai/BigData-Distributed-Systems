from cassandra.cluster import Cluster
import uuid

cluster = Cluster(['127.0.0.1'])

session = cluster.connect('enterprise_data')

session.execute("""

INSERT INTO orders (
order_id,
customer_id,
order_date,
amount,
status
)

VALUES (%s,%s,toTimestamp(now()),%s,%s)

""",

(

uuid.uuid4(),
uuid.uuid4(),
4500,
'Completed'

)

)

print("Order inserted successfully")
