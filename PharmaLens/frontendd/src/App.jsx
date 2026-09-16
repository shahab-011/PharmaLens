import { useState } from "react";
import "./App.css";

function App() {
  const [document, setDocument] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeDocument = async () => {
    if (!document.trim()) return;

    setLoading(true);
    setResult(null);
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(document),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Analysis failed");
      }

      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const clearAll = () => {
    setDocument("");
    setResult(null);
    setError("");
  };

  return (
    <div className="app">

      {/* Background */}
      <div className="background-glow"></div>

      {/* Navbar */}
      <header className="navbar">

        <div className="logo">
          <div className="logo-mark">P</div>

          <div>
            <h2>PharmaLens</h2>
            <span>Document Intelligence</span>
          </div>
        </div>

        <div className="system-status">
          <span className="status-dot"></span>
          System Online
        </div>

      </header>


      {/* Main */}
      <main className="container">

        {/* Heading */}
        <section className="hero">

          <span className="tag">
            AI · PHARMACEUTICAL INTELLIGENCE
          </span>

          <h1>
            Turn documents into
            <br />
            <span>structured intelligence.</span>
          </h1>

          <p>
            Extract clinical, drug, regulatory, efficacy and
            data-quality information from pharmaceutical documents.
          </p>

        </section>


        {/* Workspace */}
        <section className="workspace">

          {/* INPUT */}
          <div className="card">

            <div className="card-header">

              <div>
                <h3>Document</h3>
                <p>Paste your pharmaceutical document</p>
              </div>

              <span className="counter">
                {document.length} chars
              </span>

            </div>


            <textarea
              value={document}
              onChange={(e) => setDocument(e.target.value)}
              placeholder="Paste your pharmaceutical, clinical trial, regulatory or drug development document here..."
            />


            <div className="card-footer">

              <button
                className="primary-button"
                onClick={analyzeDocument}
                disabled={!document.trim() || loading}
              >

                {loading ? (
                  <>
                    <span className="spinner"></span>
                    Analyzing
                  </>
                ) : (
                  <>
                    Analyze Document
                    <span>→</span>
                  </>
                )}

              </button>

              <button
                className="secondary-button"
                onClick={clearAll}
              >
                Clear
              </button>

            </div>

          </div>


          {/* OUTPUT */}
          <div className="card output-card">

            <div className="card-header">

              <div>
                <h3>Structured Output</h3>
                <p>Pydantic validated intelligence</p>
              </div>

              <span className="json-label">
                JSON
              </span>

            </div>


            {/* Empty */}
            {!result && !loading && !error && (
              <div className="empty">

                <div className="empty-symbol">
                  {"{ }"}
                </div>

                <h4>No analysis yet</h4>

                <p>
                  Your structured pharmaceutical data
                  will appear here.
                </p>

              </div>
            )}


            {/* Loading */}
            {loading && (
              <div className="empty">

                <div className="loader"></div>

                <h4>Analyzing document</h4>

                <p>
                  Extracting structured pharmaceutical information...
                </p>

              </div>
            )}


            {/* Error */}
            {error && !loading && (
              <div className="error-box">

                <div className="error-title">
                  Analysis failed
                </div>

                <p>{error}</p>

              </div>
            )}


            {/* Result */}
            {result && !loading && !error && (
              <div className="result">

                <div className="result-top">

                  <div className="result-status">
                    <span></span>
                    Validated
                  </div>

                  <button
                    className="copy-button"
                    onClick={() =>
                      navigator.clipboard.writeText(
                        JSON.stringify(result, null, 2)
                      )
                    }
                  >
                    Copy JSON
                  </button>

                </div>


                <pre>
                  {JSON.stringify(result, null, 2)}
                </pre>

              </div>
            )}

          </div>

        </section>


        {/* Pipeline */}
        <section className="pipeline">

          <span>PIPELINE</span>

          <div className="pipeline-flow">

            <div>Document</div>

            <b>→</b>

            <div>Groq LLM</div>

            <b>→</b>

            <div>Pydantic</div>

            <b>→</b>

            <div>JSON</div>

          </div>

        </section>

      </main>


      {/* Footer */}
      <footer>
        PharmaLens · AI-powered pharmaceutical document intelligence
      </footer>

    </div>
  );
}

export default App;