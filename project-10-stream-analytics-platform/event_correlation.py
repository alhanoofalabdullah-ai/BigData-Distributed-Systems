from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()

events = env.from_collection([
    "customer_event",
    "order_event",
    "payment_event"
])

events.print()

env.execute("Event Correlation")
