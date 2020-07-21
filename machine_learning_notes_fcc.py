'''
###Introduction to ML
AI -Artificial Intelligence. predefined rules, algorithims to follow.  Some can be complicated, very long.

ML -Machine Learning. A subset of AI.  Attempts to figure the rules out.  Give it data and answers, and it comes up with the rules. 1 layer of data?.

NN -Neural Networks. A form of ML, that uses a layered representation of data. Think of multiple layers, (multi stage information extraction process...)



###Introduction to TensorFlow
Tensor -made from vectors and matricies to potentially higher dimensions

Creating Tensors:
string = tf.Variable("this is a string", tf.string)
number = tf.Variable(324, tf.int16)
floating = tf.Variable(3.56, tf.float64)

Rank / Degree:
-represents the number of diminessions in the tensor
a scarlar value is 0 dim, ex: 5
an array is 1 dim ex: [5, 3, 2]
a 2d array is rank 2 ex: [[5, 3, 2], [6, 7, 8]]
The rank / degree is determened by the deepest nested array

#get the rank, shape, and data type:
my_tensor_var = tf.Variable([[5, 3, 2], [6, 7, 8]], tf.int16)
tf.rank(my_tensor_var) #-> tf.Tensor: shape=(), dtype=int16, numpy=2
my_tensor_var.shape #->TensorShape([2,2])

#reshape
tf.Tensor(some_tensor_var, shape=(1,2,3))
#-> [[[x,x,x],[x,x,x]]] ->1 array, with 2 arrays, with 3 values

#Tensor Types
constant, variable, placeholder, sparseTensor.  Only variable is mutable

#Evaluate Tensor
with tf.Session() as sess:
	my_tensor.eval()



###Core Learning Algorithms
-Linear Regression
-Classification
-Clustering
-Hidden Markov Models

#linear Regression - linear correspondance between data...can use multiple data sets. ex: age, weight, blood pressure => life expectancy



###Core Learning Algorithms: Working with Data
###Core Learning Algorithms: Training and Testing Data

TF wants the data frame to be composed of numbers.
categorical_columns = are columns using non-numbers

#example from titanic data:
CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []
#this loops through the cat columns to replace words with numbers.
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from given feature column
  #TF method that on the surface turns it into an object with key and values (key being original names, values being the new numeric representation.  -it is probably working differently, but that's an easy way to understand it)
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

print(feature_columns)




###Core Learning Algorithms: The Training Process

#essentially creates an obj/func that returns data in formated fashing for tf to use (basically just gives our data to TF and tells it how many batches and epochs to use)
def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use


#passes the df variables & the answer column
train_input_fn = make_input_fn(dftrain, y_train)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)


#linear_est is our tf model, that can call other tf methods later
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)
# We create a linear estimtor by passing the feature columns we created earlier (feature_columns, was just a dict with column names and col values converted to numbers)

linear_est.train(train_input_fn)  # train
result = linear_est.evaluate(eval_input_fn)  # get model metrics/stats by testing on tetsing data

clear_output()  # clears consoke output (there's a lot of TF gibberish...)
print(result)
print(result['accuracy'])  # the result variable is simply a dict of stats about our model
#accuracy (the model compares how accurate it is compared to what should be expected based on the data fed to it)
####^everything to this point has been to create a TF model, that can then be used to make predictions etc####

result = list(linear_est.predict(eval_input_fn))
clear_output()


i = 0
import random as random

#creates a list and shuffles to show 10 random people
randoList = list(range(len(dfeval.index)))
random.shuffle(randoList)
##prints 10 random people to compare tf predictions with actual results
while i < 10:
  randoNum = randoList[i]
  print('person row info: ', dfeval.loc[randoNum])
  print('survived (1 = y, 0 = n): ', y_eval.loc[randoNum])
  print('TF model prediction: ', result[randoNum]['probabilities'][1])
  i += 1


#methods so far: .train .evaluate .predict
pred_dicts = list(linear_est.predict(eval_input_fn))

probs = pd.Series([pred['probabilities'][1] for pred in pred_dicts])
print(probs)
probs.plot(kind='hist', bins=20, title='predicted probabilities')




###Core Learning Algorithms: Classification

###Core Learning Algorithms: Building the Model

###Core Learning Algorithms: Clustering

###Core Learning Algorithms: Hidden Markov Models

###Core Learning Algorithms: Using Probabilities to make Predictions

###Neural Networks with TensorFlow

###Neural Networks: Activation Functions

###Neural Networks: Optimizers

###Neural Networks: Creating a Model

###Convolutional Neural Networks

###Convolutional Neural Networks: The Convolutional Layer

###Creating a Convolutional Neural Network

###Convolutional Neural Networks: Evaluating the Model

###Convolutional Neural Networks: Picking a Pretrained Model

###Natural Language Processing With RNNs

###Natural Language Processing With RNNs: Part 2

###Natural Language Processing With RNNs: Recurring Neural Networks

###Natural Language Processing With RNNs: Sentiment Analysis

###Natural Language Processing With RNNs: Making Predictions

###Natural Language Processing With RNNs: Create a Play Generator

###Natural Language Processing With RNNs: Building the Model

###Natural Language Processing With RNNs: Training the Model

###Reinforcement Learning With Q-Learning

###Reinforcement Learning With Q-Learning: Part 2

###Reinforcement Learning With Q-Learning: Example

###Conclusion