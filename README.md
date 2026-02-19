# End-to-End-Credit-Risk-Customer-Intelligence-Platform

📌 Problem Statement

Financial institutions must accurately assess borrower creditworthiness while maintaining portfolio profitability and minimizing default risk. Traditional rule-based credit evaluation systems often fail to capture complex financial patterns, leading to:

Increased loan default rates

Inefficient risk segmentation

Limited data-driven decision-making

Poor scalability for analytical reporting

This project addresses these challenges by building a scalable, end-to-end credit risk intelligence system that integrates data warehousing, ETL pipelines, feature engineering, machine learning, and business intelligence.

🎯 Project Objective

The objective of this project is to design and deploy a production-style analytics system that:

Predicts the probability of loan default using machine learning

Segments customers based on financial behavior and risk profile

Provides executive-level insights through interactive dashboards

Implements a structured data warehouse architecture

Enables deployment-ready risk scoring

🏗️ Solution Architecture

This project simulates a real-world fintech data ecosystem consisting of:

Data Warehouse (Star Schema)

ETL Pipeline (Python + PostgreSQL)

Advanced Feature Engineering

Machine Learning Classification Models

Power BI Executive Dashboard

Web-based Model Deployment

🗄️ Data Warehouse Design

A star schema architecture was implemented to support scalable analytical queries.

Fact Table

Loan-level transactions

Default indicator (target variable)

Dimension Tables

Customer information

Financial profile

Time dimension

Location

This structure ensures optimized aggregation, reporting flexibility, and clean analytical workflows.

🔄 ETL Pipeline

A modular ETL pipeline was developed using Python:

Extract

Raw loan and customer datasets

Transform

Missing value handling

Outlier detection

Data normalization

Categorical encoding

Creation of financial risk ratios

Load

Structured data into PostgreSQL fact and dimension tables

This ensures data integrity, reproducibility, and analytics readiness.

🧮 Feature Engineering

Domain-driven financial indicators were engineered to enhance model performance, including:

Debt-to-Income Ratio

Credit Utilization Rate

Loan-to-Income Ratio

EMI Burden Ratio

Income Segmentation

Age Bucketing

Historical Default Count

These features reflect real-world credit risk assessment practices.

🤖 Machine Learning Model

Multiple classification models were implemented:

Logistic Regression

Random Forest

XGBoost

Evaluation metrics:

Accuracy

Precision

Recall

F1 Score

ROC-AUC

Given the imbalanced nature of credit risk data, class weighting and SMOTE techniques were applied to improve predictive performance.

The final model generates a probability-based risk score for each borrower.

📊 Business Intelligence Dashboard

An interactive Power BI dashboard was developed to provide strategic insights:

Executive Overview

Total Loans

Default Rate

Risk Distribution

Portfolio Exposure

Risk Analysis

Default by income group

Default by geography

Feature importance insights

Customer Intelligence

Risk segmentation

Profitability vs Risk matrix

This enables informed lending decisions and risk optimization strategies.

🌐 Deployment

The trained model is deployed via:

Streamlit web application for real-time risk prediction
OR

API-based backend integration

This simulates real-world credit scoring systems used in financial institutions.

💼 Business Impact

This platform enables:

Data-driven loan approval decisions

Early identification of high-risk borrowers

Reduction in credit losses

Improved risk-adjusted returns

Scalable analytics infrastructure

🛠️ Tech Stack

Python (Pandas, NumPy, Scikit-learn)

PostgreSQL

Power BI

XGBoost

Streamlit / Flask

Git & GitHub
