import datetime
import streamlit as st # Import Streamlit library for creating the web app
import numpy as np # Import numpy for numerical operations
import sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
# Set the title,of the app
st.title("Title:Bio Data")
#Display a short introductory message
st.write("This is my first web app.")
#Create input fields for user data collection
first_name = st.text_input("First Name") # Text input for entering first name
last_name = st.text_input("Last Name")
gender= st.selectbox("Gender",["Male","Female"])
age = st.number_input("Your Age",0, 100,30,1)
dob = st.date_input("your Birthday",
                    value=datetime.date(1985,1,1),
                    min_value=datetime.date(1900,1,1),
                    max_value=datetime.date.today())
martial_status = st.radio("Martial Status",["Single","Married"])
years_of_experience= st.slider("Years of experience", 0,40)
education = st.selectbox("Education Level",["High school","Bachelor","Master","PhD"])
job_title = st.selectbox("Job Title",["software Engineer","Data Analyst","Manager","Teacher","Senior Scientist","Financial Analyst","Accountant","CEO","Business Analyst"])
#Adding a profile picture upload option
# profile picture upload
profile_pic = st.file_uploader("Upload profile picture",type=["jpg","png","jpeg"])
#Display the uploaded image
if profile_pic:
    st.image(profile_pic, caption="profile Picture",width=150)
    #Checks if a file has been uploaded
    #Display the image using st.image(profile_pic, caption="Profile Picture", width=150)
    # submit Button-when the user clicks Submit, their details are displayed.
if st.button("Submit",key="submit_button"):
    st.success("Here is your bio data:")
 #Display user details below the success message
    st.write(f"Name:{first_name}{last_name}")
    st.write(f"Gender:{gender}")
    st.write(f"Age:{age}")
    st.write(f"Date of birth:{dob}")
    st.write(f"Martial status:{martial_status}")
    st.write(f"Years of Experience:{years_of_experience}")
    st.write(f"Education:{education}")
    st.write(f"job_title:{job_title}")
# saving user data
# store data in a dictionary when the user clicks the "Submit" button
if st.button("Submit"):
    user_data ={
        "First Name": first_name,
        "Last_name": last_name,
        "Gender":gender,
        "Age":age,
        "Date of birth":str(dob),
        "Martial Status":martial_status,
        "Years of Experience": years_of_experience
    } #Convert the dictionary into a Pandas DataFrame
    df = pd.DataFrame([user_data])
    #Append data to the CVS file
    df.to_csv("user_data.csv",mode="a", header=False, index=False)
    #show a success message after saving the data
    st.success("Your data has been saved")
#salary Prediction
#Sample dataset for training(Years of Experience vs salary)
file_path = "/workspaces/gdp-dashboard/salaryData.csv"
salary_data = pd.read_csv("/workspaces/PROJECT-2/salaryData.csv")
#Check for missing values
salary_data = salary_data.dropna(subset={"Salary"})
#Impute missing values
imputer = SimpleImputer(strategy='mean')
salary_data[["Years of Experience"]] = imputer.fit_transform(salary_data[["Years of Experience"]])
#Prepare features and target
X = salary_data[["Years of Experience"]]
y = salary_data["Salary"]
#Train the model
model = LinearRegression()
model.fit(X,y)
#Salary prediction section
if st.button("Predict Salary", key = "predict_salary"):
        predicted_salary= model.predict(np.array([[years_of_experience]]))[0]
        st.success(f"Estimated Salary: ${predicted_salary:,.2f}")