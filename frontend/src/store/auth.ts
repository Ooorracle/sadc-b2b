import { create } from "zustand";
import { persist } from "zustand/middleware";
import type { AuthTokens, User } from "@/types/auth";

interface AuthState {
  user: User | null;
  access: string | null;
  refresh: string | null;
  isHydrated: boolean;
  setSession: (user: User, tokens: AuthTokens) => void;
  setTokens: (tokens: AuthTokens) => void;
  setUser: (user: User) => void;
  logout: () => void;
  markHydrated: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      user: null,
      access: null,
      refresh: null,
      isHydrated: false,
      setSession: (user, tokens) =>
        set({ user, access: tokens.access, refresh: tokens.refresh }),
      setTokens: (tokens) =>
        set({ access: tokens.access, refresh: tokens.refresh }),
      setUser: (user) => set({ user }),
      logout: () => set({ user: null, access: null, refresh: null }),
      markHydrated: () => set({ isHydrated: true }),
    }),
    {
      name: "sadc-auth",
      partialize: (s) => ({
        user: s.user,
        access: s.access,
        refresh: s.refresh,
      }),
      onRehydrateStorage: () => (state) => {
        state?.markHydrated();
      },
    },
  ),
);

export const useIsAuthenticated = () =>
  useAuthStore((s) => Boolean(s.access && s.user));