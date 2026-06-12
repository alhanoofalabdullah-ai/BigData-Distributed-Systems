from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

activities = env.from_collection([
    "login",
    "purchase",
    "logout"
])

activities.print()

env.execute("Customer Activity Stream")
