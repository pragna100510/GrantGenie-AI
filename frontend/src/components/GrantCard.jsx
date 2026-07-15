import { useState } from "react";
import api from "../api/api";
import EligibilityCard from "./EligibilityCard";
import ProposalModal from "./ProposalModal";

function GrantCard({ startupProfile, analysis }) {
  const [proposal, setProposal] = useState(null);
  const [loading, setLoading] = useState(false);

  const grant = analysis.grant;
  const recommendation = analysis.recommendation;
  const eligibility = analysis.eligibility;

  const generateProposal = async () => {
    setLoading(true);

    try {
      const response = await api.post("/proposal", {
        profile: startupProfile,
        grant: grant,
      });

      setProposal(response.data);
    } catch (err) {
      console.error(err);
      alert("Failed to generate proposal.");
    }

    setLoading(false);
  };

  return (
    <>
      <div className="card grant-card">

        <div className="grant-header">

          <div>
            <h2>{grant.name}</h2>

            <span
              className={
                recommendation.match_score.toLowerCase() === "high"
                  ? "badge success"
                  : recommendation.match_score.toLowerCase() === "medium"
                  ? "badge warning"
                  : "badge danger"
              }
            >
              ⭐ {recommendation.match_score} Match
            </span>
          </div>

          <button onClick={generateProposal} disabled={loading}>
            {loading ? "Generating..." : "📝 Generate Proposal"}
          </button>

        </div>

        <div className="grant-grid">

          <div className="grant-item">
            <h4>🌍 Country</h4>
            <p>{grant.country}</p>
          </div>

          <div className="grant-item">
            <h4>🏭 Sector</h4>
            <p>{grant.sector}</p>
          </div>

          <div className="grant-item">
            <h4>🚀 Stage</h4>
            <p>{grant.stage}</p>
          </div>

          <div className="grant-item">
            <h4>💰 Funding</h4>
            <p>{grant.funding}</p>
          </div>

          <div className="grant-item">
            <h4>📅 Deadline</h4>
            <p>{grant.deadline}</p>
          </div>

          <div className="grant-item">
            <h4>🌐 Website</h4>

            <a
              href={grant.website}
              target="_blank"
              rel="noreferrer"
              className="website-link"
            >
              Visit Portal →
            </a>

          </div>

        </div>

        <div className="reason-box">

          <h3>🤖 AI Recommendation</h3>

          <p>{recommendation.reason}</p>

        </div>

        <EligibilityCard eligibility={eligibility} />

      </div>

      {proposal && (
        <ProposalModal
          proposal={proposal}
          onClose={() => setProposal(null)}
        />
      )}
    </>
  );
}

export default GrantCard;