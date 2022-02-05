const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
	content: ["./index.html", "./src/**/*.{vue,js}"],
	theme: {
		extend: {
			fontFamily: {
				sans: ["Inter var", ...defaultTheme.fontFamily.sans],
			},
		},
	},
	plugins: [],
};
