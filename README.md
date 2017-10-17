# Big Data Analytics with Java
This is the code repository for [Big Data Analytics with Java](https://www.packtpub.com/big-data-and-business-intelligence/big-data-analytics-java?utm_source=github&utm_medium=repository&utm_campaign=9781787288980), published by [Packt](https://www.packtpub.com/?utm_source=github). It contains all the supporting project files necessary to work through the book from start to finish.
## About the Book
This book covers case studies such as sentiment analysis on a tweet dataset, recommendations on a movielens dataset, customer segmentation on an ecommerce dataset, and graph analysis on actual flights dataset.

This book is an end-to-end guide to implement analytics on big data with Java. Java is the de facto language for major big data environments, including Hadoop. This book will teach you how to perform analytics on big data with production-friendly Java. This book basically divided into two sections. The first part is an introduction that will help the readers get acquainted with big data environments, whereas the second part will contain a hardcore discussion on all the concepts in analytics on big data. It will take you from data analysis and data visualization to the core concepts and advantages of machine learning, real-life usage of regression and classification using Naïve Bayes, a deep discussion on the concepts of clustering,and a review of simple neural networks on big data using deepLearning4j or plain Java Spark code. This book is a must-have book for Java developers who want to start learning big data analytics and want to use it in the real world.

## Instructions and Navigation
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter02.



The code will look like the following:
```
Dataset<Row> rowDS = spark.read().csv("data/loan_train.csv");
rowDS.createOrReplaceTempView("loans");
Dataset<Row> loanAmtDS = spark.sql("select _c6 from loans");
```

There are a few things you will require to follow the examples in this book: a text
editor (I use Sublime Text), internet access, admin rights to your machine to install
applications and download sample code, and an IDE (I use Eclipse and IntelliJ).
You will also need other software such as Java, Maven, Apache Spark, Spark
modules, the GraphFrames library, and the JFreeChart library. We mention the
required software in the respective chapters.
You also need a good computer with a good RAM size, or you can also run the
samples on Amazon AWS.

## Related Products
* [Big Data Analytics with R](https://www.packtpub.com/big-data-and-business-intelligence/big-data-analytics-r?utm_source=github&utm_medium=repository&utm_campaign=9781786466457)

* [Getting Started with Greenplum for Big Data Analytics](https://www.packtpub.com/big-data-and-business-intelligence/getting-started-greenplum-big-data-analytics?utm_source=github&utm_medium=repository&utm_campaign=9781782177043)

* [Big Data Analytics with R and Hadoop](https://www.packtpub.com/big-data-and-business-intelligence/big-data-analytics-r-and-hadoop?utm_source=github&utm_medium=repository&utm_campaign=9781782163282)

### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSe5qwunkGf6PUvzPirPDtuy1Du5Rlzew23UBp2S-P3wB-GcwQ/viewform) if you have any feedback or suggestions.
