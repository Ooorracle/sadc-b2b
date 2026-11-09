export interface User {
  id: number;
  username: string;
  first_name: string;
  last_name: string;
  full_name: string;
  email: string;
  phone_number: string | null;
  address: string | null;
  city: string | null;
  country: string | null;
  is_verified: boolean;
  date_joined: string;
}

export interface AuthTokens {
  access: string;
  refresh: string;
}

export interface LoginResponse {
  message: string;
  user: User;
  tokens: AuthTokens;
}

export interface RegisterPayload {
  first_name: string;
  last_name: string;
  email: string;
  password: string;
  password2: string;
  phone_number?: string;
  address?: string;
  city?: string;
  country?: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}