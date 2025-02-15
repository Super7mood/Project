import { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const [loggedInUser, setLoggedInUser] = useState(localStorage.getItem("loggedInUser"));
  const navigate = useNavigate();

  // Ensure navbar updates instantly when login state changes
  useEffect(() => {
    const handleStorageChange = () => {
      setLoggedInUser(localStorage.getItem("loggedInUser")); // Update state when localStorage changes
    };

    window.addEventListener("storage", handleStorageChange); // Listen for localStorage updates

    return () => {
      window.removeEventListener("storage", handleStorageChange); // Cleanup on unmount
    };
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("loggedInUser"); // Clear stored user
    setLoggedInUser(null); // Update state instantly
    window.dispatchEvent(new Event("storage")); // Force navbar update across the app
    navigate("/login"); // Redirect to login page
  };

  return (
    <nav className="navbar">
      <h1 className="logo">AI-Checker Pro</h1>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/ask">Ask a Question</Link></li>
        {loggedInUser ? (
          <>
            <li className="user-info">Hi, {loggedInUser.split("@")[0]}!</li>
            <li><button className="logout-btn" onClick={handleLogout}>Logout</button></li>
          </>
        ) : (
          <li><Link to="/login">Login</Link></li>
        )}
      </ul>
    </nav>
  );
}

export default Navbar;
