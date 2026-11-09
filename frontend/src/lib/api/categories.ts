import { api } from "./client";

export interface Category {
  id: number;
  name: string;
  description: string;
  slug: string;
}

export async function fetchCategories(): Promise<Category[]> {
  const { data } = await api.get<Category[] | { results: Category[] }>("/catalogue/categories/");
  
  if (Array.isArray(data)) return data;
  return data.results || [];
}