import { useState } from "react";
import jsPDF from "jspdf";

function ProposalModal({ proposal, onClose }) {

  const [copied, setCopied] = useState(false);

  if (!proposal) return null;


  const proposalText =
    typeof proposal === "string"
      ? proposal
      : JSON.stringify(proposal, null, 2);



  const copyProposal = async () => {

    await navigator.clipboard.writeText(proposalText);

    setCopied(true);

    setTimeout(() => {
      setCopied(false);
    },2000);

  };

  const downloadPDF = () => {
    const doc = new jsPDF();
    doc.setFontSize(16);
    doc.text(
        "AI Generated Funding Proposal",
        20,
        20
    );
    
    doc.setFontSize(11);
    
    const lines = doc.splitTextToSize(
        proposalText,
        170
    );
    
    doc.text(
        lines,
        20,
        40
    );
    
    doc.save(
        "AI_Funding_Proposal.pdf"
    );
};


  return (

    <div className="modal-overlay">


      <div className="proposal-modal">


        {/* Header */}

        <div className="proposal-header">


          <div>

            <h2>
              📄 AI Generated Funding Proposal
            </h2>

            <p>
              Generated using Startup Intelligence Agent
            </p>

          </div>


          <button
            className="close-btn"
            onClick={onClose}
          >
            ✕
          </button>


        </div>




        {/* Document */}

        <div className="proposal-document">


          <div className="document-title">

            🚀 Startup Grant Proposal

          </div>


          <div className="document-content">


            {
              typeof proposal === "object" ?

              Object.entries(proposal).map(
                ([key,value],index)=>(

                  <div 
                    className="proposal-section"
                    key={index}
                  >

                    <h3>
                      {key.replaceAll("_"," ")}
                    </h3>

                    <p>
                      {
                        typeof value === "object"
                        ? JSON.stringify(value,null,2)
                        : value
                      }
                    </p>


                  </div>

                )
              )


              :

              <p>
                {proposalText}
              </p>

            }


          </div>


        </div>





        {/* Actions */}

        <div className="proposal-actions">


          <button
            className="copy-btn"
            onClick={copyProposal}
          >

            {
              copied
              ? "✔ Copied"
              : "📋 Copy Proposal"
            }

          </button>



          <button
            className="download-btn"
            onClick={downloadPDF}
            >
            📥 Download PDF
            </button>



        </div>



      </div>


    </div>

  );

}


export default ProposalModal;