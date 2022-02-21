import Home from '../views/Home.vue';
import Jobs from '../views/Jobs.vue';
import About from '../views/About.vue';
import HomeDashboard from '../views/HomeDashboard.vue';
import Postings from '../views/Postings.vue';
import Applicants from '../views/Applicants.vue';
import Company from '../views/Company.vue';
import NewJobPosting from '../views/NewJobPosting.vue';
import JobPostingDetail from '../views/JobPostingDetail.vue';

import authRoutes from './auth';
import UserProfile from "../views/UserProfile.vue";

export default [
	{
		path: '/',
		component: Home,
		children: [
			{ path: '/', component: HomeDashboard },
			{ path: '/postings', component: Postings },
			{ path: '/postings/new', component: NewJobPosting },
			{ path: '/postings/:id', component: JobPostingDetail, props: true },
			{ path: '/applicants', component: Applicants },
			{ path: '/company', component: Company },
			{path: '/profile', component: UserProfile}
		],
		meta: { requiresAuth: true },
	},
	{ path: '/jobs', component: Jobs },
	{ path: '/about', component: About },
	...authRoutes,
];
