import numpy as np
import torch
import torchmetrics
import torchmetrics.classification

TASK = 'multiclass'
NUM_CLASSES = 3

def accuracy(y_true, y_pred):
    accuracy = torchmetrics.Accuracy(task = TASK, num_classes=NUM_CLASSES)
    return accuracy(y_pred, y_true)

def precision(y_true, y_pred):
    precision = torchmetrics.Precision(task = TASK, num_classes=NUM_CLASSES)
    return precision(y_pred, y_true)

def sensitivity(y_true, y_pred):
    sensitivity = torchmetrics.Recall(task = TASK, num_classes=NUM_CLASSES)
    return sensitivity(y_pred, y_true)

def specificity(y_true, y_pred):
    specificity = torchmetrics.Specificity(task = TASK, num_classes=NUM_CLASSES)
    return specificity(y_pred, y_true)

def f_score(y_true, y_pred):
    f_scaore = torchmetrics.F1Score(task = TASK, num_classes=NUM_CLASSES)
    return f_score(y_pred, y_true)