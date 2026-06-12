CREATE KEYSPACE enterprise_data
WITH replication = {
'class':'SimpleStrategy',
'replication_factor':3
};
