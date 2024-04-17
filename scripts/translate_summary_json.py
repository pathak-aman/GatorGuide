def preprocess_none(summary):
    if isinstance(summary, dict):
        return {key: preprocess_none(value) for key, value in summary.items()}
    elif isinstance(summary, list):
        return [preprocess_none(item) for item in summary]
    elif summary == 'None':
        return None
    else:
        return summary

def translate_visit_motivation(summary):
    sentences = []
    try:
        visit_motivation = summary.get('visit motivation')
        if visit_motivation:
            sentences.append(f"\nVisit Motivation:")
            sentences.append(f"The patient reported {visit_motivation}")
    except Exception as e:
        return f"Error in visit motivation: {e}"
    return sentences


def translate_admission(summary):
    sentences = []
    try:
        admission = summary.get('admission', [{}])[0]  # Get first element from list
        if admission.get('reason') != None:
            sentences.append("\nAdmission:")
            reason = admission.get('reason')
            date = admission.get('date')
            duration = admission.get('duration')
            care_center = admission.get('care center details')

            sentence = f"The patient was admitted"
            if reason:
                sentence += f" for {reason}"
            if (date):
                sentence += f" on {date}"
            if duration:
                sentence += f" and stayed for {duration}"
            if care_center:
                sentence += f" at {care_center}"
            sentence += "."
            sentences.append(sentence)
        else:
            sentences.append("\nAdmission: No information")
    except Exception as e:
        return f"Error in admission information: {e}"
    return sentences


def translate_patient_info(summary):
    sentences = []
    try:
        patient_info = summary.get('patient information', {})
        if patient_info:
            sentences.append("\nPatient Information:")
            age = patient_info.get('age')
            sex = patient_info.get('sex')
            ethnicity = patient_info.get('ethnicity')
            weight = patient_info.get('weight')
            height = patient_info.get('height')
            family_history = patient_info.get('family medical history')
            recent_travels = patient_info.get('recent travels')
            socio_economic = patient_info.get('socio economic context')
            occupation = patient_info.get('occupation')

            # Construct sentences based on available data
            info = []
            if age:
                info.append(age)
            if sex:
                info.append(sex)
            if ethnicity:
                info.append(ethnicity)
            if weight:
                info.append(weight)
            if height:
                info.append(height)
            if family_history:
                info.append(family_history)
            if recent_travels:
                info.append(recent_travels)
            if socio_economic:
                info.append(socio_economic)
            if occupation:
                info.append(occupation)

            if info:
                sentence = "The patient is " + " and ".join(info) + "."
                sentences.append(sentence)
        else:
            sentences.append("\natient Information:: No information")
    except Exception as e:
        return f"Error in patient information: {e}"
    return sentences


def translate_patient_medical_info(summary):

    sentences = []
    try:
        medical_history = summary.get('patient medical history', {})
        if medical_history:
            psychological_context = medical_history.get('psychological context')
            vaccination_history = medical_history.get('vaccination history')
            allergies = medical_history.get('allergies')
            exercise_frequency = medical_history.get('exercise frequency')
            nutrition = medical_history.get('nutrition')
            sexual_history = medical_history.get('sexual history')
            alcohol_consumption = medical_history.get('alcohol consumption')
            drug_usage = medical_history.get('drug usage')
            smoking_status = medical_history.get('smoking status')
            physiological_context = medical_history.get('physiological context')

            # Construct sentences based on available data
            info = []
            if psychological_context:
                info.append(f"psychological context is {psychological_context}")
            if vaccination_history:
                info.append(f"Vaccination history is {vaccination_history}")
            if allergies:
                info.append(f"allergies is {allergies}")
            if exercise_frequency:
                info.append(f"exercise frequency is {exercise_frequency}")
            if nutrition:
                info.append(f"nutrition is {nutrition}")
            if sexual_history:
                info.append(f"sexual history is {sexual_history}")
            if alcohol_consumption:
                info.append(f"alcohol consumption is {alcohol_consumption}")
            if drug_usage:
                info.append(f"drug usage is {drug_usage}")
            if smoking_status:
                info.append(f"smoking status is {smoking_status}")
            if physiological_context:
                info.append(f"physiological context is {physiological_context}")

            if info:
                sentences.append("\nMedical History:")
                info_text = ", ".join(info)  # Join info items with commas
                sentences.append(f"The patient's {info_text}, have been reported.")
            else:
                sentences.append("\nMedical History: No information")

        else:
            sentences.append("\nMedical History: No information")
    except Exception as e:
        return f"Error in patient medical history: {e}"
    return sentences



