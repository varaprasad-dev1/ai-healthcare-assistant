from .medicine_data import MEDICINES

def get_medicine(disease):

    if disease in MEDICINES:

        return MEDICINES[disease]

    return{

        "medicines":[],

        "precautions":[

            "Consult a doctor."

        ]

    }