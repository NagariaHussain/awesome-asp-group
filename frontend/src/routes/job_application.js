import JobApplicationDashboard from '../views/JobApplicationDashboard.vue';
export default [
	{
		name: 'ApplicationDashboard',
		path: '/application/:id',
		component: JobApplicationDashboard,
		props: true
	},
];
