
import "./Hero.css";
import heroImage from "../../assets/hero.jpeg";

function Hero() {

  const handleGetStarted = () => {
    const searchSection = document.getElementById("search");

    if (searchSection) {
      searchSection.scrollIntoView({
        behavior: "smooth",
        block: "start",
      });
    }
  };

  return (
    <section
      className="hero"
      style={{ backgroundImage: `url(${heroImage})` }}
    >

      <div className="overlay"></div>

      <div className="hero-content">

        <span className="hero-badge">
          AI-Powered Healthcare
        </span>

        <h1>
          AI Healthcare Assistant
        </h1>

        <p className="hero-quote">
          "Your health deserves intelligent care,
          trusted guidance, and better decisions."
        </p>

        <p className="hero-description">
          Predict diseases using AI, analyze symptoms,
          upload medical images, and receive personalized
          healthcare guidance instantly.
        </p>

        <button
          className="hero-btn"
          onClick={handleGetStarted}
        >
          Get Started
        </button>

      </div>

      <div className="scroll-indicator">
        <span>Explore</span>
        <div className="scroll-arrow">↓</div>
      </div>

    </section>
  );
}

export default Hero;

