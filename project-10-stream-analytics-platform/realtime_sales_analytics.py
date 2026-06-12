from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

data = env.from_collection([100, 200, 300, 400])

data.map(lambda x: x * 1.15).print()

env.execute("Real Time Sales Analytics")
