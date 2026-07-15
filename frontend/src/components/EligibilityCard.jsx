function EligibilityCard({ eligibility }) {

  if (!eligibility) return null;

  const score = eligibility.eligibility_score || 0;

  return (

    <div className="eligibility-card">

      <div className="eligibility-header">

        <div>
          <h2>
            🔍 Eligibility Analysis
          </h2>

          <p>
            AI-based grant requirement verification
          </p>
        </div>


        <div
          className={
            eligibility.eligible
              ? "status-pill eligible"
              : "status-pill not-eligible"
          }
        >

          {eligibility.eligible
            ? "✔ Eligible"
            : "✖ Not Eligible"}

        </div>

      </div>


      {/* Score Section */}

      <div className="score-section">

        <div className="score-top">

          <span>
            Eligibility Score
          </span>

          <strong>
            {score}%
          </strong>

        </div>


        <div className="progress-container">

          <div
            className="progress-bar"
            style={{
              width: `${score}%`
            }}
          >

          </div>

        </div>

      </div>



      {/* Matched Conditions */}

      <div className="condition-section">

        <h3>
          ✅ Matched Requirements
        </h3>


        {
          eligibility.matched_conditions?.length > 0 ?

          <div className="condition-list">

            {
              eligibility.matched_conditions.map(
                (item,index)=>(

                  <div 
                    className="condition success-condition"
                    key={index}
                  >

                    <span>
                      ✓
                    </span>

                    {item}

                  </div>

                )
              )
            }

          </div>

          :

          <p className="empty">
            No matching conditions found
          </p>

        }

      </div>




      {/* Missing Requirements */}

      <div className="condition-section">


        <h3>
          ❌ Missing Requirements
        </h3>


        {
          eligibility.missing_requirements?.length > 0 ?

          <div className="condition-list">


          {
            eligibility.missing_requirements.map(
              (item,index)=>(

                <div
                  className="condition danger-condition"
                  key={index}
                >

                  <span>
                    ✕
                  </span>

                  {item}

                </div>

              )
            )
          }


          </div>


          :

          <p className="empty">
            No missing requirements 🎉
          </p>


        }


      </div>




      {/* Recommendation */}

      <div className="recommendation-box">

        <h3>
          💡 Recommendation
        </h3>

        <p>
          {eligibility.recommendation}
        </p>

      </div>


    </div>

  );

}


export default EligibilityCard;