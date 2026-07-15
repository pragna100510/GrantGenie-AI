from agents.profile_agent import analyze_startup
from agents.grant_agent import recommend_grants
from agents.eligibility_agent import check_eligibility


def run_agent_workflow(description: str):

    # Step 1 - Analyze startup
    profile = analyze_startup(description)

    # Step 2 - Recommend grants
    grants = recommend_grants(profile)

    # Step 3 - Eligibility Agent
    grant_analysis = []

    for recommendation in grants:

        grant = recommendation["grant"]

        eligibility = check_eligibility(
            profile,
            grant
        )

        grant_analysis.append({
            "grant": grant,
            "recommendation": {
                "match_score": recommendation["match_score"],
                "reason": recommendation["reason"]
            },
            "eligibility": eligibility
        })

    return {
        "startup_profile": profile,
        "grant_analysis": grant_analysis
    }