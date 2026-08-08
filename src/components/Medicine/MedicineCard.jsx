function MedicineCard({ data }) {

    if (!data) return null;

    return (

        <div>

            <h2>Medicine Information</h2>

            <h3>Medicines</h3>

            <ul>

                {data.medicines.map((medicine, index) => (

                    <li key={index}>{medicine}</li>

                ))}

            </ul>

            <h3>Precautions</h3>

            <ul>

                {data.precautions.map((item, index) => (

                    <li key={index}>{item}</li>

                ))}

            </ul>

            <p style={{ color: "red" }}>

                Educational purposes only.
                Always consult a qualified doctor before taking medicines.

            </p>

        </div>

    )

}

export default MedicineCard;