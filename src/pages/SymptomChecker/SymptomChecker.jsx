import {useState} from "react";

import api from "../../services/api";

import SymptomForm from "../../components/SymptomForm";

import ResultCard from "../../components/ResultCard";

function SymptomChecker(){

const[result,setResult]=useState(null);

const predict=async(symptoms)=>{

const response=await api.post("/predict",{

symptoms

});

setResult(response.data);

}

return(

<div>

<h1>Symptom Checker</h1>

<SymptomForm

onSubmit={predict}

/>

<ResultCard

result={result}

/>

</div>

)

}

export default SymptomChecker;