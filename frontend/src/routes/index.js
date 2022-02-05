import Home from '../views/Home.vue';
import Jobs from '../views/Jobs.vue';
import About from '../views/About.vue';
import HomeDashboard from '../views/HomeDashboard.vue';
import Postings from '../views/Postings.vue';
import Applicants from '../views/Applicants.vue';
import Company from '../views/Company.vue';
import Login from '../views/Login.vue';

export default [
	{
		path: '/',
		component: Home,
		children: [
			{ path: '/', component: HomeDashboard },
			{ path: '/postings', component: Postings },
			{ path: '/applicants', component: Applicants },
			{ path: '/company', component: Company },
		],
	},
	{ path: '/jobs', component: Jobs, meta: { requiresAuth: true } },
	{ path: '/login', component: Login },
	{ path: '/about', component: About },
];
