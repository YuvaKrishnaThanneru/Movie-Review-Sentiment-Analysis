<div align="center">
  <h1 style="color:#8a2be2; margin-right: 20px;">Movie Review Sentiment Analysis</h1>
</div>

## Overview
This project focuses on **sentiment analysis** of movie reviews using **Natural Language Processing (NLP)** techniques. The project involves creating a dataset of movie reviews and implementing a **Naive Bayes Classifier** to predict the sentiment of the reviews (positive or negative). It showcases end-to-end data processing, model training, and evaluation.

The project consists of two main components:
1. **Dataset Creation**: A synthetic dataset of movie reviews with labeled sentiments (positive or negative).
2. **Model Training and Sentiment Prediction**: Using the dataset to train a **Multinomial Naive Bayes** classifier for predicting the sentiment of new movie reviews.

## Key Features
- **Text Data Preprocessing**: The project uses **CountVectorizer** to convert textual data into a numerical format (bag-of-words model).
- **Model Implementation**: The **Multinomial Naive Bayes** algorithm is employed to classify reviews as either positive or negative.
- **Evaluation Metrics**: The model's performance is evaluated using metrics like **accuracy score** and **classification report** (precision, recall, and F1-score).
- **Interactive User Input**: The project includes a feature where users can input their own movie reviews and receive real-time sentiment predictions.

## Workflow
1. **Data Preparation**:
   - A synthetic dataset is generated with movie reviews and corresponding sentiment labels.
   - The dataset is saved as a CSV file (`movie_reviews.csv`).

2. **Training the Model**:
   - The dataset is split into **training** and **testing** sets using `train_test_split`.
   - The reviews are vectorized using **CountVectorizer**, transforming text into numerical features.
   - The **Multinomial Naive Bayes** classifier is trained on the vectorized training data.

3. **Model Evaluation**:
   - The model's accuracy is computed on the test set.
   - A detailed **classification report** provides insight into the model's performance in terms of precision, recall, and F1-score.

4. **User Interaction**:
   - The project allows users to input new reviews and get sentiment predictions in real-time.

## Technologies and Tools
- **Python**: Programming language for data manipulation and model training.
- **Pandas**: Used for data handling and CSV file operations.
- **scikit-learn**: Provides tools for data splitting, vectorization, model training, and evaluation.
- **NLP**: Sentiment analysis using text vectorization techniques.
- **Multinomial Naive Bayes**: For sentiment classification.
- **Interactive Input**: Allows real-time prediction for custom movie reviews.
