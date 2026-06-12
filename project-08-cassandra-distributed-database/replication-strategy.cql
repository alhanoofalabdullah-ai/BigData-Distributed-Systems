ALTER KEYSPACE enterprise_data
WITH replication = {
'class':'NetworkTopologyStrategy',
'datacenter1':3
};