def translate_diagnosis_tests(summary):
    sentences = []
    try:
        diagnosis_tests = summary.get('diagnosis tests', [])
        if diagnosis_tests[0].get("test"):
            sentences.append("\nDiagnosis Tests:")
            for test in diagnosis_tests:
                result = test.get('result')
                severity = test.get('severity')
                condition = test.get('condition')
                test_name = test.get('test')
                time = test.get('time')
                details = test.get('details')

                # Construct sentence based on available data
                if result:
                    sentence = f"The {test_name} test"
                    if time:
                        sentence += f" performed on {time}"
                    sentence += f" revealed {result}"
                    if severity:
                        sentence += f" ({severity} severity)."
                    if condition:
                        sentence += f" consistent with {condition}."
                    if details:
                        sentence += f" additional details include {details}."
                    sentences.append(sentence)
        else:
            sentences.append("Diagnosis Tests: No information")
    except Exception as e:
        return f"Error in diagnosis tests information: {e}"
    return sentences



def translate_surgeries(summary):
    sentences = []
    try:
        surgeries = summary.get('surgeries', [])
        if surgeries[0].get('reason'):
            sentences.append("\nSurgeries:")
            for surgery in surgeries:
                surgery_type = surgery.get('Type')
                reason = surgery.get('reason')
                time = surgery.get('time')
                outcome = surgery.get('outcome')
                details = surgery.get('details')

                # Construct sentence based on available data
                if surgery_type:
                    sentence = f"A {surgery_type} surgery"
                    if reason and reason != 'None':
                        sentence += f" was performed to {reason}"
                    if time:
                        sentence += f" on {time}"
                    if outcome:
                        sentence += f" with an outcome of {outcome}."
                    if details:
                        sentence += f" additional details include {details}."
                    sentences.append(sentence)
        else:
            sentences.append("\nSurgeries: No information")
    except Exception as e:
        return f"Error in surgeries information: {e}"
    return sentences



def translate_symptoms(summary):
    sentences = []
    try:
        symptoms = summary.get('symptoms', [])
        if symptoms[0].get('name of symptom'):
            sentences.append("\nSymptoms:")
            for symptom in symptoms:
                symptom_name = symptom.get('name of symptom')
                intensity = symptom.get('intensity of symptom')
                location = symptom.get('location')
                time = symptom.get('time')
                temporalization = symptom.get('temporalisation')
                behaviors = symptom.get('behaviours affecting the symptom')
                details = symptom.get('details')

                # Construct sentence based on available data
                if symptom_name:
                    sentence = f"The patient reports {symptom_name}"
                    if location:
                        sentence += f" in the {location}"
                    if intensity:
                        sentence += f" with an intensity of {intensity}"
                    if time:
                        sentence += f" for the past {time}"
                    if temporalization:
                        sentence += f". {temporalization}"
                    if behaviors:
                        sentence += f". This symptom is worsened by {behaviors}"
                    if details:
                        sentence += f". {details}."
                    sentences.append(sentence)
        else:
            sentences.append("\nSymptoms: No information")
    except Exception as e:
        return f"Error in symptoms information: {e}"
    return sentences



