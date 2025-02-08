import { Routes, Route } from "react-router-dom"; // ❌ DO NOT import BrowserRouter here
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import QuestionSubmission from "./pages/QuestionSubmission";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

function App() {
  return (
    <>
      <Navbar /> 
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/ask" element={<QuestionSubmission />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
