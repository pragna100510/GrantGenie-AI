import { useState } from "react";

function StartupForm({ analyzeStartup }) {
  const [description, setDescription] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!description.trim()) {
      alert("Please enter your startup description.");
      return;
    }

    analyzeStartup(description);
  };

  return (
    <div className="card">

      <h2 style={{ marginBottom: "10px" }}>
        💡 Describe Your Startup
      </h2>

      <p
        style={{
          color: "#6b7280",
          marginBottom: "20px",
          lineHeight: "1.6",
        }}
      >
        Provide details such as your domain, country, startup stage,
        technologies used, and funding requirements.
      </p>

      <form onSubmit={handleSubmit}>

        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder={`Example:

We are an early-stage Indian startup developing AI-powered drones for crop disease detection using computer vision. We are seeking ₹5 lakh in funding to build our MVP and expand field testing.`}
        />

        <div
          style={{
            display: "flex",
            justifyContent: "flex-end",
            marginTop: "20px",
          }}
        >
          <button type="submit">
            🚀 Analyze Startup
          </button>
        </div>

      </form>

    </div>
  );
}

export default StartupForm;