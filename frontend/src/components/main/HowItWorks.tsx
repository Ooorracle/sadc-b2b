export function HowItWorks() {
    const steps = [
        { num: "01", title: "Create an Account", desc: "Register as a retailer or wholesaler and provide your business information." },
        { num: "02", title: "Verify Your Business", desc: "Submit the required business registration and verification documents." },
        { num: "03", title: "Connect & Discover", desc: "Find suppliers, browse products and submit quotation requests." },
        { num: "04", title: "Grow Your Business", desc: "Communicate with business partners and develop new trade opportunities." },
    ];

    return (
        <section className="bg-[#f8fafc] py-20 px-6 md:px-12 lg:px-24 border-b border-slate-200">
            <div className="max-w-7xl mx-auto">
                <div className="mb-16">
                    <h2 className="text-3xl font-bold text-[#172554] mb-2">How SADC B2B Works</h2>
                    <p className="text-slate-500 text-base">Simple steps to connect buyers and suppliers.</p>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
                    {steps.map((step) => (
                        <div key={step.num} className="flex flex-col items-center text-center">
                            <div className="w-20 h-20 rounded-full bg-[#800000]/10 flex items-center justify-center mb-6">
                                <span className="text-2xl font-bold text-[#800000]">{step.num}</span>
                            </div>
                            <h3 className="text-lg font-bold text-[#172554] mb-3">{step.title}</h3>
                            <p className="text-sm text-slate-500 leading-relaxed max-w-xs">{step.desc}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    );
}