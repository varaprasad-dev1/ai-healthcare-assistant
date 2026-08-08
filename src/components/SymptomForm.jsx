import { useState } from "react";

function SymptomForm({onSubmit}){

const[input,setInput]=useState("");

const submit=()=>{

const symptoms=input.split(",");

onSubmit(symptoms);

}

return(

<div>

<input

placeholder="fever,cough"

value={input}

onChange={(e)=>setInput(e.target.value)}

/>

<button onClick={submit}>

Predict

</button>

</div>

)

}

export default SymptomForm;