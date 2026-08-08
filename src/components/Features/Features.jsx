import "./Features.css";
import {
  FaSearch,
  FaImage,
  FaRobot,
  FaPills,
  FaHeartbeat,
  FaAmbulance,
} from "react-icons/fa";

const features = [
  {
    icon: <FaSearch />,
    title: "Search Symptoms",
    description:
      "Describe your symptoms in natural language and receive AI-powered disease predictions instantly.",
  },
  {
    icon: <FaImage />,
    title: "Upload Medical Images",
    description:
      "Upload skin, eye or tongue images for AI-assisted disease detection and analysis.",
  },
  {
    icon: <FaRobot />,
    title: "AI Health Chatbot",
    description:
      "Chat with an intelligent healthcare assistant available 24×7 for medical guidance.",
  },
  {
    icon: <FaPills />,
    title: "Medicine Suggestions",
    description:
      "Receive commonly prescribed medicines and precautions based on predicted conditions.",
  },
  {
    icon: <FaHeartbeat />,
    title: "Health Dashboard",
    description:
      "Track previous disease reports, predictions and healthcare recommendations.",
  },
  {
    icon: <FaAmbulance />,
    title: "Emergency Assistance",
    description:
      "Quickly access emergency healthcare information and nearby hospitals.",
  },
];

const Features = () => {
  return (
    <section className="features" id="features">

      <div className="section-title">
        <h2>Our AI Healthcare Features</h2>
        <p>
          Powerful AI tools designed to provide quick, intelligent and reliable
          healthcare assistance.
        </p>
      </div>

      <div className="features-grid">
        {features.map((item, index) => (
          <div className="feature-card" key={index}>

            <div className="feature-icon">
              {item.icon}
            </div>

            <h3>{item.title}</h3>

            <p>{item.description}</p>

          </div>
        ))}
      </div>

    </section>
  );
};

export default Features;