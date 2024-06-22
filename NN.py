# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZCW1VH6CIauu86ZXCAvek13cPeLQ6Ab1
"""

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Display the first few rows of the dataset
# print(wine_data.head())

# Separate features and target
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.preprocessing import StandardScaler

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Display the shape of the datasets
print("Training set shape:", X_train.shape)
print("Test set shape:", X_test.shape)

import mlrose_hiive as mlrose
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import random

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Define the neural network structure
input_size = X_train.shape[1]
hidden_size = 10
output_size = len(np.unique(y_train))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Perform Randomized Hill Climbing to optimize weights
def random_hill_climbing(X_train, y_train, input_size, hidden_size, output_size, max_iterations=1000):
    W1, b1, W2, b2 = initialize_weights(input_size, hidden_size, output_size)
    best_loss = float('inf')

    for iteration in range(max_iterations):
        W1_new, b1_new, W2_new, b2_new = initialize_weights(input_size, hidden_size, output_size)
        A1, A2 = forward_pass(X_train, W1_new, b1_new, W2_new, b2_new)
        loss = compute_loss(A2, y_train)

        if loss < best_loss:
            W1, b1, W2, b2 = W1_new, b1_new, W2_new, b2_new
            best_loss = loss

    return W1, b1, W2, b2

# Train the neural network using Randomized Hill Climbing
W1, b1, W2, b2 = random_hill_climbing(X_train, y_train, input_size, hidden_size, output_size)

# Evaluate the trained neural network on the test set
_, A2_test = forward_pass(X_test, W1, b1, W2, b2)
test_accuracy = compute_accuracy(A2_test, y_test)

print("Test accuracy using Randomized Hill Climbing:", test_accuracy)

import mlrose_hiive as mlrose
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import random

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Define the neural network structure
input_size = X_train.shape[1]
hidden_size = 10
output_size = len(np.unique(y_train))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Perform Simulated Annealing to optimize weights
def simulated_annealing(X_train, y_train, input_size, hidden_size, output_size, max_iterations=1000, initial_temp=1000, cooling_rate=0.95):
    W1, b1, W2, b2 = initialize_weights(input_size, hidden_size, output_size)
    best_loss = float('inf')

    current_temp = initial_temp

    for iteration in range(max_iterations):
        W1_new, b1_new, W2_new, b2_new = initialize_weights(input_size, hidden_size, output_size)
        A1, A2 = forward_pass(X_train, W1_new, b1_new, W2_new, b2_new)
        loss = compute_loss(A2, y_train)

        if loss < best_loss or random.random() < np.exp((best_loss - loss) / current_temp):
            W1, b1, W2, b2 = W1_new, b1_new, W2_new, b2_new
            best_loss = loss

        current_temp *= cooling_rate

    return W1, b1, W2, b2

# Train the neural network using Simulated Annealing
W1, b1, W2, b2 = simulated_annealing(X_train, y_train, input_size, hidden_size, output_size)

# Evaluate the trained neural network on the test set
_, A2_test = forward_pass(X_test, W1, b1, W2, b2)
test_accuracy = compute_accuracy(A2_test, y_test)

print("Test accuracy using Simulated Annealing:", test_accuracy)

import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Define the neural network structure
input_size = X_train.shape[1]
hidden_size = 10
output_size = len(np.unique(y_train))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Genetic Algorithm to optimize weights
def genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size, pop_size=50, num_generations=100, mutation_rate=0.01):
    def initialize_population():
        return [initialize_weights(input_size, hidden_size, output_size) for _ in range(pop_size)]

    def select_parents(population):
        fitness_scores = [compute_loss(forward_pass(X_train, W1, b1, W2, b2)[1], y_train) for W1, b1, W2, b2 in population]
        fitness_scores = np.max(fitness_scores) - fitness_scores  # Convert to maximization problem
        total_fitness = np.sum(fitness_scores)
        selection_probs = fitness_scores / total_fitness
        parents = random.choices(population, weights=selection_probs, k=pop_size)
        return parents

    def crossover(parent1, parent2):
        W1_1, b1_1, W2_1, b2_1 = parent1
        W1_2, b1_2, W2_2, b2_2 = parent2
        W1 = (W1_1 + W1_2) / 2
        b1 = (b1_1 + b1_2) / 2
        W2 = (W2_1 + W2_2) / 2
        b2 = (b2_1 + b2_2) / 2
        return W1, b1, W2, b2

    def mutate(weights):
        W1, b1, W2, b2 = weights
        if random.random() < mutation_rate:
            W1 += np.random.randn(*W1.shape) * 0.1
        if random.random() < mutation_rate:
            b1 += np.random.randn(*b1.shape) * 0.1
        if random.random() < mutation_rate:
            W2 += np.random.randn(*W2.shape) * 0.1
        if random.random() < mutation_rate:
            b2 += np.random.randn(*b2.shape) * 0.1
        return W1, b1, W2, b2

    population = initialize_population()
    best_weights = None
    best_loss = float('inf')

    for generation in range(num_generations):
        parents = select_parents(population)
        next_population = [mutate(crossover(parents[i], parents[len(parents) - i - 1])) for i in range(pop_size)]

        for weights in next_population:
            _, A2 = forward_pass(X_train, *weights)
            loss = compute_loss(A2, y_train)
            if loss < best_loss:
                best_loss = loss
                best_weights = weights

        population = next_population

    return best_weights

# Train the neural network using Genetic Algorithm
W1, b1, W2, b2 = genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size)

# Evaluate the trained neural network on the test set
_, A2_test = forward_pass(X_test, W1, b1, W2, b2)
test_accuracy = compute_accuracy(A2_test, y_test)

print("Test accuracy using Genetic Algorithm:", test_accuracy)

import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Genetic Algorithm to optimize weights
def genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size, pop_size=50, num_generations=100, mutation_rate=0.01):
    def initialize_population():
        return [initialize_weights(input_size, hidden_size, output_size) for _ in range(pop_size)]

    def select_parents(population):
        fitness_scores = [compute_loss(forward_pass(X_train, W1, b1, W2, b2)[1], y_train) for W1, b1, W2, b2 in population]
        fitness_scores = np.max(fitness_scores) - fitness_scores  # Convert to maximization problem
        total_fitness = np.sum(fitness_scores)
        selection_probs = fitness_scores / total_fitness
        parents = random.choices(population, weights=selection_probs, k=pop_size)
        return parents

    def crossover(parent1, parent2):
        W1_1, b1_1, W2_1, b2_1 = parent1
        W1_2, b1_2, W2_2, b2_2 = parent2
        W1 = (W1_1 + W1_2) / 2
        b1 = (b1_1 + b1_2) / 2
        W2 = (W2_1 + W2_2) / 2
        b2 = (b2_1 + b2_2) / 2
        return W1, b1, W2, b2

    def mutate(weights):
        W1, b1, W2, b2 = weights
        if random.random() < mutation_rate:
            W1 += np.random.randn(*W1.shape) * 0.1
        if random.random() < mutation_rate:
            b1 += np.random.randn(*b1.shape) * 0.1
        if random.random() < mutation_rate:
            W2 += np.random.randn(*W2.shape) * 0.1
        if random.random() < mutation_rate:
            b2 += np.random.randn(*b2.shape) * 0.1
        return W1, b1, W2, b2

    population = initialize_population()
    best_weights = None
    best_loss = float('inf')
    loss_history = []

    for generation in range(num_generations):
        parents = select_parents(population)
        next_population = [mutate(crossover(parents[i], parents[len(parents) - i - 1])) for i in range(pop_size)]

        for weights in next_population:
            _, A2 = forward_pass(X_train, *weights)
            loss = compute_loss(A2, y_train)
            if loss < best_loss:
                best_loss = loss
                best_weights = weights

        population = next_population
        loss_history.append(best_loss)

    return best_weights[0], best_weights[1], best_weights[2], best_weights[3], loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    W1, b1, W2, b2, loss_history = genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs')
plt.grid(True)
plt.show()

import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Simulated Annealing to optimize weights
def simulated_annealing(X_train, y_train, input_size, hidden_size, output_size, max_iterations=1000, initial_temp=1000, cooling_rate=0.995):
    W1, b1, W2, b2 = initialize_weights(input_size, hidden_size, output_size)
    best_W1, best_b1, best_W2, best_b2 = W1, b1, W2, b2
    best_loss = float('inf')
    loss_history = []
    temperature = initial_temp

    for i in range(max_iterations):
        # Randomly modify weights
        new_W1, new_b1, new_W2, new_b2 = initialize_weights(input_size, hidden_size, output_size)
        _, A2 = forward_pass(X_train, new_W1, new_b1, new_W2, new_b2)
        loss = compute_loss(A2, y_train)
        delta_loss = loss - best_loss

        if delta_loss < 0 or np.exp(-delta_loss / temperature) > np.random.rand():
            best_W1, best_b1, best_W2, best_b2 = new_W1, new_b1, new_W2, new_b2
            best_loss = loss

        loss_history.append(best_loss)
        temperature *= cooling_rate

    return best_W1, best_b1, best_W2, best_b2, loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    W1, b1, W2, b2, loss_history = simulated_annealing(X_train, y_train, input_size, hidden_size, output_size)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size (Simulated Annealing)')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs (Simulated Annealing)')
plt.grid(True)
plt.show()

import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Genetic Algorithm to optimize weights
def genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size, pop_size=100, num_generations=100, mutation_rate=0.01):
    def crossover(parent1, parent2):
        child = {}
        for key in parent1.keys():
            crossover_point = np.random.randint(parent1[key].size)
            child[key] = np.concatenate((parent1[key].flatten()[:crossover_point], parent2[key].flatten()[crossover_point:])).reshape(parent1[key].shape)
        return child

    def mutate(child, mutation_rate):
        for key in child.keys():
            mutation_mask = np.random.rand(*child[key].shape) < mutation_rate
            child[key] += mutation_mask * np.random.randn(*child[key].shape)
        return child

    # Initialize population
    population = [{'W1': np.random.randn(input_size, hidden_size), 'b1': np.zeros((1, hidden_size)),
                   'W2': np.random.randn(hidden_size, output_size), 'b2': np.zeros((1, output_size))} for _ in range(pop_size)]

    best_individual = None
    best_loss = float('inf')
    loss_history = []

    for generation in range(num_generations):
        fitness_scores = []
        for individual in population:
            _, A2 = forward_pass(X_train, individual['W1'], individual['b1'], individual['W2'], individual['b2'])
            loss = compute_loss(A2, y_train)
            fitness_scores.append(-loss)
            if loss < best_loss:
                best_loss = loss
                best_individual = individual

        loss_history.append(best_loss)

        # Selection
        fitness_scores = np.array(fitness_scores)
        probabilities = np.exp(fitness_scores - np.max(fitness_scores))
        probabilities /= probabilities.sum()

        new_population = []
        for _ in range(pop_size // 2):
            parents = np.random.choice(population, size=2, p=probabilities, replace=False)
            child1, child2 = crossover(parents[0], parents[1]), crossover(parents[1], parents[0])
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))

        population = new_population

    return best_individual['W1'], best_individual['b1'], best_individual['W2'], best_individual['b2'], loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    W1, b1, W2, b2, loss_history = genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size (Genetic Algorithm)')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs (Genetic Algorithm)')
plt.grid(True)
plt.show()

# import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import time

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Genetic Algorithm to optimize weights
def genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size, pop_size=50, num_generations=100, mutation_rate=0.01):
    def initialize_population():
        return [initialize_weights(input_size, hidden_size, output_size) for _ in range(pop_size)]

    def select_parents(population):
        fitness_scores = [compute_loss(forward_pass(X_train, W1, b1, W2, b2)[1], y_train) for W1, b1, W2, b2 in population]
        fitness_scores = np.max(fitness_scores) - fitness_scores  # Convert to maximization problem
        total_fitness = np.sum(fitness_scores)
        selection_probs = fitness_scores / total_fitness
        parents = random.choices(population, weights=selection_probs, k=pop_size)
        return parents

    def crossover(parent1, parent2):
        W1_1, b1_1, W2_1, b2_1 = parent1
        W1_2, b1_2, W2_2, b2_2 = parent2
        W1 = (W1_1 + W1_2) / 2
        b1 = (b1_1 + b1_2) / 2
        W2 = (W2_1 + W2_2) / 2
        b2 = (b2_1 + b2_2) / 2
        return W1, b1, W2, b2

    def mutate(weights):
        W1, b1, W2, b2 = weights
        if random.random() < mutation_rate:
            W1 += np.random.randn(*W1.shape) * 0.1
        if random.random() < mutation_rate:
            b1 += np.random.randn(*b1.shape) * 0.1
        if random.random() < mutation_rate:
            W2 += np.random.randn(*W2.shape) * 0.1
        if random.random() < mutation_rate:
            b2 += np.random.randn(*b2.shape) * 0.1
        return W1, b1, W2, b2

    population = initialize_population()
    best_weights = None
    best_loss = float('inf')
    loss_history = []

    for generation in range(num_generations):
        parents = select_parents(population)
        next_population = [mutate(crossover(parents[i], parents[len(parents) - i - 1])) for i in range(pop_size)]

        for weights in next_population:
            _, A2 = forward_pass(X_train, *weights)
            loss = compute_loss(A2, y_train)
            if loss < best_loss:
                best_loss = loss
                best_weights = weights

        population = next_population
        loss_history.append(best_loss)

    return best_weights[0], best_weights[1], best_weights[2], best_weights[3], loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []
runtimes = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    start_time = time.time()
    W1, b1, W2, b2, loss_history = genetic_algorithm(X_train, y_train, input_size, hidden_size, output_size)
    end_time = time.time()
    runtime = end_time - start_time
    runtimes.append(runtime)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Print runtimes
for size, runtime in zip(training_sizes, runtimes):
    print(f"Training size {size}: Runtime = {runtime:.2f} seconds")

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs')
plt.grid(True)
plt.show()

# import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import time

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Simulated Annealing to optimize weights
def simulated_annealing(X_train, y_train, input_size, hidden_size, output_size, max_iterations=1000, initial_temp=1000, cooling_rate=0.995):
    W1, b1, W2, b2 = initialize_weights(input_size, hidden_size, output_size)
    best_W1, best_b1, best_W2, best_b2 = W1, b1, W2, b2
    best_loss = float('inf')
    loss_history = []
    temperature = initial_temp

    for i in range(max_iterations):
        # Randomly modify weights
        new_W1, new_b1, new_W2, new_b2 = initialize_weights(input_size, hidden_size, output_size)
        _, A2 = forward_pass(X_train, new_W1, new_b1, new_W2, new_b2)
        loss = compute_loss(A2, y_train)
        delta_loss = loss - best_loss

        if delta_loss < 0 or np.exp(-delta_loss / temperature) > np.random.rand():
            best_W1, best_b1, best_W2, best_b2 = new_W1, new_b1, new_W2, new_b2
            best_loss = loss

        loss_history.append(best_loss)
        temperature *= cooling_rate

    return best_W1, best_b1, best_W2, best_b2, loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []
runtimes = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    start_time = time.time()
    W1, b1, W2, b2, loss_history = simulated_annealing(X_train, y_train, input_size, hidden_size, output_size)
    end_time = time.time()
    runtime = end_time - start_time
    runtimes.append(runtime)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Print runtimes
for size, runtime in zip(training_sizes, runtimes):
    print(f"Training size {size}: Runtime = {runtime:.2f} seconds")

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size (Simulated Annealing)')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs (Simulated Annealing)')
plt.grid(True)
plt.show()

# import mlrose_hiive as mlrose
import numpy as np
import random
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import time

# Load Wine Quality Dataset
wine_data_path = "/content/wine/winequality-white.csv"  # Adjust path as needed
wine_data = pd.read_csv(wine_data_path, delimiter=';')

# Separate features and target
X = wine_data.drop('quality', axis=1).values  # Convert to numpy array
y = wine_data['quality'].values  # Convert to numpy array

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Define the neural network structure
input_size = X.shape[1]
hidden_size = 10
output_size = len(np.unique(y_encoded))

# Initialize weights randomly
def initialize_weights(input_size, hidden_size, output_size):
    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))
    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))
    return W1, b1, W2, b2

# Define the neural network forward pass
def forward_pass(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(A1, W2) + b2
    exp_scores = np.exp(Z2)
    A2 = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    return A1, A2

# Define the loss function
def compute_loss(A2, y):
    m = y.shape[0]
    log_probs = -np.log(A2[range(m), y])
    loss = np.sum(log_probs) / m
    return loss

# Define the accuracy function
def compute_accuracy(A2, y):
    predictions = np.argmax(A2, axis=1)
    accuracy = np.mean(predictions == y)
    return accuracy

# Randomized Hill Climbing to optimize weights
def randomized_hill_climbing(X_train, y_train, input_size, hidden_size, output_size, max_iterations=1000):
    W1, b1, W2, b2 = initialize_weights(input_size, hidden_size, output_size)
    best_W1, best_b1, best_W2, best_b2 = W1, b1, W2, b2
    best_loss = float('inf')
    loss_history = []

    for i in range(max_iterations):
        # Randomly modify weights
        new_W1, new_b1, new_W2, new_b2 = initialize_weights(input_size, hidden_size, output_size)
        _, A2 = forward_pass(X_train, new_W1, new_b1, new_W2, new_b2)
        loss = compute_loss(A2, y_train)

        if loss < best_loss:
            best_W1, best_b1, best_W2, best_b2 = new_W1, new_b1, new_W2, new_b2
            best_loss = loss

        loss_history.append(best_loss)

    return best_W1, best_b1, best_W2, best_b2, loss_history

# Train and evaluate the neural network for different training sizes
training_sizes = [0.2, 0.4, 0.6, 0.8]
accuracy_results = []
loss_histories = []
runtimes = []

for size in training_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=1-size, random_state=42)
    start_time = time.time()
    W1, b1, W2, b2, loss_history = randomized_hill_climbing(X_train, y_train, input_size, hidden_size, output_size)
    end_time = time.time()
    runtime = end_time - start_time
    runtimes.append(runtime)
    _, A2_test = forward_pass(X_test, W1, b1, W2, b2)
    test_accuracy = compute_accuracy(A2_test, y_test)
    accuracy_results.append(test_accuracy)
    loss_histories.append(loss_history)

# Print runtimes
for size, runtime in zip(training_sizes, runtimes):
    print(f"Training size {size}: Runtime = {runtime:.2f} seconds")

# Plot Accuracy vs. Training Size
plt.figure(figsize=(10, 6))
plt.plot(training_sizes, accuracy_results, marker='o')
plt.xlabel('Training Size')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Training Size (Randomized Hill Climbing)')
plt.grid(True)
plt.show()

# Plot Loss vs. Epochs for the best training size
best_training_size_idx = np.argmax(accuracy_results)
best_loss_history = loss_histories[best_training_size_idx]

plt.figure(figsize=(10, 6))
plt.plot(range(len(best_loss_history)), best_loss_history, marker='o')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs. Epochs (Randomized Hill Climbing)')
plt.grid(True)
plt.show()