import { useState } from "react";
import "./App.css";

function App() {
  const [documentText, setDocumentText] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const analyzeDocument = async () => {
    if (!documentText.trim()) {
      return;
    }

    setLoading(true);
    setResult("");

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          document: documentText,
        }),
      });

      const data = await response.json();

      setResult(data.result);
    } catch (error) {
      setResult("Unable to connect to PharmaLens backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">

      <header className="header">
        <div className="brand">

          <div className="logo">
            P
          </div>

          <div>
            <h1>PharmaLens</h1>
            <p>Pharmaceutical Document Intelligence</p>
          </div>

        </div>
      </header>


      <main className="container">

        <section className="input-card">

          <h2>Analyze Pharmaceutical Document</h2>

          <p className="description">
            Paste a pharmaceutical, clinical trial, or drug development
            document to extract useful information.
          </p>

          <textarea
            value={documentText}
            onChange={(e) => setDocumentText(e.target.value)}
            placeholder="Paste your pharmaceutical document here..."
          />

          <button
            onClick={analyzeDocument}
            disabled={loading || !documentText.trim()}
          >
            {loading ? "Analyzing..." : "Analyze Document"}
          </button>

        </section>


        {result && (
          <section className="result-card">

            <div className="result-header">

              <h2>Analysis Result</h2>

              <span>PharmaLens AI</span>

            </div>

            <div className="result">
              {result}
            </div>

          </section>
        )}

      </main>

    </div>
  );
}

export default App;