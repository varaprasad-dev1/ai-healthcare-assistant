import { useState } from "react";

import Hero from "../../components/Hero/Hero";
import Features from "../../components/Features/Features";
import DiseaseSearch from "../../components/DiseaseSearch/DiseaseSearch";
import PredictionResult from "../../components/PredictionResult/PredictionResult";

// Future Components
// import ChatBot from "../../components/ChatBot/ChatBot";
// import MedicineSearch from "../../components/MedicineSearch/MedicineSearch";
// import Footer from "../../components/Footer/Footer";

const Home = () => {
  const [result, setResult] = useState(null);

  return (
    <main>

      {/* ================= HERO ================= */}
      <Hero />

      {/* ================= FEATURES ================= */}
      <Features />

      {/* ================= DISEASE PREDICTION ================= */}
      <DiseaseSearch
        setResult={setResult}
      />

      {/* ================= RESULT ================= */}
      {result !== null && (
        <PredictionResult
          result={result}
        />
      )}

      {/* ================= FUTURE MODULES ================= */}

      {/*
      <MedicineSearch
        disease={result?.disease}
      />
      */}

      {/*
      <ChatBot />
      */}

      {/*
      <Footer />
      */}

    </main>
  );
};

export default Home;