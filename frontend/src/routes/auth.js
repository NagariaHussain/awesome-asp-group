import Login from '../views/Login.vue';
import Signup from '../views/Signup.vue';

export default [
	{ path: '/login', component: Login, meta: { isLoginPage: true } },
	{ path: '/signup', component: Signup, meta: { isLoginPage: true } },
];
