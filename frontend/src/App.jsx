import { useState } from "react";
import api from "./api/api";

import StartupForm from "./components/StartupForm";
import StartupProfile from "./components/StartupProfile";
import GrantCard from "./components/GrantCard";

import "./App.css";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeStartup = async (description) => {
    setLoading(true);

    try {
      const response = await api.post("/workflow", {
        description,
      });

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Failed to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header className="hero">

        <h1>🚀 GrantGenie AI</h1>

        <p>
          Discover Grants • Check Eligibility • Generate Winning Proposals
        </p>

      </header>

      <StartupForm analyzeStartup={analyzeStartup} />

      {loading && (

        <div className="loading-card">

          <div className="spinner"></div>

          <h3>AI Agents Working...</h3>

          <p>Analyzing startup profile</p>

        </div>

      )}

      {result && (

        <>

          <div className="section-title">
            🌱 Startup Profile
          </div>

          <StartupProfile profile={result.startup_profile} />

          <div className="section-title">
            🏆 Recommended Grants
          </div>

          {result.grant_analysis.map((analysis, index) => (

            <GrantCard
              key={index}
              startupProfile={result.startup_profile}
              analysis={analysis}
            />

          ))}

        </>

      )}

      <footer>

        Built with ❤️ using FastAPI, React & IBM watsonx.ai

      </footer>

    </div>
  );
}

export default App;