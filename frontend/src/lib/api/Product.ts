import { api } from './client';


export interface Product {
    id: number;
    name: string;
    description?: string;
    currency: string;
    base_price: number;
    category_name: string;
    business_name: string;
    created_at: string;
    image: {
        url: string;
    };
}

export async function fetchProducts(): Promise<Product[]> {
    const { data } = await api.get<Product[] | { results: Product[] }>("/catalogue/");
    if (Array.isArray(data)) return data;
    return data.results || [];
}
