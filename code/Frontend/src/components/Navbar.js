import { Link } from "react-router-dom";
import "./Navbar.css"; // Import styles

function Navbar() {
  return (
    <nav className="navbar">
      <h1 className="logo">AI-Checker Pro</h1>
      <ul className="nav-links">
        <li><Link to="/">Home</Link></li>
        <li><Link to="/login">Login</Link></li>
        <li><Link to="/ask">Ask a Question</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
