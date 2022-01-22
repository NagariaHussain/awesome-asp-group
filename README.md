# awesome-asp-group

Awesome repo for awesome team.

## Contribution Notes:

1. Use semmantic commits (e.g. `feat: My new feature`, `fix: An old bug` etc.).

2. Use prettier for formatting frontend.

3. Use black for python formatting.

## Setup

1. Create and activate a new virtual environment

   ```bash
   $ virtualenv venv
   $ source venv/bin/activate
   ```

2. Install Requirements

   ```bash
   $ pip install -r requirements.txt
   ```

3. Running the server

   ```bash
   $ python backend/manage.py runserver
   ```

> manage.py is a CLI tool provided by django to carry out tasks like data migrations, creating super users etc.

## For front-end development

1. Install NodeJS (14+)

2. Install dependencies

   ```bash
   $ cd frontend && npm install
   ```

3. Install vite (Vite.js)

   ```bash
   $ npm install -g vite
   ```

4. Running the dev server

   ```bash
   # In frontend directory
   $ npm run dev
   ```

> Note: The frontend dev server runs on port `3000` while the django server runs on port `8000`

For re-building assets:

> Note: If new assets are to be generated use `npm run build` which will compile all the assets using Rollup.js and optimize bundle size
