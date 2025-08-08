# GammaGroup_JC_DS_FT_JKT_28_FinalProject
# Turning Churn Into Opportunity: A Strategic Analysis of Telco Customer Behavior
Created by:
- **Muhammad Fachry Priambodo**
- **Aimar Mohammad Butragueno**
- **Gerald Pascal Ginting**

# **Context**
In today’s highly competitive telecom industry, customer churn directly impacts profitability and long-term growth. This project explores customer behavior through a data-driven lens to uncover opportunities for improving retention, maximizing revenue, and streamlining operations.

# **Problem Statement**
To transform raw customer data into actionable business insights by analyzing the patterns, drivers, and risks associated with customer churn.

# **Goals**
1. **Churn Understanding**  
   Identify the key factors that influence customer churn through exploratory analysis and predictive modeling.

2. **Customer Segmentation**  
   Cluster customers based on service usage, contract types, and payment behavior to uncover distinct personas and risk profiles.

3. **Revenue Optimization**  
   Quantify the financial impact of churn and explore how customer lifetime value (CLTV) is affected across segments.

4. **Operational Improvement**  
   Evaluate how services, billing methods, and contract structures correlate with churn, identifying levers for operational efficiency.

# **Analytical Approach**
- Data understanding & cleaning
- Perform exploratory data analysis (EDA) to identify patterns and correlations.
- Apply clustering techniques to define customer personas.
- Develop a churn prediction model to identify high-risk customers.
- Generate business-driven recommendations supported by visual insights.

# **Evaluation Metrics**
- Accuracy: The proportion of correct predictions for both churn and non-churn.
- Precision & Recall: Especially Recall for the “Churn” class, as it is important to minimize false negatives (customers predicted as non-churn but actually churn).
- F1-Score: A combination of Precision and Recall.
- ROC-AUC Score: Measures the model’s ability to distinguish between churn and non-churn classes.

# **Stakeholder**
This notebook is designed for both data teams and executive stakeholders who seek a strategic understanding of churn dynamics and its implications for customer value and service design.

# **Dataset Overview**
**FEATURES**
| Column | Description (EN) | Deskripsi (ID)
| -- | --- | ---
| Customer ID | Unique ID to each customer | ID unik setiap pelanggan
| Gender | Whether the customer is a male or a female | Jenis kelamin pelanggan
| Senior Citizen | Whether the customer is a senior citizen or not | Apakah pelanggan adalah warga lanjut usia
| Partner | Whether the customer has a partner or not | Apakah pelanggan memiliki pasangan
| Dependents | Whether the customer has dependents or not | Apakah pelanggan memiliki tanggungan
| Tenure | Number of months the customer has stayed with the company | Lama waktu pelanggan sudah aktif/berlangganan hingga sekarang (bulan)
| Phone Service | Whether the customer has a phone service | Apakah pelanggan menggunakan layanan telepon (rumah)
| Multiple  Lines | Whether the customer has multiple phone lines | Apakah pelanggan memiliki beberapa jalur telepon
| Internet Service | Customer’s internet service provider | Penyedia layanan internet pelanggan (DSL, Fiber optic, no)
| Online Security | Whether the customer has online security | Apakah pelanggan memiliki keamanan online (firewall/antivirus/VPN)
| Online Backup | Whether the customer has online backup service | Apakah pelanggan menggunakan penyimpanan cadangan pada daring (cloud)
| Device Protection | Whether the customer has device protection plan | Apakah pelanggan memiliki perlindungan perangkat
| Tech Support | Whether the customer has tech support service | Apakah pelanggan mendapat bantuan teknis
| Streaming TV | Whether the customer uses streaming TV service | Apakah pelanggan mendapat layanan TV digital
| Streaming Movies | Whether the customer uses streaming movies service | Apakah pelanggan menggunakan layanan streaming film
| Contract | The contract term of the customer  | Jangka waktu kontrak pelanggan (bulanan/tahunan)
| Paperless Billing | Whether the customer receives paperless billing | Apakah pelanggan menerima tagihan digital
| Payment Method | Customer’s payment method | Metode pembayaran
| Monthly Charges | Monthly billing amount charged to the customer | Biaya langganan per bulan
| Total Charges | Total amount charged over the entire contract | Total biaya yang telah dibayar sejak awal berlangganan
| Churn | Indicates whether the customer has churned | Apakah pelanggan terindikasi berhenti berlangganan

# **Methodology**
1. **Data Understanding & Preparation**
2. **Exploration Data Analysis (EDA)**
3. **Feature Engineering**
4. **Preprocessing**
5. **Model Benchmarking**
6. **Hyperparameter Tuning** (RandomizedSearchCV)
7. **Test Data with Best Model**
8. **Model Explainability**

---

# **Conclusion**
??

# **Recommendations**
Based on the modeling results and interpretation of the most important features, several recommendations can be made:

---

# **Link Tableau**
https://public.tableau.com/views/TurningChurnIntoOpportunityAStrategicAnalysisofTelcoCustomerBehavior/TurningChurnIntoOpportunityAStrategicAnalysisofTelcoCustomerBehavior?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
