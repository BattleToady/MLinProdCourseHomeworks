# MLinProdCourseHomeworks

Project for course "Machine Learning in Production"

# ML Design Docs

## 1. Overview
This project should solve task of predicting entrace in university(classification) with realistic predict proba to give more information to applicants. I will use ML models, what will be trained on data from previous years campaigns,

## 2. Motivation
In Ukraine there are more then 250k applicants annually. Majority of them would like to have app which could predict their entrace on budget form and give information as probability of it.

## 3. Success metrics
It's seasonal need with low customer lifetime but with high demand. So, our choice is YAU(Yearly active users).

## 4. Requirements & Constraints
Functional requirements: app has to give prediction of applicant's entrance based on his input.

Non-functional/technical requirements: api server(GCP), web input form and ml model. Saving inputs of users into db for future analytics.
Cost < $x * 250k(count of customers) * 7(mean count of customer requests) < $3 * 1 750 000(api calls)
p99 latency < yms

### 4.1 What's in-scope & out-of-scope?
-

## 5. Methodology
### 5.1. Problem statement
supervised learning(classification) + probability calibration

### 5.2. Data
Parsing data from abit-poisk.org

### 5.3. Techniques
Cleaning(NaN, Duplicates, Outliers)
Scaling(MinMaxScaler)
UnderSampler(to remove imbalace of classes)
Feature Engineering(getting the ratio of mark to average mark) 
Some classic model(from sklearn)

### 5.4. Experimentation & Validation
Group KFold + F1-score - offline

### 5.5. Human-in-the-loop
-

## 6. Implementation
### 6.1. High-level design
![image](https://github.com/BattleToady/MLinProdCourseHomeworks/assets/89700552/6995971c-1fe7-4563-8b81-870826c8e637)

### 6.2. Infra
GCP

### 6.3. Performance (Throughput, Latency)
How will your system meet the throughput and latency requirements? Will it scale vertically or horizontally?

### 6.4. Security
How will your system/application authenticate users and incoming requests? If it's publicly accessible, will it be behind a firewall?

### 6.5. Data privacy
How will you ensure the privacy of customer data? Will your system be compliant with data retention and deletion policies (e.g., GDPR)?

### 6.6. Monitoring & Alarms
How will you log events in your system? What metrics will you monitor and how? Will you have alarms if a metric breaches a threshold or something else goes wrong?

### 6.7. Cost
How much will it cost to build and operate your system? Share estimated monthly costs (e.g., EC2 instances, Lambda, etc.)

### 6.8. Integration points
How will your system integrate with upstream data and downstream users?

### 6.9. Risks & Uncertainties
Risks are the known unknowns; uncertainties are the unknown unknows. What worries you and you would like others to review?

## 7. Appendix
### 7.1. Alternatives
What alternatives did you consider and exclude? List pros and cons of each alternative and the rationale for your decision.

### 7.2. Experiment Results
Share any results of offline experiments that you conducted.

### 7.3. Performance benchmarks
Share any performance benchmarks you ran (e.g., throughput vs. latency vs. instance size/count).

### 7.4. Milestones & Timeline
What are the key milestones for this system and the estimated timeline?

### 7.5. Glossary
Define and link to business or technical terms.

### 7.6. References
Add references that you might have consulted for your methodology.
