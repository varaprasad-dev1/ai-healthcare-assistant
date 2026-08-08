import { Routes, Route, Navigate } from "react-router-dom";

// Authentication
import Register from "./pages/Register/Register";
import Login from "./pages/Login/Login";

// Main Pages
import Home from "./pages/Home/Home";

// Future Pages
// import Dashboard from "./pages/Dashboard/Dashboard";
// import SymptomChecker from "./pages/SymptomChecker/SymptomChecker";
// import Chatbot from "./pages/Chatbot/Chatbot";
// import Medicine from "./pages/Medicine/Medicine";
// import Profile from "./pages/Profile/Profile";

function App() {
  return (
    <Routes>

      {/* Default Route */}
      <Route path="/" element={<Navigate to="/register" replace />} />

      {/* Authentication */}
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<Login />} />

      {/* Home */}
      <Route path="/home" element={<Home />} />

      {/* Future Routes */}
      {/* <Route path="/dashboard" element={<Dashboard />} /> */}
      {/* <Route path="/symptoms" element={<SymptomChecker />} /> */}
      {/* <Route path="/chatbot" element={<Chatbot />} /> */}
      {/* <Route path="/medicine" element={<Medicine />} /> */}
      {/* <Route path="/profile" element={<Profile />} /> */}

      {/* Invalid URL */}
      <Route path="*" element={<Navigate to="/register" replace />} />

    </Routes>
  );
}

export default App;