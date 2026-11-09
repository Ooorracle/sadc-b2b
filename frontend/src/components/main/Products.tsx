import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { ArrowRight, Loader2, PackageX, Image as ImageIcon, Check } from "lucide-react";
import { fetchProducts } from "@/lib/api/Product";

const BACKEND_URL = "http://127.0.0.1:8000";

function ProductCard({ product }: { product: any }) {
    const [isExpanded, setIsExpanded] = useState(false);
    const description = product.description || "No description available.";
    const isLongText = description.length > 100;

    const getImageUrl = (imageField: any) => {
        if (!imageField) return null;
        const path = typeof imageField === 'string' ? imageField : imageField.url;
        if (!path) return null;
        return path.startsWith("http") ? path : `${BACKEND_URL}${path}`;
    };

    const imageUrl = getImageUrl(product.image);

    return (
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow flex flex-col overflow-hidden">
            <div className="w-full h-48 bg-slate-100 relative flex items-center justify-center p-2">
                <div className="absolute top-3 left-3 bg-green-100 text-green-800 text-xs font-bold px-2.5 py-1 rounded-md z-10">Popular</div>
                {imageUrl ? (
                    <img src={imageUrl} alt={product.name} className="w-full h-full object-cover rounded-t-lg" onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }} />
                ) : (
                    <ImageIcon className="h-12 w-12 text-slate-300" />
                )}
            </div>

            <div className="p-6 flex flex-col flex-1">
                <h3 className="text-xl font-bold text-[#172554] leading-tight mb-1">{product.name}</h3>
                <div className="flex items-center gap-1 text-sm text-slate-500 mb-4">
                    <span>{product.business_name || "Unknown Supplier"}</span>
                    <span className="flex items-center text-green-600 font-semibold text-xs ml-1">
                        <Check className="h-3 w-3 mr-0.5" strokeWidth={3} /> Verified
                    </span>
                </div>

                <div className="flex items-baseline gap-1 mb-4">
                    <span className="text-2xl font-extrabold text-[#800000]">
                        {product.currency === 'USD' ? '$' : product.currency}{Number(product.base_price || 0).toFixed(2)}
                    </span>
                    <span className="text-sm font-medium text-slate-500">/ {product.unit || "unit"}</span>
                </div>

                <div className="mb-6 flex-1">
                    <p className={`text-sm text-slate-500 leading-relaxed ${!isExpanded ? "line-clamp-3" : ""}`}>{description}</p>
                    {isLongText && (
                        <button onClick={(e) => { e.stopPropagation(); setIsExpanded(!isExpanded); }} className="text-[#800000] text-xs font-semibold mt-2 hover:underline focus:outline-none">
                            {isExpanded ? "See less" : "See more"}
                        </button>
                    )}
                </div>

                <div className="mt-auto pt-4 border-t border-slate-100 flex items-center justify-between">
                    <div className="text-sm font-medium text-slate-600">MOQ: {product.moq || "1,000 units"}</div>
                    <button className="bg-[#172554] hover:bg-slate-800 text-white font-medium text-sm px-5 py-2.5 rounded-lg transition-colors">
                        Request Quote
                    </button>
                </div>
            </div>
        </div>
    );
}

export default function Products() {
    const { data: products, isLoading, isError } = useQuery({ queryKey: ["products"], queryFn: fetchProducts, retry: false });

    return (
        <div className="flex flex-col px-6 md:px-12 lg:px-24 py-20 bg-white">
            <div className="max-w-7xl mx-auto w-full">
                <div className="flex flex-row justify-between items-end mb-12">
                    <div className="flex flex-col">
                        <h2 className="font-bold text-3xl text-[#172554]">Products</h2>
                        <p className="text-slate-500 mt-2 text-base">Discover products from different industries and suppliers.</p>
                    </div>
                    {products && products.length > 0 && (
                        <a href="/products" className="group flex items-center gap-1 text-slate-700 hover:text-[#800000] font-semibold text-sm transition-colors mb-1">
                            <span>View all products</span>
                            <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
                        </a>
                    )}
                </div>

                {isLoading && <div className="flex items-center justify-center py-12 text-slate-500"><Loader2 className="h-6 w-6 animate-spin mr-2" /><span>Loading products...</span></div>}

                {isError && <div className="bg-red-50 text-red-600 p-4 rounded-lg border border-red-200">Failed to load products. Please check your backend connection.</div>}

                {!isLoading && !isError && products?.length === 0 && (
                    <div className="flex flex-col items-center justify-center py-16 bg-slate-50 rounded-xl border border-slate-200 border-dashed">
                        <PackageX className="h-10 w-10 text-slate-400 mb-3" />
                        <h3 className="text-slate-900 font-medium text-lg">No products yet</h3>
                        <p className="text-slate-500 text-sm mt-1">Products will appear here once they are added.</p>
                    </div>
                )}

                {!isLoading && !isError && products && products.length > 0 && (
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                        {products.map((product) => <ProductCard key={product.id} product={product} />)}
                    </div>
                )}
            </div>
        </div>
    );
}