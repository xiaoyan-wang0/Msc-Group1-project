
/**
 * reqquest header to check token( In furture).
 */
export default function authHeader() {
  let user = JSON.parse(localStorage.getItem('user'));
  if (user && user.accessToken) {
    return { Authorization: 'AMDB ' + user.accessToken };
  } else {
    return {};
  }
}