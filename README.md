# GammaGroup_JC_DS_FT_JKT_28_FinalProject
# Turning Churn Into Opportunity: A Strategic Analysis of Telco Customer Behavior
Created by:
- **Muhammad Fachry Priambodo**
- **Aimar Mohammad Butragueno**
- **Gerald Pascal Ginting**

# **Context**
Telecommunication companies are now facing significant challenges in retaining customers amid increasingly fierce market competition. One of the most critical issues is customer churn, which occurs when customers stop using their services. Losing customers not only impacts revenue but also incurs substantial costs in acquiring new ones. In this context, the analyzed Telco company has historical customer data, including demographic information, services used, and payment behaviors. Leveraging this data, a comprehensive analysis was conducted to identify churn patterns and develop a predictive model to estimate the likelihood of churn in the future.

# **Problem Statement**
In the highly competitive telecommunications industry, customer retention has become a business priority that is equally — if not more — important than acquiring new customers. The cost of acquiring a new customer can be up to five times higher than the cost of retaining an existing one. Therefore, companies need to implement data-driven strategies to identify customers at risk of churn before it happens. Unfortunately, many companies still struggle with recognizing the early signs that a customer is about to churn, identifying the key factors that contribute most to a customer’s decision to leave, and implementing the right interventions quickly and efficiently. This is where the role of predictive analytics and machine learning becomes crucial.

# **Goals**
1. **Churn Understanding**  
   Identify the key factors that influence customer churn through exploratory analysis and predictive modeling.

2. **Customer Segmentation**  
   Cluster customers based on service usage, contract types, and payment behavior to uncover distinct personas and risk profiles.

3. **Revenue Optimization**  
   Quantify the financial impact of churn and explore how customer lifetime value (CLTV) is affected across segments.

4. **Operational Improvement**  
   Evaluate how services, billing methods, and contract structures correlate with churn, identifying levers for operational efficiency.

5. **Building a Machine Learning Model**  
   Building an accurate and interpretable machine learning–based churn prediction model.
   
6. **Providing Business Insights**  
   Building an accurate and interpretable machine learning–based churn prediction model.
   
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
This notebook is designed for marketing teams who seek a strategic understanding of churn dynamics and its implications for customer value and service design.
> Marketing Teams

# **Dataset Overview**
| Column | Description (EN) | Deskripsi (ID)
| -- | --- | ---
| Customer ID | Unique ID to each customer | ID unik setiap pelanggan
| Gender | Whether the customer is a male or a female | Jenis kelamin pelanggan
| Senior Citizen | Whether the customer is a senior citizen or not (0 = No, 1 = Yes) | Apakah pelanggan adalah warga lanjut usia (0 = Tidak, 1 = Ya)
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
1. Prioritize High Churn Score Customers for Active Retention
   - Business Actions:
      - Focus retention efforts (special offers, discounts, bonuses) on high-risk churn customers.
      - Create a “save offer” program for customers in their final month of active service.
     
   🎯 Expected Outcome:
      > Reduce churn through faster and more targeted interventions.

2. Offer Long-Term Contracts to Monthly Contract Customers
   - Business Actions:
      - Offer migration promos to annual contracts (e.g., 1-month free, extra data quota).
      - Prioritize targeting customers who’ve subscribed for more than 6 months.

   🎯 Expected Outcome:
      > Reduce churn and increase long-term customer loyalty.

3. Migrate Manual Payments to Digital / Auto-Pay Methods
   - Business Actions:
      - Encourage customers to switch to digital payment methods (e-wallets, debit, etc.).
      - Offer cashback or waive admin fees for those who migrate.
   
   🎯 Expected Outcome:
      > More stable customers, smoother payments, and reduced churn risk.
   
4. Educate New Customers
   - Business Actions:
      - Send onboarding content: tutorials, service benefit tips, first-time usage promos.
      - Follow up after the first 30 days of subscription.
   🎯 Expected Outcome:
      > New customers feel more engaged → lower churn in the first 3 months.
   
5. Segment Campaigns by Demographic & Service Features
   - Business Actions:
      - For senior customers: provide simple, easy-to-use service packages.
      - For customers without tech support: offer discounted bundled upgrades.
      - For customers without internet: promote add-ons with special pricing.
   
   🎯 Expected Outcome:
      > More personalized campaigns → higher relevance and engagement → reduced churn.

6. Activate Payment Reminders & Early Warnings
   - Business Actions:
      - Send notifications or SMS reminders 5 days before payment due date.
      - Add an “auto-reminder” feature for new customers.
      - Set alerts for payments delayed over 1 week — flag as potential churn risk.
   
   🎯 Expected Outcome:
      > Reduce churn caused by late payments & improve payment discipline.

7. Tenure- and Usage-Based Loyalty Program
   - Business Actions:
      - Reward loyal customers annually (e.g., 1-month discount, partner vouchers).
      - Launch a “Loyalty Milestone” program with membership levels (Bronze, Silver, Gold) based on tenure and usage.
   
   🎯 Expected Outcome:
      > Customers feel valued → less likely to switch to competitors.

8. Regularly Monitor Churn and Evaluate the Model
   - Business Actions:
      - Schedule churn model retraining every 3–6 months.
      - Track important features (e.g., MonthlyCharges, Contract) and how they change over time.
      - Use feedback from marketing and customer service teams to improve model accuracy.
   
   🎯 Expected Outcome:
      > Churn predictions remain relevant, accurate, and responsive to customer behavior changes.
---

# **Link Tableau**
https://public.tableau.com/views/TurningChurnIntoOpportunityAStrategicAnalysisofTelcoCustomerBehavior/TurningChurnIntoOpportunityAStrategicAnalysisofTelcoCustomerBehavior?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
