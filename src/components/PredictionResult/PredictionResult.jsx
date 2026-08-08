import "./PredictionResult.css";

import {
  FaHeartbeat,
  FaPills,
  FaShieldVirus,
  FaAppleAlt,
  FaUserMd,
} from "react-icons/fa";

const PredictionResult = ({ result }) => {

  if (!result) return null;

  console.log(result);

  return (

    <section className="prediction-section">

      <div className="prediction-card">

        <div className="prediction-header">

          <h2>

            <FaHeartbeat />

            AI Diagnosis Report

          </h2>

        </div>

        <div className="disease-box">

          <h1>{result.disease}</h1>

          <p>{result.description}</p>

        </div>

        <div className="prediction-grid">

          <div className="info-card">

            <h3>

              <FaPills />

              Medicines

            </h3>

            <ul>

              {result.medicines?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}

            </ul>

          </div>

          <div className="info-card">

            <h3>

              <FaShieldVirus />

              Precautions

            </h3>

            <ul>

              {result.precautions?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}

            </ul>

          </div>

          <div className="info-card">

            <h3>

              <FaAppleAlt />

              Diet

            </h3>

            <ul>

              {result.diet?.map((item, index) => (
                <li key={index}>{item}</li>
              ))}

            </ul>

          </div>

          <div className="info-card">

            <h3>

              <FaUserMd />

              Specialist

            </h3>

            <p>{result.doctor}</p>

          </div>

        </div>

      </div>

    </section>

  );
};

export default PredictionResult;