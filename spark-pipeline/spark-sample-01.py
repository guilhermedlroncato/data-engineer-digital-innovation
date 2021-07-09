from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext

spark_session = SparkSession.builder.enableHiveSupport().getOrCreate()

sc = spark_session.sparkContext
ssc = StreamingContext(sc, 1)
lines = ssc.socketTextStream('localhost', 5432)
counts = lines.flatMap(lambda line: line.split('')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
counts.pprint()
ssc.start()
ssc.awaitTermination()

spark_session.stop()