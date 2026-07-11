# CIFAR-10 Image Classification: ANN vs CNN

An image classification project on the CIFAR-10 dataset that builds and compares three models: a plain Artificial Neural Network, a Convolutional Neural Network, and a CNN trained with data augmentation. The project analyzes how model architecture and training strategy each affect performance.

## Dataset

CIFAR-10 is a set of 60,000 color images at 32 by 32 resolution across ten classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, and truck. It splits into 50,000 training images and 10,000 test images. Keras downloads it automatically, so no manual download is needed.

## What the notebook covers

1. Loading and exploring the data
2. Preprocessing (normalization and reshaping)
3. An ANN baseline
4. A CNN with batch normalization and dropout
5. The same CNN trained with data augmentation
6. A side by side comparison of all three models
7. A confusion matrix and a per class report for the best model
8. A written analysis of architectures and training strategies

## How to run

The easiest path is Google Colab.

1. Open `CIFAR10_ANN_CNN_Project.ipynb` in Colab.
2. Set the runtime to GPU under Runtime, Change runtime type.
3. Choose Runtime, Run all.

To run locally instead, install the dependencies and launch Jupyter:

```
pip install -r requirements.txt
jupyter notebook
```

## Key takeaways

- Moving from the ANN to the CNN gives the largest jump in accuracy, because the CNN understands the spatial structure of images while the ANN does not.
- The CNN often reaches higher accuracy with a similar or smaller parameter count, thanks to weight sharing in convolution layers.
- Data augmentation mainly improves generalization, shown by a smaller gap between training and validation accuracy.
- The most common errors are between visually similar classes such as cat and dog, which is largely a limit of the small image size.

## Files

- `CIFAR10_ANN_CNN_Project.ipynb` : the full notebook
- `requirements.txt` : Python dependencies
