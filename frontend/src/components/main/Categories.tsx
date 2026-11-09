import { useQuery } from "@tanstack/react-query";
import { ArrowRight, Loader2, PackageX } from "lucide-react";
import { fetchCategories } from "@/lib/api/Categories";

export default function Categories() {
  const { data: categories, isLoading, isError } = useQuery({
    queryKey: ["categories"],
    queryFn: fetchCategories,
    retry: false,
  });

  return (
    <div className="flex flex-col px-6 md:px-12 lg:px-24 py-20 bg-[#f8fafc] border-b border-slate-200">
      <div className="max-w-7xl mx-auto w-full">
        <div className="flex flex-row justify-between items-end mb-12">
          <div className="flex flex-col">
            <h2 className="font-bold text-3xl text-[#172554]">Categories</h2>
            <p className="text-slate-500 mt-2 text-base">Discover products from different industries and suppliers.</p>
          </div>
          {categories && categories.length > 0 && (
            <a href="/categories" className="group flex items-center gap-1 text-slate-700 hover:text-[#800000] font-semibold text-sm transition-colors mb-1">
              <span>View all categories</span>
              <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-1" />
            </a>
          )}
        </div>

        {isLoading && (
          <div className="flex items-center justify-center py-12 text-slate-500">
            <Loader2 className="h-6 w-6 animate-spin mr-2" />
            <span>Loading categories...</span>
          </div>
        )}

        {isError && (
          <div className="bg-red-50 text-red-600 p-4 rounded-lg border border-red-200">
            Failed to load categories. Please check your backend connection.
          </div>
        )}

        {!isLoading && !isError && categories?.length === 0 && (
          <div className="flex flex-col items-center justify-center py-16 bg-white rounded-xl border border-slate-200 border-dashed">
            <PackageX className="h-10 w-10 text-slate-400 mb-3" />
            <h3 className="text-slate-900 font-medium text-lg">No categories yet</h3>
            <p className="text-slate-500 text-sm mt-1">Categories will appear here once they are added.</p>
          </div>
        )}

        {!isLoading && !isError && categories && categories.length > 0 && (
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
            {categories.map((category) => (
              <div key={category.id} className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow cursor-pointer flex flex-col items-start">
                <div className="w-12 h-12 bg-[#172554]/10 rounded-lg flex items-center justify-center mb-4">
                  <span className="text-[#172554] font-bold text-xl">
                    {category.name.charAt(0).toUpperCase()}
                  </span>
                </div>
                <h3 className="font-bold text-slate-900 text-lg">{category.name}</h3>
                <p className="text-sm text-slate-500 mt-2 line-clamp-2 leading-relaxed">
                  {category.description || "Explore products in this category."}
                </p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}