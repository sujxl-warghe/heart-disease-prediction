# 🫀 Heart Disease Prediction Using Machine Learning

Heart disease is one of the leading causes of death worldwide. Early prediction can help in reducing risk through timely medical advice and lifestyle changes.

This project implements a **Machine Learning–based Heart Disease Prediction System** that learns from real patient records and predicts whether a person may have heart disease or not. The trained model is deployed as a **Streamlit web application** so anyone can easily interact with it.

---

## 🎯 Project Objective

> **Given a set of medical and health-related attributes of a patient, predict whether the patient is likely to have heart disease.**

This project follows a complete machine-learning workflow — from understanding the problem to deployment.

---

## 📊 Dataset Information

The dataset used is the **Cleveland Heart Disease Dataset**, which is widely used in research and academic ML projects.

Dataset Source Links:

🔗 UCI Machine Learning Repository  
https://archive.ics.uci.edu/ml/datasets/heart+Disease  

🔗 Kaggle Dataset  
https://www.kaggle.com/ronitf/heart-disease-uci  

The dataset contains **303 records**, each labelled as:

- `1` → Heart disease present  
- `0` → No heart disease  

---

Heart-Disease-Prediction/
│
├── app.py
├── logistic_regression.pkl
├── README.md
├── requirements.txt
└── notebook.ipynb   (optional)


## 🧠 Machine Learning Model

Multiple ML algorithms were experimented with, and **Logistic Regression** was selected as the final model because:

✔ It performs well on binary classification  
✔ It’s interpretable and easy to explain  
✔ It works effectively on structured health datasets  

### 📌 Final Model Results (on test data)

- **Accuracy:** ~88.5%  
- **Precision:** ~90.6%  

These metrics indicate that the model is reasonably reliable for academic and learning purposes.

---

## 🛠 Technologies & Libraries Used

This project uses the following tools and libraries:

- Python  
- NumPy  
- Pandas  
- Scikit-Learn  
- Matplotlib / Seaborn  
- Streamlit  
- Pickle  

---

## 🖥️ Streamlit Web Application

The project includes a **Streamlit web app** that allows users to:

✔ Input required health parameters  
✔ Submit the data  
✔ Get an instant prediction  
✔ See whether the user is at risk or not  

Prediction Output:

- ⚠️ **At Risk of Heart Disease**
- ✅ **Healthy / No Risk Detected**

---

## 🚀 How to Run the Project Locally

1. Clone or download the project :
```bash
git clone https://github.com/sujxl-warghe/heart-disease-prediction.git
```
2. Create a virtual environment :
```bash
pyhton -m venv venv
.venv/Scripts/activate
```
3. Install dependencies :
```bash
pip install requirement.txt
```
4. Run the application :
```bash
streamlit run app.py
```
