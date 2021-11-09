import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

def inputs():
    Gender = st.selectbox("Select Gender",tuple(Gender_label.keys()))
    cp = st.selectbox("Select Type of Chest Pain",tuple(cp_label.keys()))
    fbs = st.selectbox("Select whether fasting blood sugar is greater than 120mg/dl",tuple(fbs_label.keys()))
    restecg = st.selectbox("Select resting electrocardiographic results",tuple(restecg_label.keys()))
    exang = st.selectbox("exercise induced angina",tuple(exang_label.keys()))
    slope = st.selectbox("The slope of the peak exercise ST segment",tuple(slope_label.keys()))
    ca = st.selectbox("number of major vessels (0-3) colored by flourosopy",tuple(ca_label.keys()))
    thal = st.selectbox("thal: 3 = normal; 6 = fixed defect; 7 = reversable defect",tuple(thal_label.keys()))
   
    #encoding
    v_Gender=get_value(Gender,Gender_label)
    v_cp=get_value(cp,cp_label)
    v_fbs=get_value(fbs,fbs_label)
    v_restecg=get_value(restecg,restecg_label)
    v_exang=get_value(exang,exang_label)
    v_slope=get_value(slope,slope_label)
    v_ca=get_value(ca,ca_label)
    v_thal=get_value(thal,thal_label)
    
    age = st.number_input("Age")
    trestbps=st.number_input("Resting Blood Pressure in mm Hg")
    chol=st.number_input("Serum cholestoral in mg/dl")
    thalach=st.number_input("Maximum heart rate achieved")
    oldpeak=st.number_input("ST depression induced by exercise relative to rest")
    
    
    data=np.array([[age,v_Gender,v_cp,trestbps,chol,v_fbs,v_restecg,thalach,v_exang,oldpeak,v_slope,v_ca,v_thal]]).astype(np.int64)
    
    return data
    

Gender_label={'Male':1,'Female':0}
cp_label={'Type 1-Typical angina':0,'Type 2-Atypical angina':1,'Type 3-Non angina pain':2,'Type 4-Asymptomatic':3}
fbs_label={'True':1,'False':0}
restecg_label={'Normal':0,'Having_ST_T wave abnormal':1,'left ventricular hypertrophy':2}
exang_label={'Yes':1,'No':0}
slope_label={'Upsloping':0,'Flat':1,'Down sloping':2}
ca_label={'0':0,'1':1,'2':2,'3':3}
thal_label={'0':0,'1':1,'2':2,'3':3}

#get the value
def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val==key:
            return value

def main():
    html_temp = """
    <div style="background-color:#006400;padding:10px">
    <h2 style="color:white;text-align:center;">Heart Disease Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://www.heartfoundation.org.au/getmedia/da58c9f7-d4ba-42a6-bf65-9c38f6911b22/cardiac_blues.png");
        background-size:cover;
    }
   .sidebar .sidebar-content {
        background: url("https://www.heartfoundation.org.au/getmedia/da58c9f7-d4ba-42a6-bf65-9c38f6911b22/cardiac_blues.png")
    }
    </style>
    """,
    unsafe_allow_html=True
)
    input=inputs()
    
    if st.button("predict"):
        prediction=model.predict(input)
        pred='{0}'.format(prediction[0])
        if pred == '1':
            st.header("Suffering from heart disease")
        else:
            st.header("Not suffering from heart disease")
            
if __name__ == '__main__':
    main()
