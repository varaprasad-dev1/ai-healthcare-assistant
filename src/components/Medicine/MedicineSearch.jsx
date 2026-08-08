import { useState } from "react";

function MedicineSearch({ onSearch }) {

  const [disease, setDisease] = useState("");

  const handleSearch = () => {
    if (disease.trim() === "") {
      alert("Please enter a disease name");
      return;
    }

    onSearch(disease);
  };

  return (
    <div>

      <input
        type="text"
        placeholder="Enter disease name"
        value={disease}
        onChange={(e) => setDisease(e.target.value)}
      />

      <button onClick={handleSearch}>
        Search
      </button>

    </div>
  );
}

export default MedicineSearch;