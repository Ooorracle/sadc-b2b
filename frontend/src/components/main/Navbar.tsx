import { useState } from 'react';
import { Link } from 'react-router-dom';
import SDLOGO from "../../assets/SDLOGO.png";
import { Search, ShoppingCart } from 'lucide-react';

const Navbar = () => {
    const [open, setOpen] = useState(false);

    return (
        <nav className="flex items-center justify-between px-6 md:px-12 lg:px-24 py-4 border-b border-slate-200 bg-white w-full relative z-50">
            {/* Left: Logo */}
            <Link to="/">
                <img src={SDLOGO} alt="Logo" className="h-10 w-auto" />
            </Link>

            {/* Right: Links & Actions */}
            <div className="hidden md:flex items-center gap-8">
                <Link to="/" className="text-sm font-medium text-slate-700 hover:text-[#172554] transition-colors">Home</Link>
                <Link to="/categories" className="text-sm font-medium text-slate-700 hover:text-[#172554] transition-colors">Categories</Link>
                <Link to="/products" className="text-sm font-medium text-slate-700 hover:text-[#172554] transition-colors">Products</Link>
                <Link to="/businesses" className="text-sm font-medium text-slate-700 hover:text-[#172554] transition-colors">For Businesses</Link>
                <Link to="/about" className="text-sm font-medium text-slate-700 hover:text-[#172554] transition-colors">About us</Link>

                <div className="hidden lg:flex items-center text-sm gap-2 bg-slate-100 px-4 py-2 rounded-full focus-within:ring-2 focus-within:ring-[#172554]/20 transition-all">
                    <input className="w-48 bg-transparent outline-none placeholder-slate-400 text-sm text-slate-900" type="text" placeholder="Search products" />
                    <Search className="h-4 w-4 text-slate-500" />
                </div>

                <div className="relative cursor-pointer text-slate-700 hover:text-[#172554]">
                    <ShoppingCart className="h-6 w-6" />
                    <span className="absolute -top-2 -right-2 text-[10px] font-bold text-white bg-[#800000] w-4 h-4 rounded-full flex items-center justify-center border border-white">
                        0
                    </span>
                </div>

                <Link to="/login" className="px-6 py-2.5 bg-[#800000] hover:bg-[#5C0A14] transition text-white rounded-lg text-sm font-semibold shadow-sm">
                    Login
                </Link>
            </div>

            {/* Mobile Toggle */}
            <button onClick={() => setOpen(!open)} aria-label="Menu" className="md:hidden text-slate-900">
                <svg width="24" height="24" viewBox="0 0 21 15" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect width="21" height="1.5" rx=".75" fill="currentColor" />
                    <rect x="8" y="6" width="13" height="1.5" rx=".75" fill="currentColor" />
                    <rect x="6" y="13" width="15" height="1.5" rx=".75" fill="currentColor" />
                </svg>
            </button>

            {/* Mobile Menu */}
            <div className={`${open ? 'flex' : 'hidden'} absolute top-[72px] left-0 w-full bg-white border-b border-slate-200 shadow-lg py-4 flex-col items-start gap-4 px-6 text-sm z-50`}>
                <Link to="/" className="block font-medium text-slate-700">Home</Link>
                <Link to="/categories" className="block font-medium text-slate-700">Categories</Link>
                <Link to="/products" className="block font-medium text-slate-700">Products</Link>
                <Link to="/login" className="w-full text-center px-6 py-3 mt-2 bg-[#800000] text-white rounded-lg font-semibold">
                    Login
                </Link>
            </div>
        </nav>
    );
};

export default Navbar;