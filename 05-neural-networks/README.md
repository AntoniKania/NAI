# Neural networks

Authors: Antoni Kania, Rafał Sojecki

The application provides an implementation of neural networks for solving classification problems.

## Usage

1. Install the dependencies listed in the `requirements.txt` file (in root folder of repository):
    ```bash
    pip install -r requirements.txt
    ```
2. Run application
   ```bash
    python index.py <model_name>
    ```

Application will run all functionality described in [models](Models) for each dataset in order.

## Models

### fashion_mnist
![16](media/mnist.png)
### cats

On this network we compared ussage of 2 sizes of neural networks (by neuron count). [Used dataset](https://www.kaggle.com/datasets/yapwh1208/cats-breed-dataset/data)

#### 16 neurons

![16](media/16.png)

#### 256 neurons

![256](media/256.png)

Bigger neural networks have better accuracy than smaller ones, but the learning process takes longer. In both cases, the network correctly classified this cat.

 ![256](resources/random.jpg)
### cifar10
 Trained network, To test it we used first image of dataset to classify it.
 ![cifar10](media/cifar10.png)
### pima

#### Accuracy comparison with decision tree and SVM for pima dataset
- Neural Network Accuracy: 0.7494
- Decision Tree Accuracy: 0.7077
- SVM Accuracy: 0.7597

![neural_network](media/accuracy_pima_neural_network.png)

![decision_tree](media/accuracy_pima_decision_tree.png)

![decision_tree](media/accuracy_pima_svm.png)

