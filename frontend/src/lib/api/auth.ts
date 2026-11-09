import { api } from "./client";
import type {
  LoginPayload,
  LoginResponse,
  RegisterPayload,
  User,
} from "@/types/auth";

export async function login(payload: LoginPayload): Promise<LoginResponse> {
  const { data } = await api.post<LoginResponse>(
    "/accounts/login/",
    payload,
  );
  return data;
}

export async function register(
  payload: RegisterPayload,
): Promise<LoginResponse> {
  const { data } = await api.post<LoginResponse>(
    "/accounts/register/",
    payload,
  );
  return data;
}

export async function fetchCurrentUser(): Promise<User> {
  const { data } = await api.get<{ user: User }>("/accounts/me/");
  return data.user;
}