import { useState } from "react";
import "./DiseaseSearch.css";
import API from "../../services/api";

import {
  FaSearch,
  FaSpinner,
  FaUpload,
  FaImage,
} from "react-icons/fa";

const DiseaseSearch = ({ setResult }) => {
  const [symptoms, setSymptoms] = useState("");
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ====================================
  // Disease Prediction from Symptoms
  // ====================================

  const handleSearch = async () => {
    if (!symptoms.trim()) {
      alert("Please enter symptoms.");
      return;
    }

    try {
      setLoading(true);
      setError("");

      const response = await API.post("/predict", {
        symptoms: symptoms,
      });

      console.log("Disease prediction:", response.data);

      if (response.data.success) {
        setResult(response.data.result);
      } else {
        setError(response.data.message || "Prediction failed.");
      }
    } catch (err) {
      console.error("Disease prediction error:", err);

      if (err.response?.data?.message) {
        setError(err.response.data.message);
      } else {
        setError("Unable to connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  };

  // ====================================
  // Select Medical Image
  // ====================================

  const handleImageChange = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    // Check image type
    if (!file.type.startsWith("image/")) {
      alert("Please select a valid image.");
      return;
    }

    // Optional size limit: 10 MB
    if (file.size > 10 * 1024 * 1024) {
      alert("Please select an image smaller than 10 MB.");
      return;
    }

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setError("");
  };

  // ====================================
  // AI Image Prediction
  // ====================================

  const handleImageUpload = async () => {
    if (!image) {
      alert("Please select an image first.");
      return;
    }

    const formData = new FormData();

    formData.append("image", image);

    try {
      setLoading(true);
      setError("");

      console.log("Sending image to Gemini AI...");

      const response = await API.post(
        "/predict-image",
        formData
      );

      console.log("Gemini image response:", response.data);

      if (response.data.success) {
        setResult(response.data.result);
      } else {
        setError(
          response.data.message || "Image analysis failed."
        );
      }
    } catch (err) {
      console.error("Image prediction error:", err);

      if (err.response?.data?.message) {
        setError(err.response.data.message);
      } else {
        setError(
          "Unable to connect to the AI image analysis service."
        );
      }
    } finally {
      setLoading(false);
    }
  };

  // ====================================
  // Remove Selected Image
  // ====================================

  const handleRemoveImage = () => {
    setImage(null);
    setPreview(null);
    setError("");
  };

  // ====================================
  // UI
  // ====================================

  return (
    <section className="disease-search">
      <div className="search-container">

        <h2>AI Disease Prediction</h2>

        <p>
          Enter your symptoms or upload a medical image
          for AI-assisted analysis.
        </p>

        {/* ====================================
            SYMPTOM SEARCH
        ==================================== */}

        <textarea
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          placeholder="Example: fever, cough, headache"
          disabled={loading}
        />

        <button
          onClick={handleSearch}
          disabled={loading}
          className="search-btn"
        >
          {loading ? (
            <>
              <FaSpinner className="spin" />
              Predicting...
            </>
          ) : (
            <>
              <FaSearch />
              Predict Disease
            </>
          )}
        </button>

        {/* ====================================
            DIVIDER
        ==================================== */}

        <div className="divider">
          <span>OR</span>
        </div>

        {/* ====================================
            IMAGE UPLOAD
        ==================================== */}

        <label className="upload-label">
          <FaUpload />
          {image ? "Change Medical Image" : "Choose Medical Image"}

          <input
            type="file"
            hidden
            accept="image/png,image/jpeg,image/webp"
            onChange={handleImageChange}
            disabled={loading}
          />
        </label>

        {/* ====================================
            IMAGE PREVIEW
        ==================================== */}

        {preview && (
          <div className="image-preview">

            <img
              src={preview}
              alt="Selected medical image"
            />

            <button
              type="button"
              onClick={handleRemoveImage}
              disabled={loading}
            >
              Remove Image
            </button>

          </div>
        )}

        {/* ====================================
            AI IMAGE ANALYSIS BUTTON
        ==================================== */}

        {image && (
          <button
            className="upload-btn"
            onClick={handleImageUpload}
            disabled={loading}
          >
            {loading ? (
              <>
                <FaSpinner className="spin" />
                Analyzing Image...
              </>
            ) : (
              <>
                <FaImage />
                Analyze Image with AI
              </>
            )}
          </button>
        )}

        {/* ====================================
            ERROR
        ==================================== */}

        {error && (
          <div className="prediction-error">
            {error}
          </div>
        )}

      </div>
    </section>
  );
};

export default DiseaseSearch;