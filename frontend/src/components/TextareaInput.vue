<template>
	<div class="flex items-start space-x-4">
		<div class="flex-shrink-0">
			<img
				class="inline-block h-10 w-10 rounded-full"
				src="https://frappe.io/files/reema%202019-01-08%2014:48:53.JPG"
				alt=""
			/>
		</div>
		<div class="min-w-0 flex-1">
			<form @submit.prevent="onSubmit">
				<div
					class="border-b border-gray-200 focus-within:border-sky-600"
				>
					<label for="comment" class="sr-only"
						>Add your comment</label
					>
					<textarea
						v-model="modelValue"
						@input="onInput"
						rows="3"
						name="comment"
						id="comment"
						class="block w-full resize-none border-0 border-b border-transparent p-0 pb-2 focus:border-sky-600 focus:ring-0 sm:text-sm"
						placeholder="Add your comment..."
					/>
				</div>
				<div class="flex justify-between pt-2">
					<div class="flex items-center space-x-5">
						<div class="flow-root">
							<button
								@click.prevent="attachFile"
								type="button"
								class="-m-2 inline-flex h-10 w-10 items-center justify-center rounded-full text-gray-400 hover:text-gray-500"
							>
								<PaperClipIcon
									class="h-6 w-6"
									aria-hidden="true"
								/>
								<span class="sr-only">Attach a file</span>
							</button>
							<input
								class="hidden"
								type="file"
								name="uploaded_file"
								ref="attach_file_input"
								@change="handleFileUpload"
							/>
						</div>
					</div>
					<div class="flex-shrink-0">
						<button
							:disabled="loading"
							type="submit"
							class="inline-flex items-center rounded-md border border-transparent bg-sky-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-sky-500 focus:ring-offset-2 disabled:bg-slate-500 disabled:ring-0"
						>
							{{ !loading ? 'Post' : 'Post' }}
						</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
import { ref, inject } from 'vue';
import { PaperClipIcon } from '@heroicons/vue/outline';

// Emits
const props = defineProps({
	modelValue: String,
	loading: { type: Boolean, default: false },
});
const emit = defineEmits(['update:modelValue', 'submit']);

// declare a ref to hold the element reference
// the name must match template ref value
const attach_file_input = ref(null);
const inputValue = ref('');
const api = inject('$api');

const attachFile = () => attach_file_input.value.click();
const handleFileUpload = (e) => {
	const file = e.target.files[0];
	const formData = new FormData();

	formData.append('uploaded_file', file);

	// Use axios to upload the file
	api.post('/upload-interview-attachment', formData, {
		headers: {
			'Content-Type': 'multipart/form-data',
		},
	}).then((response) => {
		console.log(response);
	});
};

function onInput(event) {
	const inputValue = event.target.value;
	emit('update:modelValue', inputValue);
}

function onSubmit() {
	emit('submit', inputValue.value);
}
</script>
