from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

transactions = env.from_collection([100, 500, 12000, 250, 18000])

transactions.filter(
    lambda x: x > 10000
).print()

env.execute("Fraud Detection")
