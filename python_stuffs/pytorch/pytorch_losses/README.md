# Pytorch Losses
There are three popular losses implemeted by PyTorch for classification tasks:
- [BCELoss]()
- [BCELossWithLogitsLoss]()
- [CrossEntropyLoss]()

with minor differences and they are to be used for different cases. 

For more details please check the respective links and the notebook

## BCELoss
- Target values y should be between 0 and 1
- Network to only have one output node
- Need to implement Sigmoid Activation before applying BCELoss

## BCELossWithLogitsLoss
- combines a Sigmoid layer and the BCELoss in one single class
- This versionis more numerically stable than using a plain Sigmoid followed by a BCELoss, by combining the operations into one layer, we take advantage of the log-sum exp trick for numerical stability
- We should use this all the time

## Cross Entropy Loss
- Use when classification problem with C classes
- Can use it with a binary classification problem by having the network have 2 output nodes but it is superfluous [read more](https://stats.stackexchange.com/questions/207049/neural-network-for-binary-classification-use-1-or-2-output-neurons)
- seems like only the index version work (one hot encoded targets)