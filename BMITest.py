
import pandas as pd
a=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82},{"Gender": "Female",
"HeightCm": 169, "WeightKg": 83}]




def bmi():

    data={}
    underweight=[]
    Normalweight=[]
    Overweigt=[]
    Moderatelyobese=[]
    Severlyobese=[]
    verySeverlyobese=[]
    bmi=0
    for ele in a:
        b=(ele['HeightCm'])/100.0
        c=(ele['WeightKg'])

        d=c/(b**2)

        bmi=d
        
        if (bmi < 18.5):
            underweight.append(ele['Gender'])
            data['Gender underweight']=(underweight)
            data['body mass index underweight']=bmi
            data['Consider underweight']="underweight"
            data['Malnutrition risk']="Malnutrition risk"
            

        elif ( bmi >= 18.5 and bmi < 24.9):
           Normalweight.append(ele['Gender'])
           data['Gender Normalweight ']=(Normalweight)
           data['body mass index Normalweight']=bmi
           data['Consider Normalweight']="Normalweight"
           data['Low risk']="Low risk"

        elif ( bmi >= 25 and bmi < 29.9):
            Overweigt.append(ele['Gender'])
            data['Gender Overweigt']=(Overweigt)
            data['body mass index Overweigt']=bmi
            data['Consider Overweigt']="Overweigt"
            data['Enhanced risk']="Enhanced risk"

        elif ( bmi >= 30 and bmi < 34.9):
            Moderatelyobese.append(ele['Gender'])
            data['Gender Moderatelyobese']=(Moderatelyobese)
            data['body mass index Moderatelyobese']=bmi
            data['Consider Moderatelyobese']="Moderatelyobese"
            data['Medium risk']="Medium risk"
            

        elif ( bmi >= 35 and bmi < 39.9):
            Severlyobese.append(ele['Gender'])
            data['Gender Severlyobese']=(Severlyobese)
            data['body mass index Severlyobese']=bmi
            data['Consider Severlyobese']="Severlyobese"
            data['High risk']="High risk"

        elif ( bmi >= 40):
            verySeverlyobese.append(ele['Gender'])
            data['Gender verySeverlyobese']=(verySeverlyobese)
            data['body mass index Severlyobese']=bmi
            data['Consider Severlyobese']="verySeverlyobese"
            data['Very high risk']="Very high risk"

    print ("Overwiegt>>>>>>>>>>>> :",len(data['Gender Overweigt']))
    for k,v in data.items():
        print (k,"  >>>>>>>>>>>>>> ", v)
    
                                  

    



            

        
            
        
    
bmi()
    
    
