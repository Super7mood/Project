import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(""); // For error messages
  const [loading, setLoading] = useState(false); // Loading state
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(""); // Clear previous errors

    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }

    setLoading(true); // Show loading state

    try {
      const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      const data = await res.json();
      setLoading(false); // Hide loading state

      if (res.ok) {
        console.log("✅ Login successful:", data);
        localStorage.setItem("loggedInUser", email);
        window.dispatchEvent(new Event("storage")); // Force navbar to update instantly
        navigate("/ask"); // Redirect after successful login
      } else {
        setError(data.message || "Login failed. Please check your credentials.");
      }
    } catch (err) {
      setLoading(false);
      console.error("❌ Login request failed:", err);
      setError("Error connecting to the server. Please try again.");
    }
  };

  return (
    <div className="container">
      <h1>Login</h1>
      {error && <p className="error">{error}</p>} {/* Show error message */}
      <form onSubmit={handleLogin}>
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? "Logging in..." : "Login"}
        </button>
      </form>

      {/* ✅ Improved Sign-Up Link */}
      <p>
        Don't have an account?{" "}
        <button
          className="signup-btn"
          onClick={() => navigate("/signup")}
          aria-label="Go to Sign Up"
        >
          Sign up here
        </button>
      </p>
    </div>
  );
}

export default Login;
