import axios from 'axios';
import env from "@/env.js";

// const API_URL = '/api/member/';
const API_URL = env.AMDBAPI + 'member/';

class AuthService {
  login(user) {
    return axios({
      method: "post",
      url: API_URL + "login",
      data: user,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then(response => {
        // if (response.data.accessToken) {
        console.log("2222222");
        if (response.data.code != -1) {
          console.log("11111");
          localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;

      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios({
      method: "post",
      url: API_URL + "reg",
      data: user,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then(response => {
        // if (response.data.accessToken) {
        console.log("REG");
        console.log(response.data);
        // }

        return response;
      });;
  }
}

export default new AuthService();