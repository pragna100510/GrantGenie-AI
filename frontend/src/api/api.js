import axios from "axios";

const api = axios.create({
    baseURL: "https://grantgenie-ai-backend.onrender.com",
});

export default api;