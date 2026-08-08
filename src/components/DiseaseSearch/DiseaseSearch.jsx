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

  // ====================================
  // Disease Prediction
  // ====================================

  const handleSearch = async () => {
    if (!symptoms.trim()) {
      alert("Please enter symptoms.");
      return;
    }

    try {
      setLoading(true);

      console.log("Sending Symptoms:", symptoms);

      const response = await API.post("/predict", {
        symptoms: symptoms,
      });

      console.log("Response:", response.data);

      if (response.data.success) {
        setResult(response.data.result);
      } else {
        alert(response.data.message);
      }
    } catch (err) {
      console.error(err);

      if (err.response) {
        alert(err.response.data.message);
      } else {
        alert("Unable to connect to backend.");
      }
    } finally {
      setLoading(false);
    }
  };

  // ====================================
  // Select Image
  // ====================================

  const handleImageChange = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  // ====================================
  // Image Prediction
  // ====================================

  const handleImageUpload = async () => {
    if (!image) {
      alert("Please select an image.");
      return;
    }

    const formData = new FormData();

    formData.append("image", image);

    try {
      setLoading(true);

      const response = await API.post(
        "/predict-image",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      if (response.data.success) {
        setResult(response.data.result);
      } else {
        setResult(response.data);
      }
    } catch (err) {
      console.error(err);
      alert("Image prediction failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="disease-search">

      <div className="search-container">

        <h2>AI Disease Prediction</h2>

        <p>
          Enter symptoms or upload a medical image.
        </p>

        <textarea
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          placeholder="Example: fever, cough, headache"
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

        <div className="divider">
          <span>OR</span>
        </div>

        <label className="upload-label">
          <FaUpload />
          Choose Medical Image

          <input
            type="file"
            hidden
            accept="image/*"
            onChange={handleImageChange}
          />
        </label>

        {preview && (
          <div className="image-preview">
            <img src={preview} alt="preview" />
          </div>
        )}

        {image && (
          <button
            className="upload-btn"
            onClick={handleImageUpload}
          >
            <FaImage />
            Predict From Image
          </button>
        )}

      </div>

    </section>
  );
};

export default DiseaseSearch;