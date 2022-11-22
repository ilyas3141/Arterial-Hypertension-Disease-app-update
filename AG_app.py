import streamlit as st




st.write("""
# Arterial Hypertension Disease Diagnosis app
This app gives a diagnosis for **Arterial Hypertension Disease**!

""")

st.sidebar.header('Patient Input Features')




def diagnosis():
    risk_count=0
    pom_count=0
    ssz_count=0
    db=0
    
    
    gender=st.sidebar.selectbox('Gender',('Male','Female'))
    
    age=st.sidebar.slider('Age', 0,110,43)
    smoking=st.sidebar.selectbox('Smoking',('Yes','No'))
     
    hyperchol=st.sidebar.selectbox('Dyslipidemia',('Yes','No'))
    
    prediabet=st.sidebar.selectbox('Prediabet', ('Yes','No'))
    hyperur=st.sidebar.selectbox('Hyperuricemia',('Yes','No'))
    
    height=st.sidebar.slider('Height(cm)', 0,250,170)
    weight=st.sidebar.slider('Weight(kg)', 0,250,60)
    bmi=weight/((0.01*height)**2)
    
    
    abdominal=st.sidebar.slider('Wait circumference(cm)', 0,150,70)
    chss=st.sidebar.slider('Heart rate per minute', 0,150,70)
    
    semeyniy=st.sidebar.selectbox('Family history of early CVD', ('Yes','No'))
    menopause=st.sidebar.selectbox('Early menopause', ('Yes','No'))
    psycho_social=st.sidebar.selectbox('Psychosocial and economic factors', ('Yes','No'))
    
    
    sys=st.sidebar.slider('Systolic blood pressure (mm Hg)', 0,240,130)
    diasst=st.sidebar.slider('Diastolic blood pressure (mm Hg)', 0,160,87)
    pulse_press=sys-diasst
    
    ekg=st.sidebar.selectbox('Signs of LVH on the ECG', ('Yes','No'))
    echoekg=st.sidebar.selectbox('Signs of LVH on echocardiography', ('Yes','No'))

    sys_leg_cond=st.sidebar.selectbox('Has the Ankle-Brachial Index been assessed?', ('Yes','No'))
    
    if sys_leg_cond=='Yes':
        sys_leg=st.sidebar.slider('Ankle systolic blood pressure (mmHg)',0,240,120)
        shoulder_index=sys_leg/sys
        if shoulder_index < 0.9:
            pom_count+=1
    
    hbp=st.sidebar.slider('Glomerular Filtration Rate(ml/min/173m\u00b2)', 0,120,61)
   
    mau=st.sidebar.slider('Level of Microalbuminuria (mg per day)', 0,400,301)
  
    albu_kreat=st.sidebar.slider('The ratio of albumin to creatinine in single urine (mg / mmol)', 0,400,302)
    
   
    sahar=st.sidebar.selectbox('The presence of diabetes',('Yes','No'))
    
    
    #осложнения
    cerebro_vasc=st.sidebar.selectbox('Presence of cerebrovascular disease', ('Yes','No'))
    ibs=st.sidebar.selectbox('Presence of coronary heart disease', ('Yes','No'))
    sn=st.sidebar.selectbox('Presence of heart failure', ('Yes','No'))
    fibrilationechoekg=st.sidebar.selectbox('Presence of atrial fibrillation', ('Yes','No'))
    peripher=st.sidebar.selectbox('The presence of clinically manifest lesions of peripheral arteries', ('Yes','No'))
    
    diag=''
    
    if age >65 and gender == 'Female':
        risk_count+=1
    elif age >55 and gender == 'Male':
        risk_count+=1
    if smoking=='Yes':
        risk_count+=1
    if hyperchol=='Yes':
        risk_count+=1
    if prediabet=='Yes':
        risk_count+=1
    if hyperur=='Yes':
        risk_count+=1
    if bmi>=25:
        risk_count+=1
    if abdominal>=102 and gender=='Male':
        risk_count+=1
    elif abdominal>=88 and gender=='Female':
        risk_count+=1    
    if chss>=80:
        risk_count+=1   
    if semeyniy =='Yes':
        risk_count+=1
    if menopause=='Yes':
        risk_count+=1
    if psycho_social=='Yes':
        risk_count+=1
        
    if sahar=='Yes':
        db+=1
        
        
    
    if pulse_press>=60:
        pom_count+=1
    if ekg=='Yes':
        pom_count+=1
    if echoekg=='Yes':
        pom_count+=1
    
    if (hbp<=60) & (hbp>=30):
        pom_count+=1
    elif hbp<30:
        ssz_count+=1
    if (mau<=300) & (mau>=30):    
        pom_count+=1
    elif mau>300: 
        ssz_count+=1
    if (albu_kreat<=300) & (albu_kreat>=30):  
        pom_count+=1
    elif albu_kreat>300: 
        ssz_count+=1    
        
    
    if cerebro_vasc=='Yes':
        ssz_count+=1
    if ibs=='Yes':
        ssz_count+=1
    if sn=='Yes':
        ssz_count+=1
    if fibrilationechoekg=='Yes':
        ssz_count+=1
    if peripher=='Yes':
        ssz_count+=1
        

        
    #STAGE 1, 0 FACTORS
    if (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Hypertension Disease, Degree 0, Stage 1, Low Risk(0 factors)'
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag= 'Hypertension Disease, Degree 1, Stage 1, Low Risk(0 factors)'    
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag= 'Hypertension Disease, Degree 2, Stage 1, Moderate Risk(0 factors)'
    
    elif (risk_count==0)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Hypertension Disease, Degree 3, Stage 1, High Risk(0 factors)'  
    
    
    #1-2 FACTORS
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Hypertension Disease, Degree 0, Stage 1, Low Risk(1-2 factors)'
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag= 'Hypertension Disease, Degree 1, Stage 1, Moderate Risk(1-2 factors)'
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag= 'Hypertension Disease, Degree 2, Stage 1, Moderate-High Risk(1-2 factors)'  
       
    elif (risk_count<=2)&(risk_count>=1)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Hypertension Disease, Degree 3, Stage 1, High Risk(1-2 factors)'    
        
        #3+ FACTORS
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys<=139)&(diasst<=89)):
        diag= 'Hypertension Disease, Degree 0, Stage 1, Low-Moderate Risk(3+ factors)'    
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
        diag='Hypertension Disease, Degree 1, Stage 1, Moderate-High Risk(3+ factors)'     
    
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
        diag='Hypertension Disease, Degree 2, Stage 1, High Risk(3+ factors)'
    elif (risk_count>=3)&(pom_count==0)&(ssz_count==0)&(db==0)&((sys>=180)|(diasst>=110)):
        diag= 'Hypertension Disease, Degree 3, Stage 1, High Risk(3+ factors)'    
    
    
    #STAGE 2-3
    elif (ssz_count==0):
        if ((pom_count>0)&(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Hypertension Disease, Degree 0, Stage 3, Very High Risk'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Hypertension Disease, Degree 1, Stage 3, Very High Risk' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Hypertension Disease, Degree 2, Stage 3, Very High Risk'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Hypertension Disease, Degree 3, Stage 3, Very High Risk' 
                #STAGE 2
        elif ((pom_count>0)|(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Hypertension Disease, Degree 0, Stage 2, High-Moderate Risk'
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):   
                diag= 'Hypertension Disease, Degree 1, Stage 2, High Risk'
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Hypertension Disease, Degree 2, Stage 2, High Risk'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):  
                diag= 'Hypertension Disease, Degree 3, Stage 2, Very High Risk'
    elif (ssz_count>0):
        if ((pom_count>0)&(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Hypertension Disease, Degree 0, Stage 3, Very High Risk'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Hypertension Disease, Degree 1, Stage 3, Very High Risk' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Hypertension Disease, Degree 2, Stage 3, Very High Risk'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Hypertension Disease, Degree 3, Stage 3, Very High Risk' 
        elif ((pom_count>0)|(db>0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Hypertension Disease, Degree 0, Stage 3, Very High Risk'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Hypertension Disease, Degree 1, Stage 3, Very High Risk' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Hypertension Disease, Degree 2, Stage 3, Very High Risk'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Hypertension Disease, Degree 3, Stage 3, Very High Risk' 
        elif ((pom_count==0)&(db==0)):
            if ((sys<=139)&(diasst<=89))&((risk_count==0)|(risk_count>0)):
                diag= 'Hypertension Disease, Degree 0, Stage 3, Very High Risk'  
            elif ((risk_count==0)|(risk_count>0))&(((sys<=159)&(diasst<=99)&(diasst>=90))|((diasst<=89)&(sys<=159)&(sys>=140))):
                diag= 'Hypertension Disease, Degree 1, Stage 3, Very High Risk' 
            elif ((risk_count==0)|(risk_count>0))&(((sys<=179)&(diasst<=109)&(diasst>=100))|((diasst<=99)&(sys<=179)&(sys>=160))):
                diag= 'Hypertension Disease, Degree 2, Stage 3, Very High Risk'
            elif ((risk_count==0)|(risk_count>0))&((sys>=180)|(diasst>=110)):
                diag= 'Hypertension Disease, Degree 3, Stage 3, Very High Risk'        
             
 
        
            
  
    return diag  


result=diagnosis()



st.subheader('Diagnosis')
if st.button('See diagnosis'):
    st.write(result)


