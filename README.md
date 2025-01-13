# Toxic-Instagram-Comments

My Weekend with Instagram: Turning Chaos into a Deployed ML Solution
In just two days, I took on the challenge of building and deploying a Social Media Toxicity Prediction System. This wasn’t just another project—it was a meticulous blend of data engineering, deep learning, API integration, and cloud deployment, with the ultimate goal of creating an end-to-end scalable solution for real-time analysis.

Here’s an overview of the journey:

# 📊 Data Preparation: From Raw to Ready
Working with real-world data often means tackling noise, imbalance, and inconsistency. The dataset was no exception—it was messy, skewed, and full of missing or irrelevant entries.

I implemented advanced preprocessing techniques like text normalization, stopword removal, and tokenization to clean the data.
To address the severe class imbalance, I employed SMOTE (Synthetic Minority Oversampling Technique) and stratified sampling, ensuring the model would generalize effectively across all toxicity levels.
The result was a well-structured dataset that laid a strong foundation for robust model training.

# 🧠 Model Development: Harnessing Bidirectional Context
For this project, I leveraged the power of Bidirectional LSTM (BiLSTM) networks combined with a feed-forward neural network to capture contextual relationships in text from both past and future tokens.

The model was trained for 1000 epochs with optimizations like learning rate schedulers and early stopping, which ensured convergence without overfitting.
At epoch 450, the model achieved optimal performance, balancing precision and recall for detecting nuanced toxicity patterns.
Additional layers, including Dropout, were added to prevent overfitting, and Glove embeddings were utilized for semantic richness in text representation.
🔗 API Integration with Apify: Real-Time Data Handling
A major challenge in building such systems is integrating real-time data streams. My past experiences with Instagram scrapers, including issues with Meta’s restrictions, taught me valuable lessons.

Using Apify’s robust APIs, I seamlessly integrated live comment feeds from Instagram.
This step provided real-world data for validation, bridging the gap between theory and application.
# ☁️ Deployment on AWS: From Local to Cloud
Deploying the model was another layer of complexity that required careful orchestration:

# Dockerization:
Created a lightweight Docker image containing the trained model, dependencies, and the Streamlit-based interface for interaction.
Pushed the Docker image to Docker Hub for easy accessibility.
AWS EC2 Setup:
Launched an EC2 instance and configured security groups to allow custom TCP access on port 8501.
Pulled the Docker image from Docker Hub and ran the container in a controlled environment.
Real-Time Access:
The deployed system is now live, hosted on AWS, capable of processing Instagram comments in real time to predict toxicity levels with high accuracy.
This deployment showcases the seamless synergy between containerization and cloud infrastructure for creating scalable, real-time solutions.

# Key Takeaways
This project deepened my understanding of:
Advanced text preprocessing and handling imbalanced datasets.
Architecting and optimizing deep learning models for NLP tasks.
The importance of robust API integration for real-time systems.
Deploying end-to-end solutions using Docker and AWS cloud infrastructure.