def translate_medical_examinations(summary):
    sentences = []
    try:
        examinations = summary.get('medical examinations', [])
        if examinations[0].get('name'):
            sentences.append("\nMedical Examinations:")
            for examination in examinations:
                name = examination.get('name')
                result = examination.get('result')
                details = examination.get('details')

                # Construct sentence based on available data
                if name:
                    sentence = f"{name.title()} examination"
                    if result:
                        sentence += f" revealed {result}"
                    if details:
                        sentence += f". {details}"
                    sentences.append(sentence)
        else:
            sentences.append("\nMedical Examinations: No information")
    except Exception as e:
        return f"Error in medical examinations information: {e}"
    return sentences



def translate_treatments(summary):
    sentences = []
    try:
        treatments = summary.get('treatments', [])
        if treatments[0].get("name"):
            sentences.append("\nTreatments:")
            for treatment in treatments:
                name = treatment.get('name')
                related_condition = treatment.get('related condition')
                reason = treatment.get('reason for taking')
                reaction = treatment.get('reaction to treatment')
                details = treatment.get('details')
                duration = treatment.get('duration')
                dosage = treatment.get('dosage')
                time = treatment.get('time')
                frequency = treatment.get('frequency')

                # Construct sentence based on available data
                if name:
                    sentence = f"The patient received {name} treatment"
                    if related_condition:
                        sentence += f" for {related_condition}"
                    if reason:
                        sentence += f" to {reason}"
                    if duration:
                        sentence += f" on {duration}"
                    if dosage:
                        sentence += f". dosage {dosage}"
                    if time:
                        sentence += f" on {time}"
                    if frequency:
                        sentence += f". {frequency} times."
                    if details:
                        sentence += f". {details}"
                    if reaction:
                        sentence += f". which had {reaction}."
                    sentences.append(sentence)
        else:
            sentences.append("\nTreatments: No information")
    except Exception as e:
        return f"Error in treatments information: {e}"
    return sentences



def translate_discharge(summary):
    sentences = []
    try:
        discharge_info = summary.get('discharge', {})
        if discharge_info.get("reason"):
            sentences.append("\nDischarge:")
            reason = discharge_info.get('reason')
            referral = discharge_info.get('referral')
            follow_up = discharge_info.get('follow up')
            summary_text = discharge_info.get('discharge summary')

            # Construct sentences based on available data
            if reason and reason != 'None':
                sentences.append(f"The patient was discharged for {reason}.")
            if referral and referral != 'None':
                sentences.append(f"A referral was made to {referral}.")
            if follow_up and follow_up != 'None':
                sentences.append(f"Follow-up is scheduled {follow_up}.")
            if summary_text:
                sentences.append(summary_text)
        else:
            sentences.append("\nDischarge: No information")
    except Exception as e:
        return f"Error in discharge information: {e}"
    return sentences





def translate_summary(summary):

    sentences = {}
    summary = eval(summary)
    summary = preprocess_none(summary)

    visit_motivation = translate_visit_motivation(summary)
    admission = translate_admission(summary)
    patient_info = translate_patient_info(summary)
    medical_info = translate_patient_medical_info(summary)
    surgeries = translate_surgeries(summary)
    symptoms = translate_symptoms(summary)
    medical_examinations = translate_medical_examinations(summary)
    diagnosis_tests = translate_diagnosis_tests(summary)
    treatments = translate_treatments(summary)
    discharge = translate_discharge(summary)

    if visit_motivation:
        sentences["Visit Motivation"] = visit_motivation
    if admission:
        sentences["Admission"] = admission
    if patient_info:
        sentences["Patient Information"] = patient_info
    if medical_info:
        sentences["Patient Medical History"] = medical_info
    if surgeries:
        sentences["Surgeries"] = surgeries
    if symptoms:
        sentences["Symptoms"] = symptoms
    if medical_examinations:
        sentences["Medical Examinations"] = medical_examinations
    if diagnosis_tests:
        sentences["Diagnosis Tests"] = diagnosis_tests
    if treatments:
        sentences["Treatments"] = treatments
    if discharge:
        sentences["Discharge"] = discharge

    # print(sentences)

    # Combine sentences into a paragraph
    if sentences:
        paragraph = "".join([" ".join(info) for info in sentences.values()])
        return paragraph.strip(), sentences  # Remove leading/trailing whitespace
    else:
        return "No information found in the summary."


    # print(translations)
    # print(translate_admission(summary))
    # print(translate_patient_info(summary))
    # print(translate_patient_medical_info(summary))
    # print(translate_diagnosis_tests(summary))
    # print(translate_surgeries(summary))
    # print(translate_symptoms(summary))
    # print(translate_medical_examinations(summary))
    # print(translate_treatments(summary))
    # print(translate_discharge(summary))

