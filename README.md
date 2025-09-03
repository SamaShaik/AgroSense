# 🌱 Crop Recommendation System

A **machine learning-based web application** that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions. This system helps farmers and agricultural experts make data-driven decisions to improve productivity.

---

##  Dataset

This project utilizes the **Crop Recommendation Dataset** available on Kaggle, curated by Varshita Nalluri:

## 📊 Dataset  

Dataset: [**Crop Recommendation Dataset**](https://www.kaggle.com/datasets/varshitanalluri/crop-recommendation-dataset)  

- **Description**: The dataset contains records of seven key environmental and soil features—Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH Value, and Rainfall—paired with the most suitable crop for given conditions.

- **Description**: The dataset contains records of seven key environmental and soil features—Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH Value, and Rainfall—paired with the most suitable crop for given conditions :contentReference[oaicite:0]{index=0}.

---

##  How it Works

1. **Data Loading & Exploration**  
   - Loaded the dataset from CSV.  
   - Explored data characteristics via `head`, `shape`, `info`, checks for missing or duplicate values, basic statistics, and a correlation heatmap.

2. **Preprocessing & Feature Engineering**  
   - Mapped crop names to numeric labels.  
   - Split data into features (`X`) and target (`y`), followed by an 80/20 train-test split.  
   - Scaled numeric features using **MinMaxScaler**.

3. **Model Training & Evaluation**  
   - Trained a range of classification algorithms: Logistic Regression, Gaussian Naive Bayes, SVM, K-Nearest Neighbors, Decision Tree, Extra Tree, Random Forest, Bagging, Gradient Boosting, and AdaBoost.  
   - Evaluated accuracy scores on the test set and selected **Random Forest Classifier** as the best-performing model.

4. **Model Serialization**  
   - Persisted the trained model and scaler using **pickle** to `model.pkl` and `minmaxscaler.pkl`.

5. **Web Application with Flask**  
   - Built a simple Flask app to accept form inputs for soil and environmental parameters, preprocess them, run the model, and render crop recommendations in real time.

---

##  Technologies Used

- **Python**  
- **Data Handling & Visualization**: pandas, NumPy, seaborn, matplotlib  
- **Machine Learning**: scikit-learn (Random Forest, MinMaxScaler)  
- **Web Framework**: Flask  
- **Frontend**: HTML (e.g., `index.html` for user input and results display)

---

##  Features

- Input soil nutrients and environmental parameters.  
- Receive an **instant crop recommendation**.  
- Easy-to-use interface ideal for farmers and agriculture experts.  
- Scalable for integration with IoT devices or mobile applications.

---

##  How to Run

```bash
git clone <your-repo-link>
cd <your-repo-folder>
