import { Link } from "react-router-dom";

export default function BusinessRegistration() {
    return (
        <div className="bg-[#172554] py-20 px-6 md:px-12 lg:px-24">
            <div className="max-w-7xl mx-auto">
                <div className="mb-12">
                    <h1 className="text-3xl md:text-4xl font-bold text-white tracking-tight mb-3">
                        Grow Your Business With SADC B2B
                    </h1>
                    <p className="text-slate-300 text-lg max-w-2xl">
                        Whether you supply products or source them, there is a place for you.
                    </p>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">
                    {/* Wholesaler Card */}
                    <div className="bg-[#1c2c4f] border border-[#334155] rounded-2xl p-8 lg:p-12 flex flex-col">
                        <div className="text-4xl mb-6">🏭</div>
                        <h2 className="text-2xl font-bold text-white mb-4">Become a Wholesaler</h2>
                        <p className="text-slate-300 text-base leading-relaxed mb-8 flex-1">
                            Showcase your products, connect with retailers, receive quotation requests and expand your distribution network across the SADC region.
                        </p>
                        <div>
                            <Link to="/register/wholesaler" className="inline-flex items-center gap-2 bg-[#800000] hover:bg-[#6a0000] text-white font-semibold px-6 py-3 rounded-lg transition-colors">
                                Register as Wholesaler <span aria-hidden="true">&rarr;</span>
                            </Link>
                        </div>
                    </div>

                    {/* Retailer Card */}
                    <div className="bg-[#1c2c4f] border border-[#334155] rounded-2xl p-8 lg:p-12 flex flex-col">
                        <div className="text-4xl mb-6">🏪</div>
                        <h2 className="text-2xl font-bold text-white mb-4">Register as a Retailer</h2>
                        <p className="text-slate-300 text-base leading-relaxed mb-8 flex-1">
                            Discover suppliers, compare product offers, request quotations and source products for your retail business.
                        </p>
                        <div>
                            <Link to="/register/retailer" className="inline-flex items-center gap-2 bg-white hover:bg-slate-100 text-[#172554] font-bold px-6 py-3 rounded-lg transition-colors">
                                Register as Retailer <span aria-hidden="true">&rarr;</span>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}