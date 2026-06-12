from cassandra.cluster import Cluster
import uuid

cluster = Cluster(['127.0.0.1'])

session = cluster.connect('enterprise_data')

session.execute("""

INSERT INTO customers (
customer_id,
first_name,
last_name,
email,
country,
registration_date
)

VALUES (%s,%s,%s,%s,%s,toTimestamp(now()))

""",

(

uuid.uuid4(),
'Alhanoof',
'Alabdullah',
'alhanoof@example.com',
'Saudi Arabia'

)

)

print("Customer inserted successfully")
