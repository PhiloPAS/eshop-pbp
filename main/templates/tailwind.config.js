/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/*.py"],
  theme: {
    extend: {
      colors: {
        'footy-green': '#166534',
        'footy-yellow': '#facc15',
        'footy-red': '#dc2626',
      },
    },
  },
  plugins: [],
}
