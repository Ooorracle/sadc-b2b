export function TradeWithConfidence() {
    return (
        <section className="bg-white py-20 px-6 md:px-12 lg:px-24 border-b border-slate-200">
            <div className="max-w-7xl mx-auto">
                <div className="mb-16">
                    <h2 className="text-3xl font-bold text-[#172554] mb-2">Trade With Confidence</h2>
                    <p className="text-slate-500 text-base">Business-focused tools designed to encourage trusted connections.</p>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div className="border border-slate-200 rounded-xl p-8 hover:shadow-md transition-shadow bg-slate-50/50">
                        <div className="text-4xl mb-6">🛡️</div>
                        <h3 className="text-xl font-bold text-[#172554] mb-3">Business Verification</h3>
                        <p className="text-sm text-slate-500 leading-relaxed">Business profiles undergo document-based verification to help users identify verified businesses.</p>
                    </div>
                    <div className="border border-slate-200 rounded-xl p-8 hover:shadow-md transition-shadow bg-slate-50/50">
                        <div className="text-4xl mb-6">📋</div>
                        <h3 className="text-xl font-bold text-[#172554] mb-3">Quotation Management</h3>
                        <p className="text-sm text-slate-500 leading-relaxed">Retailers can submit quotation requests while wholesalers manage and respond to enquiries.</p>
                    </div>
                    <div className="border border-slate-200 rounded-xl p-8 hover:shadow-md transition-shadow bg-slate-50/50">
                        <div className="text-4xl mb-6">🌍</div>
                        <h3 className="text-xl font-bold text-[#172554] mb-3">Regional Connections</h3>
                        <p className="text-sm text-slate-500 leading-relaxed">Discover business opportunities and suppliers across Southern African markets.</p>
                    </div>
                </div>
            </div>
        </section>
    );
}