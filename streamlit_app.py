#Import necessary libraries..
from tkinter import *
from tkinter import messagebox
from ml_models import knn_model,rf_model,nb_model,dt_model
import db_operations as db
import re
# Define symptoms and diseases
symptoms_list=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

diseases = ['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
    'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
    ' Migraine','Cervical spondylosis',
    'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
    'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
    'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
    'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
    'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
    'Impetigo']

#Creation of GUI..
root = Tk()
root.title("Disease Predictor")
root.configure(background='#42f5f5')
root.iconbitmap('favicon.ico')
root.geometry('800x600')

# Variables
Name = StringVar()
Symptom1 = StringVar(value="Choose symptom")
Symptom2 = StringVar(value="Choose symptom")
Symptom3 = StringVar(value="Choose symptom")
Symptom4 = StringVar(value="Choose symptom")
Symptom5 = StringVar(value="Choose symptom")
pred_var = StringVar()

#Method to predict disease..
def predict_disease(model):
    name = Name.get()
    symptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    
    if not name:
        messagebox.showerror("Error", "Please enter the patient's name")
        return
    if name.isdigit()==True:
        messagebox.showerror("Error","Please enter valid name of the patient")
        return
    
    special_char=re.compile("[@_!#$%^&*()<>?/|}{~:]")
    if special_char.search(name)!=None:
        messagebox.showerror("Error", "Please enter valid name of the patient")
        return
    
    if "Choose symptom" in symptoms[:2]:
        messagebox.showerror("Error", "Please select at least two symptoms")
        return
    
    symptom_vector = [1 if symptom in symptoms else 0 for symptom in symptoms_list]
    print("Symptoms:", symptoms)
    print("Symptom Vector:", symptom_vector)
    disease_index = model.predict(symptom_vector)
    print("Disease Index:", disease_index)
    
    disease = diseases[disease_index[0]]
    print("Predicted Disease:", disease)
    
    pred_var.set(disease)
    db.save_prediction(name, symptoms, disease)
#Method to reset all the inputs..
def reset():
    Name.set("")
    Symptom1.set("Choose symptom")
    Symptom2.set("Choose symptom")
    Symptom3.set("Choose symptom")
    Symptom4.set("Choose symptom")
    Symptom5.set("Choose symptom")
    pred_var.set("")
#Method to exit the system..
def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit?"):
        root.destroy()
# Layout
Label(root, text="Disease Predictor using Machine Learning", font=("Verdana", 30, "bold"), bg="#42f5f5").pack(pady=20)

frame = Frame(root, bg="#42f5f5")
frame.pack(pady=20)

Label(frame, text="Name of the Patient  ", font=("Verdana", 15,"bold"), bg="#42f5f5").grid(row=0, column=0, pady=10, sticky=W)
Entry(frame, textvariable=Name, width=50).grid(row=0, column=1, pady=20)

symptom_labels = ["Symptom 1", "Symptom 2", "Symptom 3", "Symptom 4", "Symptom 5"]
symptom_vars = [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5]

for i, (label, var) in enumerate(zip(symptom_labels, symptom_vars)):
    Label(frame, text=label, font=("Verdana", 15,"bold"), bg="#42f5f5").grid(row=i+1, column=0, pady=10, sticky=W)
    OptionMenu(frame, var, *symptoms_list).grid(row=i+1, column=1, pady=10)

# Prediction buttons
btn_frame = Frame(root, bg="#42f5f5")
btn_frame.pack(pady=20)

Button(btn_frame, text="Prediction 1", command=lambda: predict_disease(dt_model), bg="pink", font=("Verdana", 15,"bold")).grid(row=0, column=0, padx=10)
Button(btn_frame, text="Prediction 2", command=lambda: predict_disease(rf_model), bg="pink", font=("Verdana", 15,"bold")).grid(row=0, column=1, padx=10)
Button(btn_frame, text="Prediction 3", command=lambda: predict_disease(nb_model), bg="pink", font=("Verdana", 15,"bold")).grid(row=0, column=2, padx=10)
Button(btn_frame, text="Prediction 4", command=lambda: predict_disease(knn_model), bg="pink", font=("Verdana", 15,"bold")).grid(row=0, column=3, padx=10)

# Prediction result
Label(root, text="Predicted Disease:", font=("Verdana", 15,"bold"), bg="#42f5f5").pack(pady=10)
Label(root, textvariable=pred_var, font=("Verdana", 15,"bold"), bg="#42f5f5", relief=GROOVE, width=50).pack(pady=10)

# Control buttons
control_frame = Frame(root, bg="#42f5f5")
control_frame.pack(pady=20)

Button(control_frame, text="Reset Inputs", command=reset, bg="lightgreen", font=("Verdana", 15,"bold")).grid(row=0, column=0, padx=10)
Button(control_frame, text="Exit System", command=exit_app, bg="lightcoral", font=("Verdana", 15,"bold")).grid(row=0, column=1, padx=10)

root.mainloop()
