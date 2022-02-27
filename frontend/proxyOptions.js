const webserver_port = 8084;

module.exports = {
	'^/(api|assets|files|ws)': {
		target: `http://localhost:${webserver_port}`,
		ws: true,
		router: function (req) {
			const site_name = req.headers.host.split(':')[0];
			return `http://${site_name}:${webserver_port}`;
		},
	},
};
