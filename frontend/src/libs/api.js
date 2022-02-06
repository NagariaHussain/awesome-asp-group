import axios from 'axios';

const axiosApi = axios.create({
	baseURL: '/api/',
	headers: {
		'X-CSRFToken': getCSRFToken(),
	},
});

export default axiosApi;

function getCSRFToken() {
	const cookie = Object.fromEntries(
		document.cookie
			.split('; ')
			.map((part) => part.split('='))
			.map((d) => [d[0], decodeURIComponent(d[1])])
	);

	return cookie.csrftoken;
}
