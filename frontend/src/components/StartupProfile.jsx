function StartupProfile({ profile }) {
  if (!profile) return null;

  return (
    <div className="card">

      <h2 className="card-title">
        🌱 Startup Profile
      </h2>

      <div className="profile-grid">

        <div className="profile-item">
          <span className="label">🏭 Domain</span>
          <span className="value">{profile.domain}</span>
        </div>

        <div className="profile-item">
          <span className="label">🌍 Country</span>
          <span className="value">{profile.country}</span>
        </div>

        <div className="profile-item">
          <span className="label">🚀 Startup Stage</span>
          <span className="value">{profile.startup_stage}</span>
        </div>

        <div className="profile-item">
          <span className="label">💰 Funding Needed</span>
          <span className="funding">
            {profile.funding_needed}
          </span>
        </div>

      </div>

      <div className="tech-section">

        <h3>🛠 Technologies</h3>

        <div className="tech-list">

          {profile.technology?.map((tech, index) => (

            <span className="tech-chip" key={index}>
              {tech.replace("_", " ")}
            </span>

          ))}

        </div>

      </div>

    </div>
  );
}

export default StartupProfile;