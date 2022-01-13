import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import proxyOptions from "./proxyOptions";

export default defineConfig({
	build: {
		outDir: "../backend/dist",
	},
	plugins: [vue()],
	server: {
		port: 3030,
		proxy: proxyOptions,
	},
});
