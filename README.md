### DATA-ENGINEERING-PROJECT
---
## PROJECT 3

## Team Members: 
Elis okala -
Kiwaski Nix -
Mina Agyen -
Monique Reid 

## PROJECT OVERVIEW 
As we move into summer, the need for in-home entertainment is at an all-
time high. Families have gathered around the television (TV) for decades to 
enjoy movies or shows. With the introduction of companies like Netflix, 
entertainment has never been more accessible. Whether bonding over a love
story or quivering with fear over a horror movie, Netflix continues to provide 
captivating streaming options. Our goal was to gather relevant data from 
Netflix movies and TV shows, transform it into a usable format, and load it 
into a database for analysis and reporting purposes. This dataset was chosen
for its complexity and diversity, allowing us to showcase our ETL workflow 
skillset.

## OBJECTIVES
For this track, our group choose the data engineering track. We are tasked with the following:
1 - Find a dataset that contains at least 100 records.
2 - Design an ETL workflows to ingest data in a SQL or NoSQL database (PostgreSQL, MongoDB, SQLite, etc). 
3 - Design a Flask Api app with JSON output to facilitate user's interactions with our work materials
4 - Research a library not covered in class related to data engineering. 

## USER'S INTERACTIONS
We designed a flask app to facilitate user's interaction with our project. The flask app is a combination of 4 different routes referencing each table in our database. We shared a link to our git repository which users can follow and get access to our work material.

## WHY SQLite?
We choose to use SQLite for various reasons:
1 - Open source and free: SQLite is accessible to developers of all levels.
2 - Serverless: SQLite doesn't require a separate database server, which can eliminate the need for complex configurations and make it cheaper for smaller projects like ours.
3 - Multiple instances: Multiple instances of the same app can run simultaneously without issue.
4 - Data transfer: SQLite databases can facilitate data transfer between systems. Given that we were going to transfer to flask to allow users interactions, SQLite is the right fits for our needs.

## PANDAS_ERD
We performed intensive research for a new library that was not discussed in class and decided to use the PANDAS_ERD as our library to sketch an Entity-Relationship Diagram (ERD). Pandas_erd is a powerful and specialized tool designed to simplify the process of visualizing the relationships within data stored in pandas DataFrames. It integrates seamlessly with pandas, leveraging its robust data manipulation capabilities to analyze and structure data relationships.
The code allows users to generate comprehensive ERDs by automatically detecting relationships between different columns. It supports various types of relationships, including one-to-one, one-to-many, and many-to-many, providing a clear and accurate representation of data structures. This visualization is crucial for understanding complex datasets, identifying potential data integrity issues, and designing efficient database schemas.
By immersing ourselves in this project, we enhanced our skills in data collection, organization, analysis, and visualization. The use of pandas_erd specifically enabled us to better understand the underlying structures and connections within our data, which can facilitated more informed decision-making and clearer communication of our findings. Additionally, working with this code introduced us to advanced features of pandas, deepening our proficiency in data science tools and techniques.


## ETHICAL CONSIDERATIONS
There were two paramount ethical considerations for our project. The first ethical consideration was the source of our data. When obtaining data, privacy or consent (where people ask permission) are paramount. Our dataset was retrieved from Kaggle, a popular online platform and community for data scientists and machine learning practitioners. It provides a collaborative environment where users can find and share datasets, participate in competitions, and learn from one another. Using datasets from Kaggle offers several ethical benefits that ensure responsible data sourcing, utilization, and sharing. Kaggle provides transparent documentation about data origins and collection methods, which promotes informed and ethical use. Compliance with legal standards, such as data privacy laws, is enforced, protecting individuals' rights. The community review system allows for scrutiny and feedback, addressing potential ethical concerns like biases or inaccuracies. Kaggle promotes open science and collaboration, enhancing scientific integrity by allowing researchers to validate and reproduce findings. The platform's focus on educational opportunities aids in the ethical development of future data scientists. Moreover, Kaggle often supports projects with socially beneficial purposes, encouraging ethical applications of data science. Many datasets on Kaggle are curated for diversity and inclusion, helping to mitigate biases and ensure fair model performance across different populations. Additionally, data anonymization processes protect personal information, ensuring privacy. These factors collectively help ensure that data is used responsibly and ethically in various projects.

The second ethical consideration was referencing for data source(s) and any code that wasn’t ours. Proper attribution and referencing are fundamental to maintaining academic and professional integrity. By clearly acknowledging the sources of data and any borrowed code, we demonstrate respect for the original creators' intellectual property and contributions. This practice helps avoid plagiarism, ensuring that we give credit where it is due. Furthermore, accurate referencing provides transparency, allowing others to trace the origins of our data and understand the basis of our methodologies. It enhances the reproducibility of our work, as others can access the same sources and replicate our results, which is crucial for the scientific process. Additionally, it fosters a culture of openness and honesty within the research community, encouraging collaborative efforts and the sharing of knowledge. By adhering to proper referencing standards, we not only uphold ethical norms but also contribute to the overall credibility and reliability of our project. 

## SUMMARY  
Netflix is a streaming application that is very popular with all generations. Netflix allows users to access a very diverse selection of local and international movies and films. The objective of this project is to include data cleansing and organization, analysis, and engineering. We will import data from kaggle.com, design the tables to hold the data from the CSV files, and import the CSV files into an SQL database. In summary, diligent referencing for data sources and external code is essential for ethical research practices, ensuring that the contributions of others are properly acknowledged and that our work can be trusted and verified by the wider community.

## REFERENCES AND METADATA    
Special thanks to our instructional team for their guidance in deciding which library suited our needs best. 

Data: https://www.kaggle.com/datasets/shivamb/netflix-shows/data	

Image: https://sql.sh/wp-content/uploads/2014/04/sqlite-sgbd-500px.png

































































