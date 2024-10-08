import pyspark
import pandas as pd

msg = "\nHellow World, \nWe will have fun soon.\n"
print(msg)

pd.read_csv('Data.csv')

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Test').getOrCreate()
df_datafile = spark.read.csv('Data.csv');