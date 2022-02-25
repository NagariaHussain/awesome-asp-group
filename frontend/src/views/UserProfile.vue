<template>
	<div class="mt-1 flex flex-row items-start justify-center gap-10">
		<div
			class="basis-4/12 items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm hover:border-gray-400"
		>
			<div>
				<div class="flex justify-end">
					<div>
						<button
							type="button"
							class="mr-1 mb-1 inline-flex flex-shrink-0 items-center rounded border-transparent bg-gray-200 px-4 py-1.5 text-xs text-xs text-gray-600 shadow active:bg-gray-400"
							@click="toggleModal = !toggleModal"
						>
							<svg
								xmlns="http://www.w3.org/2000/svg"
								class="h-4 w-4"
								fill="none"
								viewBox="0 0 24 24"
								stroke="currentColor"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z"
								/>
							</svg>
							<span class="ml-1">Edit</span>
						</button>
					</div>
				</div>
				<div class="mt-3 grid grid-cols-1 justify-items-center">
					<div>
						<img src="/src/assets/logo.png" alt="profile img" />
					</div>
					<div>
						<p class="font-sans text-lg font-medium">
							{{ userStore.account.first_name }}
							{{ userStore.account.last_name }}
						</p>
					</div>
					<div>
						<p class="text-slate-500">{{ title }}</p>
					</div>
				</div>
				<div
					class="mt-8 mb-8 border-gray-400 text-gray-200"
					v-if="title"
				>
					<hr />
				</div>
				<div class="grid grid-cols-1 justify-items-start space-y-4">
					<div v-if="age">
						<p>
							<span class="font-mono font-semibold">Age:</span>
							<span class="text-slate-700">{{ age }}</span>
						</p>
					</div>
					<div v-if="gender">
						<p>
							<span class="font-mono font-semibold">Gender:</span>
							<span class="text-slate-700">{{ gender }}</span>
						</p>
					</div>
					<div v-if="location">
						<p>
							<span class="font-mono font-semibold"
								>Location:</span
							>
							<span class="text-slate-700">{{ location }}</span>
						</p>
					</div>
					<div v-if="desired_salary">
						<p>
							<span class="font-mono font-semibold"
								>Desired Salary:</span
							>
							<span class="text-slate-700"
								>{{ desired_salary }}$</span
							>
						</p>
					</div>
					<div v-if="desired_location">
						<p>
							<span class="font-mono font-semibold"
								>Desired Location:</span
							>
							<span class="text-slate-700">{{
								desired_location
							}}</span>
						</p>
					</div>
				</div>
			</div>
		</div>
		<div
			class="basis-6/12 items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm hover:border-gray-400"
		>
			<div>
				<div class="align-center flex justify-between">
					<div>
						<p class="text-lg font-medium">About</p>
					</div>
				</div>
				<div class="mt-5">
					<p class="text-sm font-light text-slate-600">
						{{ about ?? 'Not Set' }}
					</p>
				</div>
				<div class="mt-8 mb-8 border-gray-400 text-gray-200">
					<hr />
				</div>

				<div class="align-center flex justify-between">
					<div>
						<p class="text-lg font-medium">Work Experience</p>
					</div>
				</div>
				<div>
					<div
						class="mt-5"
						v-for="experience in work_experience"
						:key="experience.start_date"
					>
						<p class="font-medium">{{ experience.title }}</p>
						<div class="flex justify-between">
							<p class="mt-1 text-sm">{{ experience.company }}</p>
							<p class="mt-1 text-sm">
								{{ experience.location }}
							</p>
							<p class="mt-1 text-sm">
								{{ experience.start_date }} -
								{{ experience.end_date }}
							</p>
						</div>
						<p class="mt-3 text-sm font-light text-slate-600">
							{{ experience.description }}
						</p>
					</div>
				</div>
				<div class="mt-8 mb-8 border-gray-400 text-gray-200">
					<hr />
				</div>

				<div class="align-center flex justify-between">
					<div>
						<p class="text-lg font-medium">Skills & Technologies</p>
					</div>
				</div>
				<div class="mt-5 flex flex-row flex-wrap">
					<p
						class="mt-2 mr-2 rounded bg-yellow-100 px-2.5 py-0.5 text-sm font-medium text-yellow-800 dark:bg-violet-200 dark:text-violet-900"
						v-for="st in skills_and_technologies"
						:key="st"
					>
						{{ st }}
					</p>
				</div>
			</div>
		</div>
	</div>

	<div
		v-if="toggleModal"
		class="fixed inset-0 z-50 flex items-center justify-center overflow-y-auto overflow-x-hidden"
	>
		<div class="relative mx-auto w-1/3 py-5 sm:w-full md:w-full lg:w-2/4">
			<div class="w-full rounded bg-white shadow-2xl">
				<div class="px-5 py-5">
					<app-tabs
						class="bg-blue flex w-full flex-wrap"
						:tabList="tabList"
						variant="horizontal"
					>
						<template v-slot:tabPanel-1>
							<div>
								<form class="flex flex-col space-y-6">
									<div
										class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
									>
										<label
											for="title"
											class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
											>Title</label
										>
										<input
											type="text"
											name="title"
											v-model="title"
											id="title"
											class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											placeholder="Your Title"
										/>
									</div>

									<div class="flex flex-row gap-3">
										<div
											class="relative basis-1/3 rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="age"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Age</label
											>
											<input
												type="number"
												name="age"
												v-model="age"
												id="age"
												class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
												placeholder="Your Age"
											/>
										</div>
										<div
											class="relative basis-1/3 rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="desired-salary"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Desired Salary</label
											>
											<div
												class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3"
											>
												<span
													class="text-gray-500 sm:text-sm"
												>
													$
												</span>
											</div>
											<input
												type="number"
												name="desired-salary"
												v-model="desired_salary"
												id="desired-salary"
												class="block w-full border-0 p-0 pl-5 pr-2 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
												placeholder="Your Title"
											/>
											<div
												class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-3"
											>
												<span
													class="text-gray-500 sm:text-sm"
													id="price-currency"
												>
													USD
												</span>
											</div>
										</div>

										<div
											class="relative basis-1/3 rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="age"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Gender</label
											>
											<select
												id="gender"
												v-model="gender"
												name="gender"
												autocomplete="gender"
												class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											>
												<option>Male</option>
												<option>Female</option>
											</select>
										</div>
									</div>

									<div
										class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
									>
										<label
											for="location"
											class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
											>Location</label
										>
										<input
											type="text"
											name="location"
											v-model="location"
											id="location"
											class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											placeholder="Your Location"
										/>
									</div>

									<div
										class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
									>
										<label
											for="desired-location"
											class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
											>Desired Location</label
										>
										<input
											type="text"
											name="desired-location"
											v-model="desired_location"
											id="desired-location"
											class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											placeholder="Desired Location"
										/>
									</div>
								</form>
							</div>
						</template>
						<template v-slot:tabPanel-2>
							<div>
								<form>
									<div
										class="relative h-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
									>
										<label
											for="about"
											class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
											>About</label
										>

										<textarea
											id="about"
											name="about"
											v-model="about"
											rows="10"
											class="block h-full w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
										/>
									</div>
								</form>
							</div>
						</template>
						<template v-slot:tabPanel-3>
							<div>
								<form>
									<!--									<div v-if="work_experience && work_experience.length > 0">-->
									<div
										v-for="experience in work_experience"
										:key="experience.start_date"
										class="space-y-6"
									>
										<div
											class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="work-experience-title"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Title</label
											>
											<input
												type="text"
												name="work-experience-title"
												v-model="experience.title"
												id="work-experience-title"
												class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
												placeholder="Title"
											/>
										</div>
										<div
											class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="work-experience-company"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Company</label
											>
											<input
												type="text"
												name="work-experience-company"
												v-model="experience.company"
												id="work-experience-company"
												class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
												placeholder="Company"
											/>
										</div>
										<div
											class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="work-experience-location"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Location</label
											>
											<input
												type="text"
												name="work-experience-location"
												v-model="experience.location"
												id="work-experience-location"
												class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
												placeholder="Location"
											/>
										</div>

										<div class="flex flex-row gap-4">
											<div
												class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
											>
												<label
													for="work-experience-start-date"
													class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
													>Start Date</label
												>
												<input
													type="text"
													name="work-experience-start-date"
													v-model="
														experience.start_date
													"
													id="work-experience-start-date"
													class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
													placeholder="Start Date"
												/>
											</div>
											<div
												class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
											>
												<label
													for="work-experience-end-date"
													class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
													>End Date</label
												>
												<input
													type="text"
													name="work-experience-start-date"
													v-model="
														experience.end_date
													"
													id="work-experience-end-date"
													class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
													placeholder="End Date"
												/>
											</div>
										</div>

										<div
											class="relative h-full rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
										>
											<label
												for="description"
												class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
												>Description</label
											>

											<textarea
												id="description"
												name="about"
												v-model="experience.description"
												rows="10"
												class="block h-full w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											/>
										</div>
									</div>
								</form>
							</div>
						</template>
						<template v-slot:tabPanel-4>
							<div>
								<div>
									<div
										class="relative rounded-md border border-gray-300 px-3 py-2 shadow-sm focus-within:border-sky-600 focus-within:ring-1 focus-within:ring-sky-600"
									>
										<label
											for="skills_and_technologies"
											class="absolute -top-2 left-2 -mt-px inline-block bg-white px-1 text-xs font-medium text-gray-900"
										>
											Skills & Technologies</label
										>
										<input
											type="text"
											name="skills_and_technologies"
											v-on:keyup.enter="addNewSkill"
											id="skills_and_technologies"
											class="block w-full border-0 p-0 text-gray-900 placeholder-gray-500 focus:ring-0 sm:text-sm"
											placeholder="Add all keywords"
										/>
									</div>
								</div>

								<div class="flex w-96 flex-wrap">
									<span
										class="mt-2 mr-2 rounded bg-yellow-100 px-2.5 py-0.5 text-sm font-medium text-yellow-800 dark:bg-violet-200 dark:text-violet-900"
										v-for="st in skills_and_technologies"
										:key="st"
									>
										{{ st }}
										<button
											type="button"
											@click="remove_st(st)"
											class="ml-0.5 inline-flex h-4 w-4 flex-shrink-0 items-center justify-center rounded-full text-sky-400 hover:bg-sky-200 hover:text-sky-500 focus:bg-sky-500 focus:text-white focus:outline-none"
										>
											<span class="sr-only"
												>Remove large option</span
											>
											<svg
												class="h-2 w-2"
												stroke="currentColor"
												fill="none"
												viewBox="0 0 8 8"
											>
												<path
													stroke-linecap="round"
													stroke-width="1.5"
													d="M1 1l6 6m0-6L1 7"
												/>
											</svg>
										</button>
									</span>
								</div>
							</div>
						</template>
					</app-tabs>
				</div>
				<div class="flex flex-row-reverse gap-2 py-2 px-5">
					<div>
						<Button type="primary" @click="updateProfile"> Update </Button>
					</div>
					<div>
						<Button @click="toggleModal = false">Clase</Button>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div
		v-if="toggleModal"
		class="absolute inset-0 z-40 bg-black opacity-50"
	></div>
