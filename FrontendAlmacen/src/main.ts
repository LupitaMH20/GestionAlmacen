import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import "@fontsource/poppins/400.css"
import "@fontsource/poppins/500.css"
import "@fontsource/poppins/600.css"
import "@fontsource/poppins/700.css"
import router from './router/index'
import VueApexCharts from 'vue3-apexcharts'

const app = createApp(App)

app.use(router)
app.use(VueApexCharts)
app.component('ApexCharts', VueApexCharts)

app.mount('#app')
