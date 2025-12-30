import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// You can add interceptors here if you need to handle tokens, etc.
// For example, to add the auth token to every request
apiClient.interceptors.request.use(config => {
    const token = localStorage.getItem('access');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, error => {
    return Promise.reject(error);
});

export default apiClient;
