# Databricks notebook source
data=[[1,'venky',2000],[2,'swathi',3000]]
schema=['id','name','salary']
df=spark.createDataFrame(data,schema)
df.display()
