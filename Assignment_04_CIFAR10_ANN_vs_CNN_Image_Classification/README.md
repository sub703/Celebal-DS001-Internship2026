# Assignment 04 – CIFAR-10 Image Classification using ANN and CNN

## Overview

This assignment was completed as part of the **Celebal Excellence Internship (CEI) 2026** under the **Data Science (DS001)** track at **Celebal Technologies**.

The objective of this assignment was to build and compare multiple deep learning models for image classification using the **CIFAR-10** dataset. The project analyzes how different neural network architectures and training strategies affect model performance by implementing an Artificial Neural Network (ANN), a Convolutional Neural Network (CNN), and a CNN trained with data augmentation.

---

## Problem Statement

**Build and compare multiple deep learning models for image classification on the CIFAR-10 dataset.**

The assignment involved designing and implementing a complete deep learning workflow covering:

- Data Loading and Exploration
- Data Preprocessing and Normalization
- Artificial Neural Network (ANN)
- Convolutional Neural Network (CNN)
- Batch Normalization and Dropout
- Data Augmentation
- Model Training and Evaluation
- Performance Comparison
- Confusion Matrix and Classification Report
- Result Analysis

---

## Dataset

**CIFAR-10 Image Dataset**

The CIFAR-10 dataset consists of **60,000 color images (32 × 32 pixels)** belonging to **10 different classes**:

- Airplane
- Automobile
- Bird
- Cat
- Deer
- Dog
- Frog
- Horse
- Ship
- Truck

The dataset contains:

- **Training Images:** 50,000
- **Testing Images:** 10,000

The dataset is automatically downloaded using the TensorFlow/Keras API, so no manual download is required.

---

## Deep Learning Models Implemented

### Artificial Neural Network (ANN)

- Fully Connected Dense Layers
- Flattened Image Input
- Baseline Model for Performance Comparison

### Convolutional Neural Network (CNN)

- Convolutional Layers
- Max Pooling Layers
- Batch Normalization
- Dropout Regularization

### CNN with Data Augmentation

The CNN model was further improved using real-time data augmentation techniques to improve generalization and reduce overfitting.

---

## Files

| File | Description |
|------|-------------|
| | week4_subrata_kumar_dey.ipynb | Completed Week 4 Image Classification Assignment Notebook |
| requirements.txt | Python dependencies required to run the project |
| README.md | Project documentation |

---

## Tools & Libraries Used

- Python
- TensorFlow
- Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Google Colab / Jupyter Notebook

---

## Learning Outcomes

Through this assignment, the following concepts were practiced:

- Image preprocessing and normalization
- Artificial Neural Networks (ANN)
- Convolutional Neural Networks (CNN)
- Batch Normalization
- Dropout Regularization
- Data Augmentation
- Deep Learning model training and evaluation
- Confusion Matrix and Classification Report generation
- Comparative analysis of deep learning architectures
- Image classification using TensorFlow/Keras

---

## Key Observations

- CNN significantly outperformed the baseline ANN by effectively learning spatial features from images.
- Batch Normalization and Dropout improved model stability and reduced overfitting.
- Data Augmentation further improved model generalization and validation performance.
- Most classification errors occurred between visually similar classes such as cats and dogs due to the low image resolution.

---

## Author

**Subrata Kumar Dey**

Data Science Intern – CEI 2026

B.Tech CSE (Cyber Security & Privacy)

DIT University