if __name__ == '__main__':
    summary = '''{'visit motivation': 'Discomfort in the neck and lower back, restriction of body movements, inability to maintain an erect posture, and requiring assistance in standing and walking.', 'admission': [{'reason': 'None', 'date': 'None', 'duration': 'None', 'care center details': 'None'}], 'patient information': {'age': 'Sixteen years old', 'sex': 'Female', 'ethnicity': 'None', 'weight': 'None', 'height': 'None', 'family medical history': 'None', 'recent travels': 'None', 'socio economic context': 'None', 'occupation': 'None'}, 'patient medical history': {'physiological context': 'None', 'psychological context': 'Diagnosed with bipolar affective disorder at the age of eleven, first episode was that of mania.', 'vaccination history': 'None', 'allergies': 'None', 'exercise frequency': 'None', 'nutrition': 'None', 'sexual history': 'None', 'alcohol consumption': 'None', 'drug usage': 'None', 'smoking status': 'None'}, 'surgeries': [{'reason': 'None', 'Type': 'None', 'time': 'None', 'outcome': 'None', 'details': 'None'}], 'symptoms': [{'name of symptom': 'Discomfort in the neck and lower back, restriction of body movements, inability to maintain an erect posture', 'intensity of symptom': 'None', 'location': 'Neck and lower back', 'time': 'Past four months', 'temporalisation': 'None', 'behaviours affecting the symptom': 'Standing up from a sitting position', 'details': 'Head turned to the right and upwards due to sustained contraction of neck muscles, sideways bending of the back in the lumbar region, limbs positioned to support body weight.'}], 'medical examinations': [{'name': 'None', 'result': 'None', 'details': 'None'}], 'diagnosis tests': [{'test': 'None', 'severity': 'None', 'result': 'None', 'condition': 'None', 'time': 'None', 'details': 'None'}], 'treatments': [{'name': 'Olanzapine tablets', 'related condition': 'Bipolar affective disorder', 'dosage': '5 mg per day', 'time': 'Past four months', 'frequency': 'Daily', 'duration': 'None', 'reason for taking': 'Control of exacerbated mental illness', 'reaction to treatment': 'Pain and discomfort in neck, sustained and abnormal contraction of neck muscles, requiring assistance in daily chores', 'details': 'Previously managed with olanzapine tablets in 2.5–10 mg doses per day at different times over the past seven years.'}, {'name': 'Trihexyphenidyl', 'related condition': 'Rigidity in upper limbs', 'dosage': '4 mg per day', 'time': 'Brief period of around three weeks', 'frequency': 'Daily', 'duration': 'None', 'reason for taking': 'Rigidity in upper limbs', 'reaction to treatment': 'Good response', 'details': 'None'}], 'discharge': {'reason': 'None', 'referral': 'None', 'follow up': 'None', 'discharge summary': 'None'}}'''

    # summary = '''{'visit motivation': 'Inability to walk on both lower limbs', 'admission': [{'reason': 'Sudden onset pain in right groin region while walking, inability to bear weight on right lower limb, and later similar pain in left groin with inability to bear weight on either lower limb', 'date': 'None', 'duration': '3 months', 'care center details': 'None'}], 'patient information': {'age': '16 years old', 'sex': 'Female', 'ethnicity': 'None', 'weight': 'None', 'height': 'None', 'family medical history': 'None', 'recent travels': 'None', 'socio economic context': 'None', 'occupation': 'None'}, 'patient medical history': {'physiological context': 'Coxa vara deformity of bilateral hips, bilateral non-union of pathological fracture of femur neck', 'psychological context': 'None', 'vaccination history': 'None', 'allergies': 'None', 'exercise frequency': 'None', 'nutrition': 'None', 'sexual history': 'None', 'alcohol consumption': 'None', 'drug usage': 'None', 'smoking status': 'None'}, 'surgeries': [{'reason': 'Correction of deformity to realign the head, neck, and shaft of the femur; to achieve valgus at the neck-shaft region and a horizontal configuration neck fracture to increase the chances of union of pathological fracture of neck femur', 'Type': 'Oblique osteotomy', 'time': 'None', 'outcome': 'None', 'details': 'Performed on the right side, first oblique osteotomy was done from just distal to the greater trochanter'}], 'symptoms': [{'name of symptom': 'Inability to walk', 'intensity of symptom': 'None', 'location': 'Both lower limbs', 'time': 'Last 3 months', 'temporalisation': 'Initially able to walk with a limp, then sudden onset of pain leading to inability to bear weight', 'behaviours affecting the symptom': 'Walking', 'details': 'Patient experienced sudden onset pain in right groin region while walking, leading to inability to bear weight on right lower limb, followed by similar pain in left groin'}], 'medical examinations': [{'name': 'Clinical findings', 'result': 'Coxa vara deformity of bilateral hips, possibility of bilateral non-union of pathological fracture of femur neck', 'details': 'No evidence of endocrine disturbance, altered pigmentation, or precocious puberty'}], 'diagnosis tests': [{'test': 'Imaging', 'severity': 'None', 'result': "Polyostotic fibrous dysplasia with bilateral Shepherd's crook deformity of the proximal femur, bilateral non-union of pathological fracture of neck femur", 'condition': 'Polyostotic fibrous dysplasia', 'time': 'None', 'details': 'Imaging of other bones showed fibrous dysplastic lesions in the shaft of left tibia'}, {'test': 'Magnetic resonance scanning', 'severity': 'None', 'result': 'Features consistent with fibrous dysplasia of the proximal femur shaft along with sub-capital fracture of femur neck without evidence of avascular necrosis of the femur head', 'condition': 'Fibrous dysplasia of the proximal femur shaft, sub-capital fracture of femur neck', 'time': 'None', 'details': 'None'}, {'test': 'Blood and serum biochemical investigations', 'severity': 'None', 'result': 'Normal', 'condition': 'None', 'time': 'None', 'details': 'Hemoglobin, total and differential white cell counts, erythrocyte sedimentation rate, C-reactive protein, calcium, phosphorus, alkaline phosphatase levels and all hormonal studies were within normal limits'}], 'treatments': [{'name': 'Surgical correction of deformity', 'related condition': 'Coxa vara deformity, non-union of pathological fracture of neck femur', 'dosage': 'None', 'time': 'None', 'frequency': 'None', 'duration': 'None', 'reason for taking': 'To realign the head, neck, and shaft of the femur; to achieve valgus at the neck-shaft region and a horizontal configuration neck fracture to increase the chances of union', 'reaction to treatment': 'None', 'details': 'One stage, each side at a time'}], 'discharge': {'reason': 'Successful postoperative recovery', 'referral': 'None', 'follow up': 'None', 'discharge summary': 'Patient underwent surgical removal of a calcified mass and lower right third molar with curettage of infected soft tissues, with uneventful healing and no neural defects postoperatively.'}}'''

    translated_summary, summary_dict = translate_summary(summary)
    print(translated_summary)
    print(summary_dict)

