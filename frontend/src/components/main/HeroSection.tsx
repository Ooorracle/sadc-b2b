import { Globe } from "lucide-react"

const HeroSection = () => {
    return (
        <div className="flex flex-col w-full bg-[#172554] px-6 md:px-12 lg:px-24 py-16 md:py-24">
            <div className="max-w-7xl mx-auto w-full">
                <div className='flex flex-row items-center gap-2 text-slate-300 bg-[#253b75] px-4 py-1.5 rounded-full mb-6 w-fit'>
                    <Globe className='h-4 w-4' />
                    <h4 className='text-[11px] font-bold tracking-wide'>ONE MARKETPLACE. ONE REGION. ENDLESS OPPORTUNITIES.</h4>
                </div>

                <h1 className="text-4xl md:text-6xl font-extrabold text-white mb-6 leading-tight max-w-3xl">
                    Connecting SADC Businesses. <span className="text-[#800000]">Empowering Trade.</span>
                </h1>

                <p className="text-lg md:text-xl text-slate-300 mb-10 max-w-3xl leading-relaxed">
                    Discover trusted suppliers, connect with wholesalers, source quality products and grow your business across Southern Africa.
                </p>

                <div className="relative w-full max-w-3xl mb-8">
                    <div className="flex items-center bg-white border border-slate-200 rounded-xl p-1.5 focus-within:ring-2 focus-within:ring-[#800000]/50 transition-shadow shadow-lg">
                        <input
                            type="text"
                            placeholder="What products are you looking for?"
                            className="flex-1 w-full px-4 py-3 outline-none bg-transparent text-sm text-slate-900 placeholder-slate-400"
                        />
                        <button className="px-8 py-3 bg-[#800000] text-white rounded-lg hover:bg-[#5C0A14] transition text-sm font-semibold whitespace-nowrap shadow-sm">
                            Search Products
                        </button>
                    </div>
                </div>

                <div className="flex flex-wrap gap-3 mt-4">
                    {["Electronics", "Consumables", "Agriculture", "Construction", "Automotive", "Sports"].map((cat) => (
                        <button key={cat} className="text-slate-300 text-sm font-medium border border-slate-600 hover:border-white hover:text-white px-4 py-1.5 rounded-full transition-colors">
                            {cat}
                        </button>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default HeroSection