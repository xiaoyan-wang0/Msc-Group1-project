import axios from 'axios';
import env from "@/env.js";
class myAxios {
    amdbAxios(axiosConfig) {
        const service = axios.create({
            baseURL: "/api", // amdb api
            timeout: 20000, // time out
            headers: { 'Content-Type': 'multipart/form-data' }
        });
        return service(axiosConfig)
    }

    othersAxios(axiosConfig) {
        const service = axios.create({
            baseURL: env.tmdbmovieapi, // tmdb api
            timeout: 20000, // time out
        });
        return service(axiosConfig)
    }
}

export default new myAxios();