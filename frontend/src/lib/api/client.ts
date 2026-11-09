import axios, {
  AxiosError,
  type AxiosRequestConfig,
  type InternalAxiosRequestConfig,
} from "axios";
import { useAuthStore } from "@/store/auth";

export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000/api";

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { "Content-Type": "application/json" },
});

// Attach access token to every request
api.interceptors.request.use((config: InternalAxiosRequestConfig) => {
  const token = useAuthStore.getState().access;
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auto-refresh on 401 once, then retry
let refreshPromise: Promise<string> | null = null;

async function refreshAccessToken(): Promise<string> {
  const { refresh, setTokens, logout } = useAuthStore.getState();
  if (!refresh) {
    logout();
    throw new Error("No refresh token");
  }
  try {
    const { data } = await axios.post<{ access: string }>(
      `${API_BASE_URL}/token/refresh/`,
      { refresh },
    );
    setTokens({ access: data.access, refresh });
    return data.access;
  } catch (err) {
    logout();
    throw err;
  }
}

api.interceptors.response.use(
  (res) => res,
  async (error: AxiosError) => {
    const original = error.config as
      | (AxiosRequestConfig & { _retry?: boolean })
      | undefined;

    if (
      error.response?.status === 401 &&
      original &&
      !original._retry &&
      !original.url?.includes("/token/refresh/") &&
      !original.url?.includes("/accounts/login/")
    ) {
      original._retry = true;
      try {
        refreshPromise = refreshPromise ?? refreshAccessToken();
        const newAccess = await refreshPromise;
        refreshPromise = null;
        original.headers = {
          ...original.headers,
          Authorization: `Bearer ${newAccess}`,
        };
        return api(original);
      } catch (e) {
        refreshPromise = null;
        return Promise.reject(e);
      }
    }
    return Promise.reject(error);
  },
);

// Helper to pull a human-readable error out of DRF error shapes
export function extractApiError(err: unknown): string {
  if (axios.isAxiosError(err)) {
    const data = err.response?.data;
    if (typeof data === "string") return data;
    if (data && typeof data === "object") {
      if ("detail" in data && typeof data.detail === "string") return data.detail;
      // DRF field errors: { email: ["..."], password: ["..."] }
      const first = Object.values(data as Record<string, unknown>)[0];
      if (Array.isArray(first) && typeof first[0] === "string") return first[0];
      if (typeof first === "string") return first;
    }
    return err.message;
  }
  if (err instanceof Error) return err.message;
  return "Something went wrong.";
}