# Assignment 06 – Image Denoising using Autoencoders on MNIST

## Overview

This project was completed as part of the **Celebal Excellence Internship (CEI) 2026** under the **Data Science (DS001)** track at **Celebal Technologies**.

The objective of Assignment 06 was to build a deep learning model capable of removing noise from images using an autoencoder on the **MNIST** dataset. The assignment explores and compares linear and convolutional autoencoder architectures for reconstructing clean handwritten digit images from noisy inputs.

---

## Problem Statement

**Develop an image denoising system using Autoencoders on the MNIST dataset.**

The assignment involved:

- Loading and preprocessing the MNIST dataset
- Adding random noise to clean images
- Building a Linear Autoencoder
- Building a Convolutional Autoencoder
- Training models for image reconstruction
- Evaluating reconstruction performance
- Comparing Linear and Convolutional Autoencoders
- Visualizing noisy, reconstructed, and original images

---

## Dataset

**MNIST Handwritten Digit Dataset**

MNIST consists of grayscale images of handwritten digits ranging from **0 to 9**.

The dataset is loaded directly using `torchvision` and automatically downloaded and cached during execution.

The dataset used in the project is divided into:

- **Training Images:** 48,000
- **Validation Images:** 12,000
- **Testing Images:** 10,000

---

## Deep Learning Models Used

### Linear Autoencoder

A baseline autoencoder that flattens each image and processes it through fully connected layers.

The model learns a compressed representation of the input image before reconstructing it through the decoder.

### Convolutional Autoencoder

A convolution-based architecture that preserves the spatial structure of the images.

The decoder uses nearest-neighbor upsampling followed by convolutional layers to reconstruct the clean digit images while reducing potential checkerboard artifacts.

---

## Training

Both models were trained using:

- Mean Squared Error (MSE) Loss
- 20 Training Epochs
- Noisy MNIST Images as Inputs
- Clean MNIST Images as Targets

---

## Files

| File | Description |
|------|-------------|
| MNIST_Denoising_Autoencoder.ipynb | Completed Assignment 06 Image Denoising Autoencoder Notebook |
| requirements.txt | Python dependencies required to run the project |
| README.md | Project documentation |

---

## Tools & Libraries Used

- Python
- PyTorch
- Torchvision
- NumPy
- Pandas
- Matplotlib
- Google Colab / Jupyter Notebook

---

## Learning Outcomes

Through this assignment, the following concepts were practiced:

- Autoencoders
- Encoder-Decoder Architecture
- Latent Representations
- Image Denoising
- Image Reconstruction
- Linear Autoencoders
- Convolutional Autoencoders
- Convolutional Neural Networks
- Noise Injection
- Mean Squared Error (MSE)
- Deep Learning Model Training
- Model Performance Comparison
- PyTorch and Torchvision

---

## Key Observations

- Both autoencoders learned to reconstruct clean handwritten digits from noisy input images.
- The Linear Autoencoder successfully performed denoising but produced comparatively blurrier reconstructions because it does not preserve spatial image structure.
- The Convolutional Autoencoder produced sharper reconstructed images and achieved lower reconstruction error.
- Convolutional layers are more efficient for image-based tasks because spatial filters are shared across the image.

---

## Author

**Subrata Kumar Dey**

Data Science Intern – CEI 2026

B.Tech CSE (Cyber Security & Privacy)

DIT University
