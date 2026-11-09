import { Link } from "react-router-dom";
import SDLOGO from "../../assets/SDLOGO.png";

export default function Footer() {
    return (
        <footer className="bg-[#172554] text-slate-300 w-full mt-auto pt-16 pb-8">
            <div className="max-w-[1300px] mx-auto px-6 md:px-12 lg:px-24">
                <div className="grid grid-cols-1 md:grid-cols-12 gap-10 lg:gap-8 mb-12">
                    <div className="md:col-span-5 pr-0 lg:pr-16">
                        <div className="flex items-center mb-6">
                            <div className="bg-white rounded-xl px-4 py-2 flex items-center justify-center inline-block shadow-sm">
                                <img src={SDLOGO} alt="SADC B2B Logo" className="h-10 w-auto object-contain" />
                            </div>
                        </div>
                        <p className="text-sm text-slate-300 leading-relaxed font-medium max-w-sm">
                            Connecting wholesalers, retailers and suppliers through a regional business marketplace built to support trade and business growth across Southern Africa.
                        </p>
                    </div>

                    <div className="md:col-span-2">
                        <h4 className="text-white text-base font-bold mb-5 tracking-wide">Marketplace</h4>
                        <ul className="space-y-3.5 text-sm text-slate-300 font-medium">
                            <li><Link to="/categories" className="hover:text-white transition-colors">Categories</Link></li>
                            <li><Link to="/products" className="hover:text-white transition-colors">Products</Link></li>
                            <li><Link to="/suppliers" className="hover:text-white transition-colors">Suppliers</Link></li>
                            <li><Link to="/wholesale" className="hover:text-white transition-colors">Wholesale</Link></li>
                            <li><Link to="/retail" className="hover:text-white transition-colors">Retail</Link></li>
                        </ul>
                    </div>

                    <div className="md:col-span-3">
                        <h4 className="text-white text-base font-bold mb-5 tracking-wide">For Businesses</h4>
                        <ul className="space-y-3.5 text-sm text-slate-300 font-medium">
                            <li><Link to="/register/wholesaler" className="hover:text-white transition-colors">Become a Wholesaler</Link></li>
                            <li><Link to="/register/retailer" className="hover:text-white transition-colors">Become a Retailer</Link></li>
                            <li><Link to="/verification" className="hover:text-white transition-colors">Business Verification</Link></li>
                            <li><Link to="/help" className="hover:text-white transition-colors">Help Centre</Link></li>
                            <li><Link to="/contact" className="hover:text-white transition-colors">Contact Us</Link></li>
                        </ul>
                    </div>

                    <div className="md:col-span-2">
                        <h4 className="text-white text-base font-bold mb-5 tracking-wide">Legal</h4>
                        <ul className="space-y-3.5 text-sm text-slate-300 font-medium">
                            <li><Link to="/about" className="hover:text-white transition-colors">About Us</Link></li>
                            <li><Link to="/privacy" className="hover:text-white transition-colors">Privacy Policy</Link></li>
                            <li><Link to="/terms" className="hover:text-white transition-colors">Terms & Conditions</Link></li>
                            <li><Link to="/cookies" className="hover:text-white transition-colors">Cookie Policy</Link></li>
                        </ul>
                    </div>
                </div>

                <div className="pt-6 border-t border-slate-700/50 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-slate-400 font-medium">
                    <p>© {new Date().getFullYear()} SADC B2B. All rights reserved.</p>
                    <p>Connecting Businesses Across Southern Africa.</p>
                </div>
            </div>
        </footer>
    );
}