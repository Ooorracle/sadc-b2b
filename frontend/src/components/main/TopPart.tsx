const TopPart = () => {
    return (
        <div className="flex flex-row justify-between items-center gap-3 px-6 md:px-12 lg:px-24 py-2.5 bg-[#172554] w-full">
            <h4 className="text-xs text-slate-300 font-medium whitespace-nowrap">
                Welcome to SADC B2B – Connecting businesses across Southern Africa
            </h4>
            <div className="flex flex-row items-center gap-6 whitespace-nowrap">
                <a href="#" className="text-xs font-medium text-slate-300 hover:text-white transition-colors">Help center</a>
                <a href="#" className="text-xs font-medium text-slate-300 hover:text-white transition-colors">Track orders</a>
                <a href="#" className="text-xs font-medium text-slate-300 hover:text-white transition-colors">Sell on SADC B2B</a>
            </div>
        </div>
    )
}
export default TopPart