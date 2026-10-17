from pyspark import pipelines as dp
from pyspark.sql.functions import col


# This file defines a sample transformation.
# Edit the sample below or add new transformations
# using "+ Add" in the file browser.
# Adding a new comment for demonstrating a code change and testing CI/CD pipeline

@dp.table
def sample_trips_dab_demo():
    return spark.read.table("samples.nyctaxi.trips")
