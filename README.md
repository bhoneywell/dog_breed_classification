# Image Classification using AWS SageMaker

Use AWS Sagemaker to train a pretrained model that can perform image classification by using the Sagemaker profiling, debugger, hyperparameter tuning and other good ML engineering practices. This can be done on either the provided dog breed classication data set or one of your choice.

This is a project to finetune a pretrained model AWS Sagemaker and the files were created as part as part of the AWS Machine Learning Engineer nanodegree.

## Project Set Up and Installation
Enter AWS through the gateway in the course and open SageMaker Studio. 
Download the starter files.
Download/Make the dataset available. 

## Dataset
The provided dataset is the dogbreed classification dataset which can be found in the classroom.
The project is designed to be dataset independent so if there is a dataset that is more interesting or relevant to your work, you are welcome to use it to complete the project.

### Access
Upload the data to an S3 bucket through the AWS Gateway so that SageMaker has access to the data. 

## Hyperparameter Tuning
What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search
I opted to use a RESNET18 model because I wanted a model I felt could get an accurate fit, but wasn't too complex and computationally expensive.

For this model I chose to tune the epochs, learning rate and batch size. I did this so I could see how each of those metrics affected the model output. Below are the ranges I used:
"lr": ContinuousParameter(0.001, 0.1),
"batch-size": CategoricalParameter([32, 64, 128, 256, 512]),
 "epochs": IntegerParameter(2, 4)

## Debugging and Profiling
**TODO**: Give an overview of how you performed model debugging and profiling in Sagemaker

To perform the model debugging and profiling I had to setup the debugging and profiling rules before running the script. Then I passed in the hook as a variable so it could report on what rules I asked as the model ran. 

[Screen Shot 2022-12-28 at 12.54.34 PM.png]

### Results
**TODO**: What are the results/insights did you get by profiling/debugging your model?
My profiling/debugging gave the output below: 

LossNotDecreasing: Error
VanishingGradient: NoIssuesFound
Overfit: NoIssuesFound
Overtraining: NoIssuesFound
PoorWeightInitialization: Error

This led me to believe I need to look into the weights of my ML model as well as loss. Then I could look to address those issues in a future model.

**TODO** Remember to provide the profiler html/pdf file in your submission.


## Model Deployment
**TODO**: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

The deployed model takes a dog image and gives back a prediction. To query the endpoint the image needs to first be transformed similarly 
to how I transform images in my model. Then it can be queried with various sample images. 

**TODO** Remember to provide a screenshot of the deployed active endpoint in Sagemaker.
[Screen Shot 2022-12-28 at 12.54.34 PM.png]


## Documents 

[Train and Deploy](train_and_deploy.ipynb) - this file contains the actual code that was ran to train and deploy the machine learning models

[HPO](hpo.py) - this file contains the pytorch code used for the machine image classification model. 

[Train Model](train_model.py) - this file contains the pytorch code used to generate another model based on the best hyperparameters identified using Sagemaker tuning. 

[Inference](inference.py) - this file contains the code used to make inferences on the model deployed with the code from train_model.

