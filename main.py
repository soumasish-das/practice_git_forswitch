import findspark

findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Spark-JDBC") \
    .config("spark.jars.packages", "net.snowflake:snowflake-jdbc:3.13.1") \
    .getOrCreate()

snowflakequery = """select e.emp_id,e.emp_name,
  max(
    CASE
      when contact_method = 'Email' Then Contact_details
      else ''
    end
  ) as EMAIL_ID,
  max(
    CASE
      when contact_method = 'Phone' Then Contact_details
      else ''
    end
  ) as PHONE from employee e
  left outer join employee_contact ec on e.emp_id = ec.emp_id group by e.emp_id,emp_name order by e.emp_id, emp_name asc limit 5;"""

snowflakeDF = spark.read \
    .format("snowflake") \
    .options("url",
             "jdbc:snowflake://so63695.us-central1.gcp.snowflakecomputing.com/?user=ravigajul&warehourse=COMPUTE_WH&db=DEMO_DB&schema=PUBLIC") \
    .option("query", "snowflakequery ") \
    .option("driver", "net.snowflake.client.jdbc.SnowflakeDriver") \
    .load()

print("---------")
snowflakeDF.show
df.show()

spark.stop()
