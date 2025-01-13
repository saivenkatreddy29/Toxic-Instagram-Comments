# Toxic-Instagram-Comments

In just two days, I took on the challenge of building and deploying a Social Media Toxicity Prediction System. This wasn’t just another project—it was a meticulous blend of data engineering, deep learning, API integration, and cloud deployment, with the ultimate goal of creating an end-to-end scalable solution for real-time analysis.
📊 𝐃𝐚𝐭𝐚 𝐏𝐫𝐞𝐩𝐚𝐫𝐚𝐭𝐢𝐨𝐧: 𝐅𝐫𝐨𝐦 𝐑𝐚𝐰 𝐭𝐨 𝐑𝐞𝐚𝐝𝐲
Starting with noisy, imbalanced data, I implemented advanced preprocessing techniques like tokenization, stop word removal, and SMOTE for balancing classes. This created a clean and structured dataset for robust model training.
🧠 𝐌𝐨𝐝𝐞𝐥 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐦𝐞𝐧𝐭: 𝐇𝐚𝐫𝐧𝐞𝐬𝐬𝐢𝐧𝐠 𝐁𝐢𝐝𝐢𝐫𝐞𝐜𝐭𝐢𝐨𝐧𝐚𝐥 𝐂𝐨𝐧𝐭𝐞𝐱𝐭
I designed a Bidirectional LSTM (BiLSTM) architecture with a feed-forward neural network, enabling contextual understanding of text from both directions. Using learning rate schedulers and early stopping, the model reached optimal performance at 450 epochs, well before the planned 1000.
🔗 𝐀𝐏𝐈 𝐈𝐧𝐭𝐞𝐠𝐫𝐚𝐭𝐢𝐨𝐧 & 𝐃𝐞𝐩𝐥𝐨𝐲𝐦𝐞𝐧𝐭
For real-time data handling, I integrated Apify APIs to fetch Instagram comments seamlessly, overcoming challenges faced in previous scraping projects.
On the deployment front:
Built a Docker image and hosted it on Docker Hub.
Configured an AWS EC2 instance with custom security settings and deployed the app via Streamlit for real-time access.
This project enhanced my skills in NLP, model optimization, API integration, and cloud deployment, all accomplished in just two days. Passion and focus truly unlock incredible possibilities. 
