import axios from "axios";
import { logout } from "./utils/auth";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL,
    withCredentials: true,
    headers: {
        'Content-Type': 'application/json',
    },
    xsrfCookieName: 'csrftoken',
    xsrfHeaderName: 'X-CSRFToken',
});

api.interceptors.request.use(config => {
    const token = localStorage.getItem('access_token')
    if (token) {
        config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
}, error => Promise.reject(error));

api.interceptors.response.use(response => response, async error => {
    if (error.response.status === 401) {
        const refreshToken = localStorage.getItem('refresh_token');
        if (refreshToken) {
            try {
                const response = await api.post('token/refresh/', { refresh: refreshToken });
                localStorage.setItem('access_token', response.data.access);
                error.config.headers['Authorization'] = `Bearer ${response.data.access}`;
                return api.request(error.config);
            } catch (refreshError) {
                console.error('Refresh token expired or invalid.');
                localStorage.removeItem('access_token');
                localStorage.removeItem('refresh_token');
                logout();
            }
        } else {
            logout();
        }
    }
    return Promise.reject(error);
});

export default api;
