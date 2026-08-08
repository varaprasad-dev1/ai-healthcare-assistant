import { useState } from "react";
import api from "../../services/api";

function Chatbot(){

const[input,setInput]=useState("");

const[reply,setReply]=useState("");

const ask=async()=>{

const res=await api.post("/chat",{

message:input

});

setReply(res.data.reply);

}

return(

<div>

<h1>AI Healthcare Chatbot</h1>

<textarea

rows={5}

value={input}

onChange={(e)=>setInput(e.target.value)}

/>

<br/>

<button onClick={ask}>

Ask AI

</button>

<p>{reply}</p>

</div>

)

}

export default Chatbot;