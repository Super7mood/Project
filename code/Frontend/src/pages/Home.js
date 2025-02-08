import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container">
      <h1>Welcome to AI-Checker Pro</h1>
      <p>Compare AI responses and get the most accurate answer.</p>
      <Link to="/login">
        <button className="nav-btn">Login</button>
      </Link>
      <Link to="/ask">
        <button className="nav-btn">Ask a Question</button>
      </Link>
    </div>
  );
}

export default Home;
