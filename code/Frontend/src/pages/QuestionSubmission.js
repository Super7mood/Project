import { useState, useEffect } from "react";
import { db } from "../firebase";
import { collection, addDoc, query, where, orderBy, onSnapshot } from "firebase/firestore";
import RankedResponses from "../components/RankedResponses";

import "../styles.css";

function QuestionSubmission() {
  const [queryText, setQueryText] = useState(""); // Stores the user's question input
  const [response, setResponse] = useState([]); // Stores multiple AI responses
  const [error, setError] = useState(""); // Stores error messages
  const [submissions, setSubmissions] = useState([]); // Stores previous questions for the logged-in user
  const [showPrevious, setShowPrevious] = useState(false); // Toggle visibility for previous submissions

  let userIdentifier = localStorage.getItem("loggedInUser");
  if (!userIdentifier) {
    if (!localStorage.getItem("guestID")) {
      localStorage.setItem("guestID", `guest-${Math.random().toString(36).substr(2, 9)}`);
    }
    userIdentifier = localStorage.getItem("guestID");
  }

  useEffect(() => {
    if (!userIdentifier) return;

    const q = query(
      collection(db, "submissions"),
      where("user", "==", userIdentifier),
      orderBy("timestamp", "desc")
    );

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const fetchedSubmissions = snapshot.docs.map((doc) => ({
        id: doc.id,
        ...doc.data(),
      }));

      console.log("Fetched Previous Submissions:", fetchedSubmissions);
      setSubmissions(fetchedSubmissions);
    });

    return () => unsubscribe();
  }, [userIdentifier]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          question: queryText,
          email: userIdentifier,
        }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response from the backend.");
      }

      const data = await res.json();
      console.log("Received Data from Backend:", data); // Debugging log
      
      let newResponses = Object.entries(data).map(([model, responseDetails]) => ({
        model,
        response: typeof responseDetails === "object" && responseDetails.response 
            ? responseDetails.response 
            : responseDetails || "No response available",
        score: responseDetails?.score !== undefined ? responseDetails.score : "N/A"
      }));

      await addDoc(collection(db, "submissions"), {
        user: userIdentifier,
        query: queryText,
        responses: data,
        timestamp: new Date(),
      });

      console.log(`✅ Submission stored in Firestore for ${userIdentifier}`);
      setQueryText("");
      setResponse(newResponses);
    } catch (err) {
      console.error("Error:", err);
      setError("Error connecting to the backend.");
    }
  };

  return (
    <div className="container">
      <h1>Ask AI-Checker Pro</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={queryText}
          onChange={(e) => setQueryText(e.target.value)}
          placeholder="Enter your question"
          required
        />
        <button type="submit">Submit</button>
      </form>
      {error && <p className="error">{error}</p>}
      <div className="response-container">
        <h2>Latest Response:</h2>
        {response.length === 0 ? (
          <p>No response yet.</p>
        ) : (
          response.map((res, index) => (
            <div key={index} className={`response-box ${res.model.toLowerCase()}`}>
              <h3>{res.model}</h3>
              <p>Response: {res.response}</p>
              <p>Score: {res.score}</p>
            </div>
          ))
        )}
      </div>
      <button className="toggle-btn" onClick={() => setShowPrevious(!showPrevious)}>
        {showPrevious ? "Hide Previous Responses" : "View Previous Responses"}
      </button>
      {showPrevious && (
        <div className="previous-submissions">
          <h2>Your Previous Submissions</h2>
          {submissions.length === 0 ? (
            <p>No previous submissions found.</p>
          ) : (
            submissions.map((submission) => (
              <div key={submission.id} className="response-box previous-response-box">
                <h3>Question:</h3>
                <p>{submission.query}</p>
                <h3>AI Responses:</h3>
                {Object.entries(submission.responses).map(([model, responseDetails], index) => (
                  <div key={index} className={`response-box ${model.toLowerCase()}`}>
                    <h4>{model}</h4>
                    <p>Response: {typeof responseDetails === "object" && responseDetails.response ? responseDetails.response : responseDetails || "No response available"}</p>
                    <p>Score: {responseDetails?.score !== undefined ? responseDetails.score : "N/A"}</p>
                  </div>
                ))}
                <small>🕒 {submission.timestamp?.toDate ? new Date(submission.timestamp.toDate()).toLocaleString() : "N/A"}</small>
              </div>
            ))
          )}
        </div>
      )}
    </div>
  );
}

export default QuestionSubmission;
