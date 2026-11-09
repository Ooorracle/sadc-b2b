import LoginPage from "@/pages/accounts/Login";
import { BrowserRouter, Routes, Route } from "react-router-dom";


export default function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </BrowserRouter>
  );
}