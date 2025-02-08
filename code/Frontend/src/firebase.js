// Import necessary Firebase functions
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore"; // ✅ Import Firestore
import { getAnalytics } from "firebase/analytics";

// Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAx2mOcPpaju5_bkDZ54KbkU-1V_B-zPR4",
  authDomain: "ai-checker-pro.firebaseapp.com",
  projectId: "ai-checker-pro",
  storageBucket: "ai-checker-pro.appspot.com", // ✅ Fix storageBucket typo
  messagingSenderId: "237246859689",
  appId: "1:237246859689:web:3317b602f71a694952dcb8",
  measurementId: "G-Q677W5RZS3"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app); // ✅ Initialize Firestore

export { db }; // ✅ Export db to be used in other files
