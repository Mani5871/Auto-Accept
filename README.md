
This project allows you to accept all your Linkedin connection requests in a single click

Steps to Run this project
Step 1: Run the below commands to install dependencies

  
  pip install streamlit
  pip install selenium
  
 Step 2: Change the path of Chrome Driver according to the location of file in line 14 of app.py
 
  driver = webdriver.Chrome(executable_path=r"C:\Users\HP\Desktop\Projects\Auto-Accept\chromedriver.exe")
  Change the path in executable path depending on the location of your project
  
Step 3: Run the project by the below command
  streamlit run app.py
  
  
 Enter login credentials and you are good to go
