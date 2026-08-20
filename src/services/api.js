import axios from "axios";

const API = axios.create({
    baseURL: "https://ai-healthcare-assistant-backend-k2xv.onrender.com",
});

export default API;