import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Navbar from "./components/main/Navbar";
import Main from "./pages/Main";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/navbar" element={<Navbar />} />
        <Route path="/main" element={<Main />} />
        <Route path="/" element={<Navigate to="/main" />} />
      </Routes>
    </BrowserRouter>
  );
}