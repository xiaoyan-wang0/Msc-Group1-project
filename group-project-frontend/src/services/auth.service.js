import axios from 'axios';
import env from "@/env.js";

// const API_URL = '/api/member/';
const API_URL = env.AMDBAPI + '/member/';

class AuthService {
  login(user) {
    return axios({
      method: "post",
      url: API_URL + "login",
      data: user,
      // withCredentials: true,
      headers: { "Content-Type": "multipart/form-data" },
    })
      .then(response => {
        // if (response.data.accessToken) {
        console.log("2222222");
        console.log(response);
        if (response.data.code != -1) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;

      });
  }

  logout() {
    localStorage.removeItem('user');
    return axios({
      method: "get",
      url: API_URL + "logout",
    })
      .then(response => {
        // if (response.data.accessToken) {
        return response.data;
      });
  }

  register(user) {
    return axios({
      method: "post",
      url: API_URL + "reg",
      data: user,
      headers: { "Content-Type": "multipart/form-data" },
    },
      // { withCredentials: true }
    )
      .then(response => {
        // if (response.data.accessToken) {
        console.log("REG");
        console.log(response.data);
        localStorage.setItem('user', JSON.stringify(response.data));
        // }
        return response;
      }).catch((error) => {
        console.log("error");
        console.log(error);
        console.log("error");
        showErroeMessage();
      });;
  }
}

export default new AuthService();