import JobApplicationDashboard from '../views/JobApplicationDashboard.vue';
import JobApplicationInfo from '../views/JobApplicationInfo.vue';
import JobApplicationCommunication from '../views/JobApplicationCommunication.vue';
import JobApplicationOnboarding from '../views/JobApplicationOnboarding.vue';

export default [
	{
		name: 'ApplicationDashboard',
		path: '/application/:id',
		component: JobApplicationDashboard,
		props: true,
		children: [
			{
				path: 'interview',
				component: () => import('../views/JobApplicationInterview.vue'),
			},
			{
				path: 'info',
				component: JobApplicationInfo,
			},
			{
				path: 'onboarding',
				component: JobApplicationOnboarding,
			},
			{
				path: 'communication',
				component: JobApplicationCommunication,
			},
		],
	},
];
