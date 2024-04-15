system_instruction = '''You are an helpful medical assistant tasked with information extraction from the provided clinical note: \n Note: There can multiple instance of symptoms, treatments. Extract all of them.
Return the extracted information in a JSON like this:\n '''

extra_instruction = '''
Instructions:
1. If something wasn't mentioned in the note, don't include it in the JSON. 
2. There can multiple instance of symptoms, treatments. Extract all of them.
'''

summary_raw_json_format = '''
visit motivation: "..." \n
admission: 'reason', 'date', 'care center details', 'duration' \n
patient information: 'socio economic context', 'recent travels', 'age', 'sex', 'weight', 'height', 'occupation', 'ethnicity', 'family medical history' \n
patient medical history: 'psychological context', 'drug usage', 'allergies', 'smoking status', 'nutrition', 'physiological context', 'sexual history', 'exercise frequency', 'alcohol consumption', 'vaccination history' \n
diagnosis tests: 'result', 'severity', 'condition', 'test', 'time', 'details' \n
discharge: 'follow up', 'referral', 'reason', 'discharge summary' \n
medical examinations: 'result', 'name', 'details' \n


surgeries: 'outcome', 'reason', 'Type', 'time', 'details' \n
symptoms: 'name of symptom', 'intensity of symptom', 'behaviours affecting the symptom', 'location', 'time', 'temporalisation', 'details' \n
treatments: 'reason for taking', 'reaction to treatment', 'name', 'related condition', 'duration', 'dosage', 'time', 'frequency', 'details' \n

'''

example_1 = '''
Here is an example:
[Full note:]
A 56-year-old male patient, whose plasmacytoma was enucleated 3 years ago from the medial side of the left mandible, was referred to our clinic due to his complaints of persistent orocutaneous fistula (Figures –). Past medical history revealed that the patient was operated three times to close the orocutaneous fistula by local flaps; however, none of these operations were successful. CT images of the patient demonstrated that the medial side of the left mandible was missing and there was a 3 × 2 cm diameter defect located between the left side of the mouth floor and the basis of the left mandible neighboring the left submandibular gland. The main reason of the failed attempts to close the fistula was considered to be the ineffective management of dead space surrounding the fistula. Consequently, it was decided to use the submandibular gland as a pedicled flap to fill the defect and support the oral and the cutaneous flaps.\n. Under general anesthesia, the fistula was excised initially and the oral and the cutaneous healthy soft tissues were prepared. At the extraoral site, the incision was extended to the posterior and anterior directions, following the previous incision lines. In the subplatysmal plane, the superficial layer of the neck fascia was dissected to reach the base of the mandible. After the dissection of the fascia, the submandibular gland and the base of the mandible were exposed, the soft tissues surrounding the submandibular gland were dissected, and the gland was mobilized by protecting the arteriovenous supply and the duct. At the oral site, the margins of the wound were released by blunt dissection and were closed by mattress sutures via 5/0 polypropylene. Following the mobilization of the gland, a soft tissue tunnel was prepared between the submandibular space and the defect area and the submandibular gland was rotated by passing the gland through the soft tissue tunnel by preserving the pedicle (). The rotated gland was sutured to the recipient site with 3/0 reabsorbable polyglaction sutures for the stabilization. At the cutaneous site, the flap was closed layer by layer by using 3/0 resorbable polyglaction for the facia and the subcutaneous layers and 3/0 polypropylene sutures for the skin. After the surgery, pressure bandage was applied for the edema control externally and the patient was ordered soft diet for a week. The postoperative healing was uneventful, and at the sixth month follow-up visit, ideal closure of the fistula was observed.


[Expected_JSON] Note the inforation required.
```json

{{[
    ('visit motivation': 'Complaints of persistent orocutaneous fistula'),
    ('admission': 
        [('reason': '...', 'date': '...', 'duration': '...', 'care center details': '...')] ),
    ( 'patient information': 
        ('age': '56', 'sex': 'male', 'ethnicity': '...', 'weight': '...', 'height': '...', 'family medical history': '...', 'recent travels': '...', 'socio economic context': '...',  'occupation': '...')),
    
    ('patient medical history': 
    ( 'physiological context': 'Plasmacytoma enucleated from the medial side of the left mandible 3 years ago', 'psychological context': '...', 'vaccination history': '...', 'allergies': '...', 'exercise frequency': '...', 'nutrition': '...', 'sexual history': '...', 'alcohol consumption': '...', 'drug usage': '...', 'smoking status': '...') ),
 
    ('surgeries': [('reason': 'To close the orocutaneous fistula', 'Type': 'Local flaps',  'time': '...', 'outcome': '...','details': '...')],)
    ( 'symptoms': [('name of symptom': 'Orocutaneous fistula', 'intensity of symptom': '...', 'location': 'Medial side of the left mandible', 'time': 'Persistent', 'temporalisation': '...', 'behaviours affecting the symptom': '...', 'details': 'A 3 × 2 cm diameter defect located between the left side of the mouth floor and the basis of the left mandible neighboring the left submandibular gland')],)
 
 
    ('medical examinations': [('name': 'CT images', 'result': 'Medial side of the left mandible was missing with a 3 × 2 cm diameter defect', 'details': 'Defect located between the left side of the mouth floor and the basis of the left mandible neighboring the left submandibular gland')], )
    
    ('diagnosis tests': [('test': 'None', 'severity': 'None',  'result': 'None', 'condition': 'Orocutaneous fistula', 'time': 'None', 'details': 'None')], )
    
    
    ( 'treatments': [('name': 'Surgical intervention using submandibular gland as a pedicled flap',
   'related condition': 'Orocutaneous fistula',
   'dosage': '...',
   'time': 'None',
   'frequency': '...',
   'duration': '...',
   'reason for taking': 'To fill the defect and support the oral and the cutaneous flaps',
   'reaction to treatment': '...',
   'details': 'Excision of fistula, preparation of oral and cutaneous soft tissues, mobilization of submandibular gland, suturing')],
   
   ('discharge': ('reason': '...',
  'referral': '...',
  'follow up': '...',
  'discharge summary': '...'))
  
]}}
```

'''


