function ResultCard({ result }) {

  if (!result) return null;

  return (
    <div>

      <h2>Disease: {result.disease}</h2>

      <h3>Confidence: {result.confidence}%</h3>

    </div>
  );
}

export default ResultCard;