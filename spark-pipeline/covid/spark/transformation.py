from os import path
from pyspark.sql import SparkSession
from pyspark import SparkConf
import pyspark.sql.functions as F
from os.path import abspath

if __name__ == '__main__':
    
    # path data-lake local
    path_datacovid = '/home/guilherme/Cursos/Alura/spark-pipeline/covid/data'

    # inicio sessão spark
    spark = SparkSession \
        .builder \
        .appName("dados-vacinacao-covid") \
        .config("spark.sql.warehouse.dir", abspath('vacinacao-covid')) \
        .enableHiveSupport() \
        .getOrCreate()

    df1 = spark.read.format('csv') \
        .option('header', 'true') \
        .option('inferSchema', 'true') \
        .load(path_datacovid + '/landing/country_vaccinations.csv')

    # exibindo o schema do df
    df1.printSchema()
    
    # imprimindo as 20 primeiras linhas
    df1.show()    

    # gravando os dados em formato parquet na camada bronze
    df1.write.format('parquet') \
        .mode('overwrite') \
        .save(path_datacovid + '/bronze/country_vaccinations')


    # transforma df1 em uma tempview
    df1.createOrReplaceTempView('country_vaccinations')

    # executando query na tempView
    spark.sql(
        '''
        SELECT country,
               ROUND(SUM(people_vaccinated),2) as people_vaccinated,
               ROUND(SUM(total_vaccinations),2) as total_vaccinations
          FROM country_vaccinations
      GROUP BY country
      ORDER BY country
        '''
    ).show()

    # encerra sessão spark
    spark.stop()