system_prompt = ''' 
```{system_instruction} \n```
```{summary_raw_json_format} \n ```
'''.format(system_instruction=system_instruction, summary_raw_json_format=summary_raw_json_format)

system_prompt_with_example = '''
```{system_instruction} \n```
```{summary_raw_json_format} \n ```
```{example_1} \n```
'''.format(system_instruction=system_instruction, summary_raw_json_format=summary_raw_json_format, example_1=example_1)



system_instruction_para = ''' You are an helpful medical assistant tasked with summarization from the provided clinical note: \n Note: There can multiple instance of symptoms, treatments. Summarize all of them.'''

summary_raw_output_format = ''' Return the detailed summary organized in the following headers: 
1. visit motivation:  \n
2. admission: Elaborate on: reason, date, care center details, duration \n
3. patient information: Elaborate on: 'socio economic context', 'recent travels', 'age', 'sex', 'weight', 'height', 'occupation', 'ethnicity', 'family medical history' \n
4. patient medical history: Elaborate on: 'psychological context', 'drug usage', 'allergies', 'smoking status', 'nutrition', 'physiological context', 'sexual history', 'exercise frequency', 'alcohol consumption', 'vaccination history' \n
5. diagnosis tests: Elaborate on: 'result', 'severity', 'condition', 'test', 'time', 'details' \n
6. medical examinations: Elaborate on: 'result', 'name', 'details' \n
7.surgeries: Elaborate on: 'outcome', 'reason', 'Type', 'time', 'details'}
8.symptoms: Elaborate on: 'name of symptom', 'intensity of symptom', 'behaviours affecting the symptom', 'location', 'time', 'temporalisation', 'details'
9. treatments Elaborate on: 'reason for taking', 'reaction to treatment', 'name', 'related condition', 'duration', 'dosage', 'time', 'frequency', 'details'
10. discharge: Elaborate on: 'follow up', 'referral', 'reason', 'discharge summary' \n
'''

