data=[[1,'venky','male',2000],[2,'swathi','female',2000]]
schema=['id','name','gender','salary']
df=spark.createDataFrame(data,schema)
df.display()
