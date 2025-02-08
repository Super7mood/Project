import React from "react";
import ReactDOM from "react-dom/client"; // ✅ Use React 18 createRoot
import { BrowserRouter } from "react-router-dom"; // ✅ Import Router
import App from "./App"; // ✅ Import main component
import "./styles.css"; // ✅ Keep your existing styles

const root = ReactDOM.createRoot(document.getElementById("root")); // ✅ Correct for React 18

root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
