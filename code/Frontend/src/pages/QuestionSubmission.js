// Ayoub comment:
// To do: if possible try to comment as many lines as possible so it will look more nice and it will be easier for me to understand

import { useState, useEffect } from "react";
import { db } from "../firebase"; // ✅ Correct path based on your structure
import { collection, addDoc, query, orderBy, onSnapshot } from "firebase/firestore";

function QuestionSubmission() {
  const [queryText, setQueryText] = useState("");
  const [response, setResponse] = useState("");
  const [error, setError] = useState("");
  const [submissions, setSubmissions] = useState([]); // Stores previous questions

  // 🔹 Fetch previous submissions in real-time
  useEffect(() => {
    const q = query(collection(db, "submissions"), orderBy("timestamp", "desc"));
    const unsubscribe = onSnapshot(q, (snapshot) => {
      setSubmissions(snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      })));
    });

    return () => unsubscribe(); // Cleanup on unmount
  }, []);

  // 🔹 Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      // Send question to Flask backend
      const res = await fetch("http://127.0.0.1:5000/api/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: queryText }),
      });

      if (!res.ok) {
        throw new Error("Failed to fetch response from the backend.");
      }

      const data = await res.json();
      setResponse(data.response);

      // 🔹 Store query & response in Firestore
      await addDoc(collection(db, "submissions"), {
        query: queryText,
        response: data.response,
        timestamp: new Date(),
      });

      console.log("✅ Submission stored in Firestore!");
      setQueryText(""); // Clear input after submission

    } catch (err) {
      console.error("Error:", err);
      setError("Error connecting to the backend.");
    }
  };

  return (
    <div className="container">
      <h1>Ask AI-Checker Pro</h1>

      {/* 🔹 Submission Form */}
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

      {/* 🔹 Display Error if Any */}
      {error && <p className="error">{error}</p>}

      {/* 🔹 AI Response */}
      <div>
        <h2>Response:</h2>
        <p>{response || "No response yet."}</p>
      </div>

      {/* 🔹 Display Previous Submissions */}
      <h2>Previous Submissions</h2>
      <ul>
        {submissions.map((submission) => (
          <li key={submission.id}>
            <strong>Question:</strong> {submission.query} <br />
            <strong>Response:</strong> {submission.response} <br />
            <small>🕒 {new Date(submission.timestamp.toDate()).toLocaleString()}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default QuestionSubmission;