example_1_para = ''' 

Here's an example:
[Note:]
A 49-year-old male presented with a complaint of pain in the left proximal forearm after a fall. The patient had a history of left elbow arthrodesis performed for posttraumatic arthritis at the age of 18. On physical examination he was tender at the proximal ulna. He had no active flexion or extension at his elbow, which was fused at 90 degrees but achieved 40 degrees of pronation and 60 degrees of supination. His motor and sensory exam was normal at the hand. Radiographs of the forearm and the elbow revealed an elbow arthrodesis at 90 degrees with retained hardware and a minimally displaced proximal ulnar shaft fracture (). A decision was made to treat his ulnar shaft fracture closed in a cast, and he subsequently developed a hypertrophic nonunion. At his clinic visit three months after the fall, surgical options for the ulna nonunion were discussed with the patient. We proceeded with conservative treatment for an additional three months, with worsening motion through the nonunion site. He revealed that he was unhappy with the functional limitations of his elbow arthrodesis and inquired about the possibility of converting it to an arthroplasty. The risks of elbow arthroplasty were discussed with the patient at length. Increasing the functional capacity of his arm was his ultimate goal, and understanding that he faced a likely operation for the ulna nonunion, the patient wished to proceed. Due to the patient's prior surgery and history of trauma, as well as risk of infection, we chose to avoid multiple surgeries and combine the repair of nonunion and the conversion of elbow arthrodesis to arthroplasty into one procedure. The stem of the ulnar component would thus act as an intramedullary device.\nIn the operating room the patient was placed in a supine position and a posterior incision centered over the elbow was performed. A prior muscle flap that was used for soft tissue coverage at his index procedure had to be elevated. The ulnar nerve was encased in scar tissue and required a meticulous neuroplasty. A triceps splitting approach to the elbow joint was then performed and multiple buried pins were removed from the humerus []. A wedge osteotomy of the arthrodesis site was then performed and the fusion taken down (). This was performed at the apex of the arthrodesis site with the humeral cut at 90 degrees to the long axis of the humerus and the ulnar cut at 45 degrees to the long axis of the ulna. The cuts were done in this manner to better accommodate the stems of the prosthesis. Resection of the humerus was greater than normal to allow for appropriate range of motion (ROM) of the elbow without undue tension on the neurovascular structures, which had been in this position for over 30 years. Resection of the radial head was performed as it was markedly arthritic. After preparation of the canals, a Stryker distal humeral replacement system was used to perform the total elbow arthroplasty (MRS (Stryker, Kalamazoo, MI)). Intraoperatively, the patient had full flexion and extension of the elbow and full pronation and supination. His muscles were properly tensioned without undue strain on the neurovascular structures. The patient's ulnar nonunion was also addressed with bone graft taken from the resected radial head. He had an uncomplicated hospital course and was allowed full ROM on postoperative day #2. At his 4.5-month appointment, the patient was achieving 0–110° elbow active elbow flexion/extension, as well as nearly full forearm rotation. He was experiencing minimal pain and was happy with the function of his prosthesis. The patient was able to return to work with an elbow brace that he locked at work. Radiographs showed a healed ulna nonunion and a stable total elbow prosthesis without signs of loosening (). Multiple attempts to contact the patient for further follow-up have been unsuccessful.
[End Note]

[Expected organized summary:]
A 49-year-old male patient with a history of left elbow arthrodesis at age 18 for posttraumatic arthritis presented with pain in the left proximal forearm after a fall.

Medical History: No significant past medical history or allergies documented.

Surgical History:

    Left elbow arthrodesis at age 18 for posttraumatic arthritis (details: elbow fused at 90 degrees).
    Repair of nonunion and conversion of elbow arthrodesis to arthroplasty three months after a prior fall and conservative treatment (details: the stem of the ulnar component would act as an intramedullary device).

Current Presentation:

    Pain in the left proximal forearm after a fall.
    Physical exam revealed no active flexion or extension at the elbow, 40 degrees of pronation, 60 degrees of supination, and normal motor and sensory exam at the hand. Elbow was fused at 90 degrees. Patient was tender at the proximal ulna.
    X-rays showed a minimally displaced proximal ulnar shaft fracture with hypertrophic nonunion and confirmed the prior elbow arthrodesis with retained hardware.

Treatment:

    Initially treated with a closed cast for the ulnar shaft fracture after the fall. This treatment developed into a hypertrophic nonunion.
    Conservative treatment for the ulnar nonunion was attempted three months after the fall for an additional three months. This resulted in worsening motion through the nonunion site.

Discharge: No discharge details documented.
'''




system_prompt_para_with_example = ''' '''






if __name__ == "__main__":
    print(system_prompt)

    print("\n", system_prompt_with_example)