</template>

<script>
import AppTabs from '../components/AppTabs.vue';
import Button from '../components/Button.vue';
import {
	PencilIcon,
	IdentificationIcon,
	PuzzleIcon,
	BriefcaseIcon,
	DesktopComputerIcon,
} from '@heroicons/vue/outline';
import api from '../libs/api';
import { mapStores } from 'pinia';
import useUser from '../stores/useUser';

export default {
	components: {
		AppTabs,
		PencilIcon,
		IdentificationIcon,
		PuzzleIcon,
		BriefcaseIcon,
		Button,
	},
	data() {
		return {
			tabList: [
				{ name: 'Basic Information', icon: IdentificationIcon },
				{ name: 'About', icon: PuzzleIcon },
				{
					name: 'Work Experience',
					icon: BriefcaseIcon,
				},
				{ name: 'Skills & Technologies', icon: DesktopComputerIcon },
			],
			toggleModal: false,
			id: null,
			username: null,
			title: null,
			age: null,
			gender: null,
			location: null,
			desired_salary: null,
			desired_location: null,
			about: null,
			work_experience: null,
			skills_and_technologies: null,
			education: 'Bachelor dg, Goldsmiths, University of London',
		};
	},
	computed: {
		...mapStores(useUser),
	},
	mounted() {
		this.username = this.userStore.account.username;
		this.fetchProfile(this.username);
	},
	methods: {
		addNewSkill(e) {
			this.skills_and_technologies.push(e.target.value);
			e.target.value = '';
		},
		remove_st(e) {
			this.skills_and_technologies = this.skills_and_technologies.filter(
				function (ele) {
					return ele !== e;
				}
			);
		},
		addWorkExperience(e) {
			this.work_experience.push(e.target.value);
		},
		async updateProfile() {
			console.log('Update profile is triggered');

			let profile = {
				id: this.id,
				username: this.username,
				title: this.title,
				age: this.age,
				gender: this.gender,
				location: this.location,
				desired_location: this.desired_location,
				desired_salary: this.desired_salary,
				about: this.about,
				work_experience: this.work_experience,
				skills_technologies: this.skills_and_technologies,
				education: [],
				license_certification: [],
				languages: [],
			};

			if (this.id) {
				//UPDATE
				try {
					await api.put('v1/users/', profile);
				} catch (e) {
					console.log(e);
				}
			} else {
				//CREATE
				try {
					await api.post('v1/users/', profile);
				} catch (e) {
					console.log(e);
				}
			}

			this.toggleModal = !this.toggleModal;
		},
		async fetchProfile(username) {
			try {
				let profile = await api.get(`v1/users/${username}`);
				let data = profile.data;
				this.id = data['id'];
				this.title = data['title'];
				this.age = data['age'];
				this.gender = data['gender'];
				this.location = data['location'];
				this.desired_salary = data['desired_salary'];
				this.desired_location = data['desired_location'];
				this.about = data['about'];
				this.work_experience = data['work_experience'] ?? [
					{
						title: 'Put your title Here',
						company: 'Company',
						location: 'Location',
						start_date: 'Start Date',
						end_date: 'End Date',
						description:
							"There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
					},
				];
				this.skills_and_technologies = data['skills_technologies'] ?? [
					'SPEAKING',
					'READING',
					'WRITING',
				];
			} catch (e) {
				console.error(e);
			}
		},
	},
	name: 'UserProfile',
};
</script>

<style scoped></style>
