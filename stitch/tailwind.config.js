/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./app/**/*.{js,jsx,ts,tsx}",
    "./components/**/*.{js, jsx, ts, tsx}",
      "./app/(tabs)/index.tsx",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

