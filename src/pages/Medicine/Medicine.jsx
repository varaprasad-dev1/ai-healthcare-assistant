import { useState } from "react";

import api from "../../services/api";

import MedicineSearch from "../../components/Medicine/MedicineSearch";

import MedicineCard from "../../components/Medicine/MedicineCard";

function Medicine() {

    const [result, setResult] = useState(null);

    const searchMedicine = async (disease) => {

        try {

            const response = await api.post("/medicine", {

                disease

            });

            setResult(response.data);

        }

        catch (error) {

            console.log(error);

        }

    };

    return (

        <div>

            <h1>Medicine Recommendation</h1>

            <MedicineSearch

                onSearch={searchMedicine}

            />

            <MedicineCard

                data={result}

            />

        </div>

    );

}

export default Medicine;