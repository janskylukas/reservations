import api from "@/api";

export const login = async (credentials: { username: string, password: string }) => {
    console.log(credentials)
    const response = await api.post('/token/', credentials);

    const { access, refresh } = response.data;

    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);


    return response.data;
};

export const getUserProfile = async () => {
    const response = await api.get('/accounts/profile/')
    return response.data;
};
