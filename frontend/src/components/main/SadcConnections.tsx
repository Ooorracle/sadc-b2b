export function SADCConnections() {
    const countries = [
        { code: "AO", name: "Angola" }, { code: "BW", name: "Botswana" }, { code: "KM", name: "Comoros" },
        { code: "CD", name: "DR Congo" }, { code: "SZ", name: "Eswatini" }, { code: "LS", name: "Lesotho" },
        { code: "MG", name: "Madagascar" }, { code: "MW", name: "Malawi" }, { code: "MU", name: "Mauritius" },
        { code: "MZ", name: "Mozambique" }, { code: "NA", name: "Namibia" }, { code: "SC", name: "Seychelles" },
        { code: "ZA", name: "South Africa" }, { code: "TZ", name: "Tanzania" }, { code: "ZM", name: "Zambia" },
        { code: "ZW", name: "Zimbabwe" },
    ];

    return (
        <section className="bg-[#f8fafc] py-20 px-6 md:px-12 lg:px-24">
            <div className="max-w-5xl mx-auto text-center">
                <h2 className="text-3xl font-bold text-[#172554] mb-3">Connecting the SADC Region</h2>
                <p className="text-slate-500 text-base mb-12">Building business connections across Southern Africa.</p>
                <div className="flex flex-wrap justify-center gap-3">
                    {countries.map((country) => (
                        <div key={country.code} className="bg-white border border-slate-200 rounded-lg px-5 py-2.5 text-sm font-semibold text-slate-700 shadow-sm flex items-center gap-2 hover:border-[#172554] transition-colors cursor-pointer">
                            <span className="text-slate-400 text-xs">{country.code}</span>
                            {country.name}
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}