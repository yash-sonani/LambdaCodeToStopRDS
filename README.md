# LambdaCodeToStopRDS
This Lambda Code Stop Running RDS Cluster which have specific Tag using boto3 library. 


## Steps to create Schedule to stop RDS Cluster in AWS

1. Create Lambda as per [lambda_function.py](https://github.com/yash-sonani/LambdaCodeToStopRDS/blob/master/lambda_function.py) code(Python 3.7)

2. Schedule CloudWatch Trigger in Lambda with Schedule expression: [cron(01 15 * * ? *)](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html) . This will trigger lambda function every day on 9:01 PM

3. Add Tag(Mention in cunstom_filter) in RDS Cluster so that code identify the same.
