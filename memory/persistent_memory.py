patient_store = {}

def save_patient(patient_id, data):
    patient_store[patient_id] = data

def get_patient(patient_id):
    return patient_store.get(patient_id, {})
