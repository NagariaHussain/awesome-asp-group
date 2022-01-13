import "./main.css";
import { createApp } from "vue";

import App from './App.vue';

import axios from "axios";

const api = axios.create({
	baseURL: "/api/",
});
const app = createApp(App);

app.provide("$api", api);
app.mount("#app");
