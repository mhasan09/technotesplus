import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const Vue = createApp(App)
Vue.use(router)
createApp(App).use(router).mount('#app')
